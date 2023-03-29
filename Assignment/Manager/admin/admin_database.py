import sys

import mysql.connector

def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')
        print("Connected!")
    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn

def adminsearch(mobile, password):
    sql = "SELECT * FROM customer WHERE mobile=%s and password=%s"
    record = None
    values = (mobile, password)
    result = {'status': False, 'message': None}
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        record = cursor.fetchone()

        cursor.close()
        conn.close()
        result['status'] = True
        result['message'] = "Record save successfully"

    except:
        result['status'] = False
        result['message'] = sys.exc_info()
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        return record