import mysql.connector
from logger import Logger

class DatabaseConnectionError (Exception):
    pass

class DbConnection:
    def __init__(self):
        self.connection = None
        self.logger = Logger(self.__class__.__name__)
 
    def get_connection(self):
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = mysql.connector.connect(
                    host="localhost",
                    database="feedback_system",
                    user="root",
                    password="mysql2025#",
                )
                self.logger.writelog("Database connection established", level="info")
            except Exception as e:
                self.connection = None
                self.logger.writelog(f"Database connection error: {e}", level="error")
                raise DatabaseConnectionError("Error connecting to the database")
            
                       
        return self.connection

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.logger.writelog("Closing database connection", level="info")
            self.connection.close()



