import mysql.connector
from mysql.connector import Error
import os
import bcrypt
from dotenv import load_dotenv

dotenv_path='.env'
load_dotenv(dotenv_path=dotenv_path)

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
   

def connectSQL():
    try:
        connection = mysql.connector.connect(  
            database = DB_NAME,
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD   
            )
        if connection.is_connected():
            return connection
    except:
        raise ValueError("Error to connect database")
    

def executeQuery(query,params=None):
    db = connectSQL()
    if db:
        try:
            cursor = db.cursor()
            if params:
                cursor.execute(query,params)
                db.commit()
            else:
                cursor.execute(query)
            if query.strip().lower().startwith("select"):
                result = cursor.fetchall()
                return result
            
        except Error as e:
            raise ValueError(f'Erro executando query: {e}')
        finally:
            cursor.close()
            db.close()
    else:
        raise ValueError('Erro to connect database')