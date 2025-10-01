from databaseConnection import DbConnection
from logger import Logger, LogLevel


class DuplicateRegistrationError (Exception):
    pass
class InvalidCredentialError (Exception):
    pass

class student:
    def __init__(self):
        self.db = DbConnection()
        self.logger = Logger(self.__class__.__name__)   

    def Registration(self,name,email, password):
        print("Registration started")
        self.logger.writelog("Registration started", LogLevel.INFO)
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "select * from students where email = %s"
            cursor.execute(query,(email,))
            rows = cursor.fetchall()
            if (len(rows))>0:
                print("Student email is not registered")
                self.logger.writelog("Duplicate registration attempt", LogLevel.WARNING)
                raise DuplicateRegistrationError("Email already registered")
            query = "Insert into students(name,email, password) values(%s,%s,%s)"
            cursor.execute(query,( name, email, password))
            conn.commit()
            print(f"Student '{name}' is registered successfully !!")
            self.logger.writelog(f"Student '{name}' is registered successfully !!", LogLevel.INFO)
        except Exception as e:
            print (f"Exception occured {e} exception type : {type(e)}")
            self.logger.writelog(f"Exception occured {e} exception type : {type(e)}", LogLevel.ERROR)
            raise e
        finally:    
            cursor.close()
            self.db.close_connection()


    
    def Login(self, email, password): 
        print("Login starts")
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "select * from students where email = %s"
            cursor.execute(query,(email,))
            rows = cursor.fetchall()
            return_value = False
            if (len(rows))==0:
                print("Student mail not registered")
                self.logger.writelog("Student mail not registered", LogLevel.WARNING)
                return_value = False
            else:
                if rows[0][3] == password:
                    print("Successfully logged in")
                    self.logger.writelog("Successfully logged in", LogLevel.INFO)
                    return_value = True
                else:
                    print("Credential doesn't match")
                    self.logger.writelog("Credential    doesn't match", LogLevel.WARNING)
                    return_value = False
        except InvalidCredentialError as e:
            print(f"Exception occurred: {e}")
            self.logger.writelog(f"Exception occurred: {e} type: {type(e)}", LogLevel.ERROR)
            return_value = False    
        except Exception as e:
            print (f"Exception occured {e} exception type : {type(e)}")
            self.logger.writelog(f"Exception occured {e} exception type : {type(e)}", LogLevel.ERROR)
            return_value = False
        finally:    
            cursor.close()
            self.db.close_connection()
        return return_value