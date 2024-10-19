import mysql.connector
from app.DAO import credenciales as c

class Conexion:
    def __init__(self,host,user,password,database,):
        self.__database = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.__cursor = self.__database.cursor(dictionary=True)
        
    def get_cursor(self):
        return self.__cursor
        
    def fetchone(self):
        return self.__cursor.fetchone()
    
    def fetchall(self):
        return self.__cursor.fetchall()
    
    def commit(self):
        self.__database.commit()
    
    def rollback(self):
        self.__database.rollback()

    def disconnect(self):
        self.__cursor.close()
        self.__database.close()
        
conexion = Conexion(c.host,c.user,c.password,c.database)