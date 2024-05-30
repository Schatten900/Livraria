import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connectSQL():
    mydb = mysql.connector.connect(  
        database = os.getenv('DB_NAME'),
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
    )
    cursor = mydb.cursor()
    sql = ""
    val = ""
    #sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    #val = ("John", "Highway 21")
    cursor.execute(sql,val)