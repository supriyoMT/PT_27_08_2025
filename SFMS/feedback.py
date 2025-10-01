from databaseConnection import DbConnection
from logger import Logger, LogLevel

class feedback:
    def __init__(self):
        self.db = DbConnection()
        self.logger = Logger(self.__class__.__name__)


    def GetCourses(self):
        print("Fetching all courses")
        self.logger.writelog("Fetching all courses", LogLevel.INFO)
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "select * from courses"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print (f"Exception occured {e} exception type : {type(e)}")
            self.logger.writelog(f"Exception occured {e} exception type : {type(e)}", LogLevel.ERROR)
        finally:    
            cursor.close()
            self.db.close_connection()

    def GetStudentID(self, email):
        print("Get student ID by email")
        self.logger.writelog("Get student ID by email", LogLevel.INFO)
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "select studentid from students where email = %s"
            cursor.execute(query, (email,))
            rows = cursor.fetchall()
            return rows[0][0] if rows else None
        except Exception as e:
            print (f"Exception occured {e} exception type : {type(e)}")
            self.logger.writelog(f"Exception occured {e} exception type : {type(e)}", LogLevel.ERROR)
        finally:    
            cursor.close()
            self.db.close_connection()
    
    def saveFeedback(self, studentid, courseid, rating, comments):
        print("Save Feedback")
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "Insert into feedback(studentid,courseid, rating, comments) values(%s,%s,%s,%s)"
            cursor.execute(query,( studentid, courseid, rating, comments))
            conn.commit()
            print(f"Feedback from student '{studentid}' is saved succesfully !!")
            self.logger.writelog(f"Feedback from student '{studentid}' is saved succesfully !!", LogLevel.INFO)
        except Exception as e:
            print (f"Exception occured {e} exception type : {type(e)}")
            self.logger.writelog(f"Exception occured {e} exception type : {type(e)}", LogLevel.ERROR) 
        finally:    
            cursor.close()
            self.db.close_connection()

    def GetAllFeedback(self):
        print("Get All Feedback")
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                SELECT 
                    s.studentid, s.name, 
                    c.name, c.faculty_name,
                    f.rating, f.comments
                FROM students s
                INNER JOIN feedback f ON s.studentid = f.studentid
                INNER JOIN courses c ON c.id = f.courseid
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print (f"Exception occured {e} exception type : {type(e)}")
            self.logger.writelog(f"Exception occured {e} exception type : {type(e)}", LogLevel.ERROR)
        finally:    
            cursor.close()
            self.db.close_connection()
       

    def CheckDuplicateFeedback(self, studentid, courseid) -> bool:
        print("Check Duplicate Feedback")
        retVal = False
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "select * from feedback where studentid = %s and courseid = %s"
            cursor.execute(query,( studentid, courseid))
            rows = cursor.fetchall()
            if (len(rows))==0:
                retVal = False
            else:
                retVal = True 
        except Exception as e:
            retVal = True
            print (f"Exception occured {e} exception type : {type(e)}")
            self.logger.writelog(f"Exception occured {e} exception type : {type(e)}", LogLevel.ERROR)
        finally:    
            cursor.close()
            self.db.close_connection()
        return retVal