import mysql.connector
from mysql.connector import Error
import os
import bcrypt
import random
from dotenv import load_dotenv

dotenv_path='.env'
flaskSecret = os.getenv('FLASK_KEY')
load_dotenv(dotenv_path=dotenv_path)

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
   

def connectSQL():
    try:    #conecta ao banco de dados
        connection = mysql.connector.connect(  
            database = DB_NAME,
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD   
            )
        if connection.is_connected():
            return connection
    except Error as e:
        raise ValueError(f"Error to connect database: {e}")
    

def executeQuery(query,params=None):
    db = connectSQL()
    if db:
        try:
            cursor = db.cursor()
            if params:
                if not isinstance(params, (list, tuple)):
                    params = (params,)
                cursor.execute(query,params)

            else:
                cursor.execute(query)

            if query.strip().lower().startswith("select"):
                result = cursor.fetchall()
            else:
                db.commit()
                result = None
            return result
            
        except Error as e:
            raise ValueError(f'Erro ao executar a query: {e}')
        
        finally:
            if cursor is not None:
                cursor.close()

            if db.is_connected():
                db.close()
    else:
        raise ValueError('Erro to connect database')