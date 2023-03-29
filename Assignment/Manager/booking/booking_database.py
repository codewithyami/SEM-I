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


def bookinginsert(booking):
    sql = "INSERT INTO booking VALUES (%s,%s, %s, %s, %s, %s, %s, %s,%s)"
    values = (booking.getCID(), "", booking.getDate(), booking.getTime(), booking.getPick_Up(), booking.getDestination(),booking.getStatus(),"","")
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


def bookinggetAll():
    conn = None

    # Retrieve or select records
    sql = "SELECT * FROM booking"
    # value = (status,)
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

def bookinggetAll1(cid):
    conn = None

    # Retrieve or select records
    sql = "SELECT * FROM booking WHERE cid=%s"
    value = (cid)
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

def bookinggetAll2(did):
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

def bookinggetAll3():
    conn = None

    # Retrieve or select records
    sql = "SELECT * FROM booking WHERE status='pending'"
    # value = ()
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



def bookingsearch(cid,):
    sql = "SELECT * FROM booking WHERE cid=%s"
    record = None
    values = (cid,)
    result = {'status': False, 'message': None}
    try:
        conn = connect()
        cursor = conn.cursor(buffered=True)
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


def bookingsearch1(bid):
    sql = "SELECT did FROM booking WHERE bid=%s"
    record = None
    values = (bid,)
    result = {'status': False, 'message': None}
    try:
        conn = connect()
        cursor = conn.cursor(buffered=True)
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

def bookingedit(newbooking):
    conn = None
    # update or edit records
    sql = "UPDATE booking SET cid=%s, date=%s, time=%s, pick_up=%s, destination=%s, status=%s WHERE bid=%s"
    # sql = "UPDATE`booking` SET `cid` = '%s', `date` = '%s', `time` = '%s', `pick_up` = '%s', `destination` = '%s', `status` = '%s' WHERE bid = '%s'"
    values = (newbooking.getCID(), newbooking.getDate(), newbooking.getTime(), newbooking.getPick_Up(), newbooking.getDestination(), newbooking.getStatus(), newbooking.getBID(),)
    result = False
    try:
        # pass #input, process, output
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
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
        del sql, values
        return result

def bookingcancel(newbooking):
    conn = None
    # update or edit records
    sql = "UPDATE booking SET status=%s WHERE bid=%s AND status=%s"
    status = "Cancelled"
    status1= "active"
    # sql = "UPDATE`booking` SET `cid` = '%s', `date` = '%s', `time` = '%s', `pick_up` = '%s', `destination` = '%s', `status` = '%s' WHERE bid = '%s'"
    values = (status, newbooking, status1)
    result = False
    try:
        # pass #input, process, output
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
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
        del sql, values
        return result

def bookingcancel1(newbooking):
    conn = None
    # update or edit records
    sql = "UPDATE booking SET status=%s WHERE bid=%s AND status=%s"
    status = "Cancelled"
    status1= "pending"
    # sql = "UPDATE`booking` SET `cid` = '%s', `date` = '%s', `time` = '%s', `pick_up` = '%s', `destination` = '%s', `status` = '%s' WHERE bid = '%s'"
    values = (status, newbooking, status1)
    result = False
    try:
        # pass #input, process, output
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
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
        del sql, values
        return result


def bookingdelete(bid):
    conn = None
    # update or edit records
    sql = "DELETE FROM booking  WHERE bid=%s"
    values = (bid,)
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



def insert2(booking):
    sql = "INSERT INTO booking VALUES (%s,%s, %s, %s, %s, %s, %s)"
    values = (booking.getCID(), booking.getBID(), booking.getDate(), booking.getTime(), booking.getPick_Up(), booking.getDestination(),booking.getStatus())
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