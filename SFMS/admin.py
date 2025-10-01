from databaseConnection import DbConnection
from logger import Logger, LogLevel


class DuplicateRegistrationError (Exception):
    pass
class InvalidCredentialError (Exception):
    pass

class admin:
    def __init__(self):
        self.db = DbConnection()
        self.logger = Logger(self.__class__.__name__)

    def Registration(self,name, password):
        print("Registration starts")
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "select * from admins where username = %s"
            cursor.execute(query,(name,))
            rows = cursor.fetchall()
            if (len(rows))>0:
                print("Admin name is already registered")
                self.logger.writelog("Duplicate registration attempt found", LogLevel.WARNING)
                raise DuplicateRegistrationError("Name is already registered")
            query = "Insert into admins(username, password) values(%s,%s)"
            cursor.execute(query,( name, password))
            conn.commit()
            print(f"Admin '{name}' is registered successfully.")
            self.logger.writelog(f"Admin '{name}' is registered successfully.", LogLevel.INFO)
        except Exception as e:
            print (f"Exception occured {e} exception type : {type(e)}")
            self.logger.writelog(f"Exception occured {e} exception type : {type(e)}", LogLevel.ERROR)
            raise e
        finally:
            cursor.close()
            self.db.close_connection()      

    def Login(self, user, password): 
        print("Admin Login starts")
        self.logger.writelog("Admin Login starts", LogLevel.INFO)
        return_value = False
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "select * from admins where username = %s"
            cursor.execute(query,(user,))
            rows = cursor.fetchall()
            if (len(rows))==0:
                print("The User is not admin")
                self.logger.writelog("The User is not admin", LogLevel.WARNING)
                return_value = False
            else:
                if rows[0][2] == password:
                    print("Successfully logged in as admin")
                    self.logger.writelog("Successfully logged in as admin", LogLevel.INFO)  
                    return_value = True
                else:
                    print("Admin Credential doesnot match")
                    self.logger.writelog("Admin Credential doesnot match", LogLevel.WARNING)
                    raise InvalidCredentialError("Invalid admin credential")
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
