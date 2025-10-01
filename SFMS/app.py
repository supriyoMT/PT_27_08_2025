from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
from logger import Logger, LogLevel
from student import student
from feedback import feedback as Feedback
from admin import admin as Admin
from os import path as Path

class DuplicateFeedbackError (Exception):
    pass

app = Flask(__name__)
app.secret_key = "secret"   # needed for sessions & flash

logger = Logger("StudentsFeedbackManagement")

BASE_DIR = Path.dirname(Path.abspath(__file__))
LOG_FILE = Path.join(BASE_DIR, "app.log")

 
# ----------------------------
# ROUTE register
# ----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        new_student = student()

        try:
            new_student.Registration(name, email, password)
            logger.writelog(f"Registration is successful for email={email}", LogLevel.INFO)
            flash("Registration is successful! Please login.", "success")
            return redirect(url_for("login"))

        except Exception as e:
            logger.writelog(f"Duplicate registration attempted for email={email}", LogLevel.WARNING)
            flash("Email already registered!", "Warning")

    return render_template("register.html")


# ----------------------------
# ROUTE login
# ----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        student_login = student()

        if student_login and student_login.Login(email, password):
            session["email"] = email
            logger.writelog(f"Login successful for email={email}", LogLevel.INFO)
            flash("Login successful!", "success")
            return redirect(url_for("submit_feedback", email=email))
        else:
            logger.writelog(f"Login failed for email={email}", LogLevel.WARNING)
            flash("Invalid email or password!", "warning")

    return render_template("login.html")


# ----------------------------
# ROUTE: submit_feedback
# ----------------------------
@app.route("/submit_feedback", methods=["GET", "POST"])
def submit_feedback():
    email = request.args.get("email") 
    if "email" not in session or session["email"] != email:
        flash("Student not logged in. Please login.", "danger")
        logger.writelog("Unauthorized access attempt to submit feedback.", LogLevel.WARNING)
        return redirect(url_for("login"))
    studentfeedback = Feedback()
    student_id = studentfeedback.GetStudentID(email)
    if not student_id:
        flash("Student not found. Please login again.", "danger")
        logger.writelog(f"Student ID not found for email={email}", LogLevel.ERROR)
        return redirect(url_for("login"))
    courses = studentfeedback.GetCourses()  # Fetch all courses for dropdown
    print(courses)

    if request.method == "POST":
        course_id = int(request.form["course_id"])
        rating = int(request.form["rating"])
        comments = request.form["comments"]

        try:
            # Duplicate check
            existing = studentfeedback.CheckDuplicateFeedback(student_id, course_id)
            if existing:
                flash("Feedback already submitted for this course.", "danger")
                logger
                raise DuplicateFeedbackError("Feedback already submitted for this course.")

            # Insert feedback
            studentfeedback.saveFeedback(student_id, course_id, rating, comments)

            logger.writelog(f"Feedback submitted: student={student_id}, course={course_id}", LogLevel.INFO)
            flash("Feedback submitted successfully!", "success")
            return redirect(url_for("login"))

        except DuplicateFeedbackError as e:
            logger.writelog(f"Duplicate feedback attempt: student={student_id}, course={course_id}", LogLevel.WARNING)
            flash(str(e), "warning")
        except Exception as e:
            logger.writelog(f"Feedback submission failed: {str(e)}", LogLevel.ERROR)
            flash("An error occurred while submitting feedback.", "error")

    return render_template("feedback_form.html", courses=courses)


# ROUTE Admin login
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        admin = Admin()

        if admin and admin.Login(username, password):
            session["is_admin"] = True
            logger.writelog(f"Admin logged in: {username}", LogLevel.INFO)
            return redirect(url_for("view_feedback"))
        else:
            logger.writelog(f"Failed admin login attempt: {username}", LogLevel.WARNING)
            flash("Invalid username or password", "warning")

    return render_template("admin_login.html")

# ----------------------------
# ROUTE register
# ----------------------------
@app.route("/admin/register", methods=["GET", "POST"])
def admin_register():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        admin = Admin()

        try:
            admin.Registration(name, password)
            logger.writelog(f"Admin Registration successful for name ={name}", LogLevel.INFO)
            flash("Registration successful! Please login.", "success")
            return redirect(url_for("admin_login"))

        except Exception as e:
            logger.writelog(f"Duplicate registration attempt for name={name}", LogLevel.WARNING)
            flash("Name already registered!", "warning")

    return render_template("admin_register.html")


# ----------------------------
# ROUTE view_feedback
# ----------------------------
@app.route("/admin/view_feedback")
def view_feedback():
    logger.writelog("Admin accessed view_feedback route.", LogLevel.INFO)
    if not session.get("is_admin"):
        logger.writelog("Unauthorized access attempt to view feedback.", LogLevel.WARNING)  
        flash("Unauthorized! Please login as admin.", "danger")
        return redirect(url_for("admin_login"))

    feedbacks = Feedback().GetAllFeedback()
    print (feedbacks)
    logger.writelog(f"Fetched {len(feedbacks)} feedback entries.", LogLevel.INFO)

    return render_template("view_feedback.html", feedbacks=feedbacks)

# ----------------------------
# ROUTE download_log
# ----------------------------
@app.route("/admin/download_log")
def download_log():
    logger.writelog("Admin accessed download_log route.", LogLevel.INFO)
    if not session.get("is_admin"):
        logger.writelog("Unauthorized access attempt to download log.", LogLevel.WARNING)
        flash("Unauthorized! Please login as admin.", "warning")
        return redirect(url_for("admin_login"))

    if Path.exists(LOG_FILE):
        
        logger.writelog(f"Log file path: {LOG_FILE}", LogLevel.INFO)
        logger.writelog("Log file downloading by admin.", LogLevel.INFO)
        return send_file(LOG_FILE, as_attachment=True)
    else:
        flash("Log file not found!", "error")
        logger.writelog("Log file not found!", LogLevel.ERROR)
        return redirect(url_for("view_feedback"))




if __name__ == '__main__':
    app.run(debug=True)