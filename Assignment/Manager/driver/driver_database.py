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


def driverinsert(user):
    sql = "INSERT INTO driver VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = ("", user.getName(), user.getAddress(), user.getMobile(), user.getEmail(), user.getAGE(), user.getGender(), user.getNumber_Plate(),
              user.getPassword(), user.getStatus())
    result = {'status': False, 'message': None}
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result['status'] = True
        result['message'] = "Record save successfully"
        print("Inserted!")
    except:
        result['status'] = False
        result['message'] = sys.exc_info()
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        return result


def drivergetAll():
    conn = None

    # Retrieve or select records
    sql = "SELECT * FROM driver"
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

def drivergetAll2():
    conn = None

    # Retrieve or select records
    sql = "SELECT mobile FROM driver"
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

def drivergetAll1(did):
    conn = None

    # Retrieve or select records
    sql = "SELECT * FROM booking WHERE did=%s"
    value = (did)
    records = None

    try:
        # pass #input, process, output
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, value)
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

def drivergetAllavailable():
    conn = None

    # Retrieve or select records
    sql = "SELECT * FROM driver WHERE status='open'"
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

def driversearch(mobile, password):
    sql = "SELECT * FROM driver WHERE mobile=%s and password=%s"
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

def driversearch1(did):
    sql = "SELECT * FROM driver WHERE did=%s"
    record = None
    values = (did)
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

def driveredit(newuser):
    conn = None
    # update or edit records
    sql = "UPDATE driver set name=%s, address=%s, mobile=%s, email=%s, dob=%s, gender=%s, password=%s WHERE cid=%s"
    values = (newuser.getName(), newuser.getAddress(), newuser.getMobile(), newuser.getEmail(), newuser.getDOB(),
              newuser.getGender(), newuser.getPassword(), newuser.getCID())
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

def driveredit1(new):
    conn = None
    # update or edit records
    sql = "UPDATE driver set status=%s WHERE did=%s"
    status = "open"
    values = (status, new)

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
    conn = None
    # update or edit records
    sql = "DELETE FROM driver WHERE cid=%s"
    values = (cid,)
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

def deleteDriver(did):
    conn = None
    # update or edit records
    sql = "DELETE FROM driver WHERE did=%s"
    values = (did)
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

