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

def customerinsert(user):
    sql = "INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = ("", user.getName(), user.getAddress(), user.getMobile(), user.getEmail(), user.getDOB(), user.getGender(), user.getPassword())
    result = {'status':False, 'message':None}
    try:
        conn = connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result['status']=True
        result['message']="Record save successfully"
        print("Inserted!")
    except:
        result['status'] = False
        result['message'] = sys.exc_info()
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        return result

def customergetAll():
    conn=None
    
    # Retrieve or select records
    sql = "SELECT * FROM customer"
    records = None
    
    try:
        # pass #input, process, output
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        
        print(records)
    except:
        # pass #error message
        print("Error : ", sys.exc_info())
    finally:
        # pass #Remove all used resources
        del sql
        return records


def customergetAll1(mobile):
    conn = None

    # Retrieve or select records
    sql = "SELECT mobile FROM customer WHERE mobile=%s"
    value =(mobile)
    records = None

    try:
        # pass #input, process, output
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, value)
        records = cursor.fetchone()
        cursor.close()
        conn.close()

        print(records)
    except:
        # pass #error message
        print("Error : ", sys.exc_info())
    finally:
        # pass #Remove all used resources
        del sql
        return records
        


def customersearch(mobile, password):
    sql = "SELECT * FROM customer WHERE mobile=%s and password=%s"
    record = None
    values = (mobile, password)
    result = {'status':False, 'message':None}
    try:
        conn = connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        record = cursor.fetchone()
        
        cursor.close()
        conn.close()
        result['status']=True
        result['message']="Record save successfully"
        
    except:
        result['status'] = False
        result['message'] = sys.exc_info()
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        return record



def customersearch1(cid):
    sql = "SELECT * FROM customer WHERE cid=%s"
    record = None
    values = (cid)
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



def customeredit(newuser):
    conn=None
    # update or edit records
    sql = "UPDATE customer set name=%s, address=%s, mobile=%s, email=%s, dob=%s, gender=%s, password=%s WHERE cid=%s"
    values = (newuser.getName(), newuser.getAddress(), newuser.getMobile(), newuser.getEmail(), newuser.getDOB(), newuser.getGender(), newuser.getPassword(), newuser.getCID())
    result = False
    try:
        # pass #input, process, output
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
        print("Update successfully")
        
    except:
        # pass #error message
        print("Error : ", sys.exc_info())
    finally:
        # pass #Remove all used resources
        del values, sql
        return result


def customerdelete(cid):
    conn=None
    # update or edit records
    sql = "DELETE FROM customer WHERE cid=%s"
    values = (cid)
    result = False
    # Connect with db
    # update records
    # Close connection
    try:
        # pass #input, process, output
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
        print("Delete successfully")
    except:
        # pass #error message
        print("Error : ", sys.exc_info())
    finally:
        # pass #Remove all used resources
        del values, sql
        return result

