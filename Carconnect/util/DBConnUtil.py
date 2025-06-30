# util/DBConnUtil.py

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='janalyn@6205',  
        database='CarConnectDB'
    )
