
from tkinter import *

from Assignment.Classes.Driver.driver_class import driverregister
from Assignment.Classes.Customer.Register import register
from Assignment.Manager.booking.booking_database import *
from Assignment.Manager.driver.driver_database import *
from Assignment.Manager.customer.database import *
from tkinter import ttk
import messagebox
from tkcalendar import DateEntry


# create a class for admin dashboard
# every frame will work inside this class where tkinter is pass while calling the class ADMIN
class ADMIN():
    def __init__(self, master):
        super().__init__()
        # passing the master to create a framework
        self.Window_main = master

        screen_width = self.Window_main.winfo_screenwidth()
        screen_height = self.Window_main.winfo_screenheight()

        #creating seperate frames for an individual widgit purpose
        self.side_frame = Frame(self.Window_main, bg="#A7DBD8", height=screen_height, width=screen_width)
        self.side_frame.pack(side=LEFT, fill=BOTH)
        self.side_frame.pack_propagate(False)

        self.main_frame = Frame(self.side_frame, bg="#F38630", height=510, width=990)
        self.main_frame.pack(side=RIGHT, fill=BOTH, anchor=SE)

        self.booking_frame = Frame(self.main_frame, bg="#E0E4CC", height=450, width=800)
        self.booking_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

        #main buttons which will help to call the function as per needed
        dashboard_btn = Button(self.side_frame, text="Dashboard", font=("San Francisco", 20))
        confirm_booking_btn = Button(self.side_frame, text="Confirm Booking", command=self.Confirm_booking_btn)
        tripinfo_btn = Button(self.side_frame, text="Trip Information", command=self.tripinfo)
        add_user_btn = Button(self.side_frame, text="Add User", command=self.Add_account)
        add_Driver_btn = Button(self.side_frame, text="Add Driver", command=self.Add_Driver)
        logout_btn = Button(self.side_frame, text="Logout", command=self.btn_clicked)

        dashboard_btn.place(x=2, y=50)
        confirm_booking_btn.place(x=13, y=200)
        tripinfo_btn.place(x=13, y=250)
        add_user_btn.place(x=13, y=300)
        add_Driver_btn.place(x=13, y=350)
        logout_btn.place(x=13, y=400)

    # function to delete the widgit while switching between different function operation
    def delete_frame(self):
        for frame in self.booking_frame.winfo_children():
            frame.destroy()

    # function to redirect in login page
    def btn_clicked(self):
        messagebox.askyesno("Confirm", "Do you really want to logout")
        while True:
            self.login()

    def login(self):
        self.Window_main.destroy()
        from Assignment.UI import UI
        return UI
        pass

    #function to assign driver to the customer
    def Confirm_booking_btn(self):
        # removing widgit
        self.delete_frame()

        # Send values to search (database) all the pending trips
        conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')
        cursor = conn.cursor()
        sql = "SELECT * FROM booking WHERE status='Pending'"
        cursor.execute(sql)
        records = cursor.fetchall()

        lblMessage = Label(self.booking_frame, text='')
        lblMessage.place(x=350, y=180)

        if records == None:
            lblMessage['text'] = "Record not found"
        else:
            #frame for table
            tableframe = Frame(self.booking_frame)
            tableframe.place(x=70, y=20)

            #creating treeview table to show the customer information in tables to understand easily
            tblpersons = ttk.Treeview(tableframe)
            # Define Our Columns
            tblpersons['column'] = ('cid', 'bid', 'date', 'time', 'pickup', 'destination', 'status')

            # Format Our Columns
            tblpersons.column("#0", width=0, stretch=NO)
            tblpersons.column("cid", width=50, anchor=CENTER)
            tblpersons.column("bid", width=100, anchor=CENTER)
            tblpersons.column("date", width=100, anchor=CENTER)
            tblpersons.column("time", width=100, anchor=CENTER)
            tblpersons.column("pickup", width=100, anchor=CENTER)
            tblpersons.column("destination", width=100, anchor=CENTER)
            tblpersons.column("status", width=100, anchor=CENTER)

            # Create Headings
            tblpersons.heading("#0", text='', anchor=CENTER)
            tblpersons.heading("cid", text='CID', anchor=CENTER)
            tblpersons.heading("bid", text='BID', anchor=CENTER)
            tblpersons.heading("date", text='DATE', anchor=CENTER)
            tblpersons.heading("time", text='TIME', anchor=CENTER)
            tblpersons.heading("pickup", text='PICK UP', anchor=CENTER)
            tblpersons.heading("destination", text='DESTINATION', anchor=CENTER)
            tblpersons.heading("status", text='STATUS', anchor=CENTER)


            global count
            count = 0

            # for record in records:
            for record in records:
                if count % 2 == 0:
                    tblpersons.insert(parent='', index='end', iid=count, text='',
                                   values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6]),
                                   tags=('evenrow',))
                else:
                    tblpersons.insert(parent='', index='end', iid=count, text='',
                                   values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6]),
                                   tags=('oddrow',))
                # increment counter
                count += 1


            tblpersons.pack()

            def selection(bid):
                selected = tblpersons.focus()
                temp = tblpersons.item(selected, 'values')
                return temp[1]

            tblpersons.bind('<ButtonRelease-1>', selection)

            #show record in txt,label and remove it before displaying
            def select_record(e):
                global values
                # Clear entry boxes
                date_lbl1.config(text="")
                time_lbl1.config(text="")
                pick_up_lbl1.config(text="")
                destination_lbl1.config(text="")
                driver_txt.delete(0, 'end')

                # Grab record Number
                selected = tblpersons.focus()
                # Grab record values
                values = tblpersons.item(selected, 'values')

                # outpus to entry boxes
                date_lbl1.config(text=values[2])
                time_lbl1.config(text=values[3])
                pick_up_lbl1.config(text=values[4])
                destination_lbl1.config(text=values[5])

            tblpersons.bind('<ButtonRelease-1>', select_record)

            #function to update the record of driver for readjustment
            def update_driver():
                conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')

                sql = "UPDATE driver SET status=%s WHERE did=%s"
                update = "booked"
                values = (update, driver_txt.get())
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
                    del sql, values
                    return result

            #function to update the record of booked trip for readjustment
            def update_record():
                global bid
                # Grab the record number
                selected = tblpersons.focus()
                value = tblpersons.item(selected, 'values')
                cid = value[0]

                #get bid from selected table which is focus(while clicking)
                bd = []
                for b in selection(bid=selection):
                    bd.append(b[0])
                    lol_string = ''.join(map(str, bd))
                bid = lol_string

                # Recive value
                date = value[2]
                time = value[3]
                pick_up = value[4]
                destination = value[5]
                status = "active"

                # Update record in table
                tblpersons.item(selected, text="", values=(cid, bid,
                                                           date, time, pick_up,
                                                           destination,
                                                           status))

                # Update the database
                # Create a database or connect to one that exists
                conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')
                sql = "UPDATE booking SET did=%s, status='active' WHERE bid=%s"
                values = (driver_txt.get(), bid)
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
                    del sql, values
                    return result

                # Clear entry boxes
                date_txt.delete(0, END)
                hrs_txt.delete(0, END)
                min_txt.delete(0, END)
                pick_up_txt.delete(0, END)
                destination_txt.delete(0, END)

            #add label
            date_lbl = Label(self.booking_frame, text="Date")
            time_lbl = Label(self.booking_frame, text="Time")
            pick_up_lbl = Label(self.booking_frame, text="Pick Up")
            destination_lbl = Label(self.booking_frame, text="Destination")
            driver_lbl = Label(self.booking_frame, text="Driver")

            book_btn = Button(self.booking_frame, text="Book", command=lambda: [update_driver(), update_record()])

            date_lbl.place(x=70, y=300)
            time_lbl.place(x=70, y=335)
            pick_up_lbl.place(x=220, y=335)
            destination_lbl.place(x=220, y=300)
            driver_lbl.place(x=450, y=300)
            lblMessage.place(x=250, y=400)

            #add label to show the information while clicking on the date to assign driver
            date_lbl1 = Label(self.booking_frame, text="")
            time_lbl1 = Label(self.booking_frame, text="")
            pick_up_lbl1 = Label(self.booking_frame, text="")
            destination_lbl1 = Label(self.booking_frame, text="")

            #show available driver by checking their status for their next booking
            driver = drivergetAllavailable()
            drivers = []
            for i in driver:
                drivers.append(i[0])
            driver_txt = ttk.Combobox(self.booking_frame)
            driver_txt['values'] = (drivers)

            date_lbl1.place(x=140, y=300)
            time_lbl1.place(x=140, y=335)
            pick_up_lbl1.place(x=350, y=335)
            destination_lbl1.place(x=350, y=300)
            driver_txt.place(x=500, y=300)

            book_btn.place(x=315, y=380)


    def tripinfo(self):
        self.delete_frame()

        #search all the trip
        result = bookinggetAll()
        # Display Message
        lblMessage = Label(self.booking_frame, text='')
        lblMessage.place(x=350, y=180)

        if result == None:
            lblMessage['text'] = "Record not found"
        else:

            tableframe = Frame(self.booking_frame)
            tableframe.place(x=70, y=20)

            # creating treeview table to show the customer information in tables to understand easily
            tblpersons = ttk.Treeview(tableframe)

            # Define Our Columns
            tblpersons['column'] = ('cid', 'bid', 'date', 'time', 'pickup', 'destination', 'status')

            # Format Our Columns
            tblpersons.column("#0", width=0, stretch=NO)
            tblpersons.column("cid", width=50, anchor=CENTER)
            tblpersons.column("bid", width=100, anchor=CENTER)
            tblpersons.column("date", width=100, anchor=CENTER)
            tblpersons.column("time", width=100, anchor=CENTER)
            tblpersons.column("pickup", width=100, anchor=CENTER)
            tblpersons.column("destination", width=100, anchor=CENTER)
            tblpersons.column("status", width=100, anchor=CENTER)

            # Create Headings
            tblpersons.heading("#0", text='', anchor=CENTER)
            tblpersons.heading("cid", text='CID', anchor=CENTER)
            tblpersons.heading("bid", text='BID', anchor=CENTER)
            tblpersons.heading("date", text='DATE', anchor=CENTER)
            tblpersons.heading("time", text='TIME', anchor=CENTER)
            tblpersons.heading("pickup", text='PICK UP', anchor=CENTER)
            tblpersons.heading("destination", text='DESTINATION', anchor=CENTER)
            tblpersons.heading("status", text='STATUS', anchor=CENTER)

            #display result
            for dt in result:
                tblpersons.insert(parent='', index='end', values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]))

            tblpersons.pack()

            def select_record(e):
                global bid, did
                # global values
                # Clear entry boxes
                date_lbl1.config(text="")
                time_lbl1.config(text="")
                pick_up_lbl1.config(text="")
                destination_lbl1.config(text="")

                d_name_lbl1.config(text="")
                d_mobile_lbl1.config(text="")
                d_age_lbl1.config(text="")
                d_gender_lbl1.config(text="")
                d_num_plate_lbl1.config(text="")

                # Grab record Number
                selected = tblpersons.focus()
                # Grab record values
                values = tblpersons.item(selected, 'values')

                #get booking id of selected value
                bid = values[1]
                #search values in database regarding the booking id
                record = bookingsearch1(bid)

                #passing driver id retrived from database which was assigh to the customer by admin
                did = record

                #search driver detail in database using driver id
                # will display the driver information through reciving driver id from booking database
                # and passing it to the database table to get driver information
                record1 = driversearch1(did)
                d_values = record1

                #applying condition when cancel button will appear
                if values[6] == "active":
                    cancel_btn = Button(self.booking_frame, text="Cancel",
                                        command=lambda: [update_driver1(), cancel_booking()])
                    cancel_btn.place(x=300, y=420)

                if values[6] == "pending":
                    cancel_btn = Button(self.booking_frame, text="Cancel",
                                        command=lambda: [cancel_booking1()])
                    cancel_btn.place(x=300, y=420)

                # outpus to entry boxes
                date_lbl1.config(text=values[2])
                time_lbl1.config(text=values[3])
                pick_up_lbl1.config(text=values[4])
                destination_lbl1.config(text=values[5])

                d_name_lbl1.config(text=d_values[1])
                d_mobile_lbl1.config(text=d_values[3])
                d_age_lbl1.config(text=d_values[5])
                d_gender_lbl1.config(text=d_values[6])
                d_num_plate_lbl1.config(text=d_values[7])

            tblpersons.bind('<ButtonRelease-1>', select_record)

        #cancel the trip having status active
        def cancel_booking():
            bookingid = bid
            record = bookingcancel(bookingid)
            return record

        #cancel the trip having status pending
        def cancel_booking1():
            bookingid = bid
            record = bookingcancel1(bookingid)
            return record


        def update_driver1():
            #get driver id which is marked as global variable
            driverid = did

            #also update the driver status while the trip is cancel
            conn1 = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')
            sql = "UPDATE driver SET status='open' WHERE did=%s"
            values = (driverid)
            result = False
            try:
                # pass #input, process, output
                conn = conn1
                cursor = conn.cursor(buffered=True)
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
                del sql, values
                return result

        #trip heading
        active_lbl = Label(self.booking_frame, text="Trip", font=("San Francisco", 15))
        active_lbl.place(x=340, y=260)

        #add label for trip information
        date_lbl = Label(self.booking_frame, text="Date")
        time_lbl = Label(self.booking_frame, text="Time")
        pick_up_lbl = Label(self.booking_frame, text="Pick Up")
        destination_lbl = Label(self.booking_frame, text="Destination")
        driver_lbl = Label(self.booking_frame, text="Driver Information")

        #add label for driver information to show to the customer who is their driver and driver related information
        d_name_lbl = Label(self.booking_frame, text="Name")
        d_mobile_lbl = Label(self.booking_frame, text="Mobile")
        d_age_lbl = Label(self.booking_frame, text="Age")
        d_gender_lbl = Label(self.booking_frame, text="Gender")
        d_num_plate_lbl = Label(self.booking_frame, text="Number Plate")

        date_lbl.place(x=70, y=295)
        time_lbl.place(x=70, y=325)
        pick_up_lbl.place(x=70, y=355)
        destination_lbl.place(x=70, y=385)

        d_name_lbl.place(x=420, y=295)
        d_mobile_lbl.place(x=420, y=325)
        d_age_lbl.place(x=420, y=355)
        d_gender_lbl.place(x=420, y=385)
        d_num_plate_lbl.place(x=420, y=415)

        driver_lbl.place(x=430, y=260)
        lblMessage.place(x=250, y=400)

        # add label for trip information, put data from table
        date_lbl1 = Label(self.booking_frame, text="")
        time_lbl1 = Label(self.booking_frame, text="")
        pick_up_lbl1 = Label(self.booking_frame, text="")
        destination_lbl1 = Label(self.booking_frame, text="")

        # add label for driver information to show to the customer who is their driver and driver related information
        #will display the driver information through reciving driver id from booking database
        #and passing it to the database table to get driver information
        d_name_lbl1 = Label(self.booking_frame, text="")
        d_mobile_lbl1 = Label(self.booking_frame, text="")
        d_age_lbl1 = Label(self.booking_frame, text="")
        d_gender_lbl1 = Label(self.booking_frame, text="")
        d_num_plate_lbl1 = Label(self.booking_frame, text="")

        date_lbl1.place(x=140, y=295)
        time_lbl1.place(x=140, y=325)
        pick_up_lbl1.place(x=140, y=355)
        destination_lbl1.place(x=140, y=385)

        d_name_lbl1.place(x=520, y=295)
        d_mobile_lbl1.place(x=520, y=325)
        d_age_lbl1.place(x=520, y=355)
        d_gender_lbl1.place(x=520, y=385)
        d_num_plate_lbl1.place(x=520, y=415)

        pass


    def Add_account(self):

        self.delete_frame()

        # get values
        result = customergetAll()

        # Display Message
        lblMessage = Label(self.booking_frame, text='')
        lblMessage.place(x=350, y=180)

        if result == None:
            lblMessage['text'] = "Record not found"
        else:

            tableframe = Frame(self.booking_frame)

            tableframe.place(x=70, y=20)

            tblpersons = ttk.Treeview(tableframe)
            tblpersons['column'] = ('id','name', 'address', 'mobile', 'email', 'dob', 'gender', 'password')

            tblpersons.column("#0", width=0, stretch=NO)
            tblpersons.column("id", width=50, anchor=CENTER)
            tblpersons.column("name", width=50, anchor=CENTER)
            tblpersons.column("address", width=100, anchor=CENTER)
            tblpersons.column("mobile", width=100, anchor=CENTER)
            tblpersons.column("email", width=100, anchor=CENTER)
            tblpersons.column("dob", width=100, anchor=CENTER)
            tblpersons.column("gender", width=100, anchor=CENTER)
            tblpersons.column("password", width=100, anchor=CENTER)

            tblpersons.heading("#0", text='', anchor=CENTER)
            tblpersons.heading("id", text='ID', anchor=CENTER)
            tblpersons.heading("name", text='Name', anchor=CENTER)
            tblpersons.heading("address", text='Address', anchor=CENTER)
            tblpersons.heading("mobile", text='Mobile', anchor=CENTER)
            tblpersons.heading("email", text='Email', anchor=CENTER)
            tblpersons.heading("dob", text='DOB', anchor=CENTER)
            tblpersons.heading("gender", text='Gender', anchor=CENTER)
            tblpersons.heading("password", text='Password', anchor=CENTER)

            global count
            count = 0

            # for record in records:
            for record in result:
                if count % 2 == 0:
                    tblpersons.insert(parent='', index='end', iid=count, text='',
                                      values=(record[0],
                                      record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                                      tags=('evenrow',))
                else:
                    tblpersons.insert(parent='', index='end', iid=count, text='',
                                      values=(record[0],
                                      record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                                      tags=('oddrow',))
                # increment counter
                count += 1


            tblpersons.pack()

            def selection(bid):
                selected = tblpersons.focus()
                temp = tblpersons.item(selected, 'values')
                return temp[1]

            tblpersons.bind('<ButtonRelease-1>', selection)

            def select_record(e):
                # Clear entry boxes
                nametxt.delete(0, END)
                addresstxt.delete(0, END)
                mobiletxt.delete(0, END)
                emailtxt.delete(0, END)
                date_txt.delete(0, END)
                gendertxt.delete(0, END)
                passwordtxt.delete(0, END)

                # Grab record Number
                selected = tblpersons.focus()
                # Grab record values
                values = tblpersons.item(selected, 'values')

                # outpus to entry boxes
                nametxt.insert(0, values[1])
                addresstxt.insert(0, values[2])
                mobiletxt.insert(0, values[3])
                emailtxt.insert(0, values[4])
                date_txt.insert(0, values[5])
                gendertxt.insert(0, values[6])
                passwordtxt.insert(0, values[7])

            tblpersons.bind('<ButtonRelease-1>', select_record)

            def selection(bid):
                selected = tblpersons.focus()
                temp = tblpersons.item(selected, 'values')
                return temp[1]

            def deletecustomer():
                # get value while click in the table data
                selected = tblpersons.focus()
                temp = tblpersons.item(selected, 'values')

                # getting specific data from table
                cid = temp[0]

                # Send values to search (Middleware)
                result = customerdelete(cid)
                # Display Message

                if result == True:
                    lblMessage['text'] = "Record Delete"
                else:
                    lblMessage['text'] = "Unsuccessfull"

                pass

            def saveUser():
                #get value while click in the table data
                selected = tblpersons.focus()
                temp = tblpersons.item(selected, 'values')

                #getting specific data from table
                Cid = temp[0]

                #update table
                tblpersons.item(selected, text="", values=(Cid,
                    nametxt.get(), addresstxt.get(), mobiletxt.get(), emailtxt.get(), date_txt.get(), gendertxt.get(),
                    passwordtxt.get()))

                # Update the database
                # Create a database or connect to one that exists
                conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')
                # Send values to save (Middleware)
                sql = "UPDATE customer set name=%s, address=%s, mobile=%s, email=%s, dob=%s, gender=%s, password=%s WHERE cid=%s"
                values = (nametxt.get(), addresstxt.get(), mobiletxt.get(), emailtxt.get(), date_txt.get(), gendertxt.get(), passwordtxt.get(), Cid)
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

            def adduser():
                c1 = register("", nametxt.get(), addresstxt.get(), mobiletxt.get(), emailtxt.get(), date_txt.get(), gendertxt.get(), passwordtxt.get())

                # Send values to save (database)
                result = customerinsert(c1)
                # Display Message
                if result['status'] == True:
                    # self.lblMessage['text']="Save Record"
                    messagebox.showinfo("Done", "Account created, Now you can log in using mobile number as password")

            #call above function while clicking
            delete_btn = Button(self.booking_frame, text="Delete", command=deletecustomer)
            update_btn = Button(self.booking_frame, text="Update", command=saveUser)
            add_btn = Button(self.booking_frame, text="Add", command=adduser)

            delete_btn.place(x=315, y=400)
            update_btn.place(x=260, y=400)
            add_btn.place(x=370, y=400)


            #add label
            namelbl = Label(self.booking_frame, text="Name")
            addresslbl = Label(self.booking_frame, text="Address")
            mobilelbl = Label(self.booking_frame, text="Mobile")
            emaillbl = Label(self.booking_frame, text="Email")
            doblbl = Label(self.booking_frame, text="DOB")
            genderlbl = Label(self.booking_frame, text="Gender")
            passwordlbl = Label(self.booking_frame, text="Password")

            # lblMessage = Label(self.booking_frame, text='', bg="gray")

            #add text box
            nametxt = Entry(self.booking_frame)
            addresstxt = Entry(self.booking_frame)
            mobiletxt = Entry(self.booking_frame)
            emailtxt = Entry(self.booking_frame)
            date_txt = DateEntry(self.booking_frame, width=12, background='darkblue',
                                 foreground='white', borderwidth=2)

            date_txt.bind("<<DateEntrySelected>>")
            gendertxt = Entry(self.booking_frame)
            passwordtxt = Entry(self.booking_frame)


            namelbl.place(x=40, y=270)
            addresslbl.place(x=40, y=300)
            mobilelbl.place(x=250, y=270)
            emaillbl.place(x=250, y=300)
            doblbl.place(x=460, y=270)
            genderlbl.place(x=460, y=300)
            passwordlbl.place(x=40, y=330)

            lblMessage.place(x=360, y=400)

            nametxt.place(x=100, y=270)
            addresstxt.place(x=100, y=300)
            mobiletxt.place(x=310, y=270)
            emailtxt.place(x=310, y=300)
            date_txt.place(x=520, y=270)
            gendertxt.place(x=520, y=300)
            passwordtxt.place(x=100, y=330)

            pass

    def Add_Driver(self):
        self.delete_frame()

        # Read values from database
        result = drivergetAll()

        # Display Message
        lblMessage = Label(self.booking_frame, text='')
        lblMessage.place(x=350, y=180)

        if result == None:
            lblMessage['text'] = "Record not found"
        else:

            tableframe = Frame(self.booking_frame)

            tableframe.place(x=25, y=20)

            tblpersons = ttk.Treeview(tableframe)
            tblpersons['column'] = ('id','name', 'address', 'mobile', 'email', 'dob', 'gender', 'numberplate', 'password')

            tblpersons.column("#0", width=0, stretch=NO)
            tblpersons.column("id", width=50, anchor=CENTER)
            tblpersons.column("name", width=50, anchor=CENTER)
            tblpersons.column("address", width=100, anchor=CENTER)
            tblpersons.column("mobile", width=100, anchor=CENTER)
            tblpersons.column("email", width=100, anchor=CENTER)
            tblpersons.column("dob", width=100, anchor=CENTER)
            tblpersons.column("gender", width=100, anchor=CENTER)
            tblpersons.column("numberplate", width=100, anchor=CENTER)
            tblpersons.column("password", width=100, anchor=CENTER)

            tblpersons.heading("#0", text='', anchor=CENTER)
            tblpersons.heading("id", text='ID', anchor=CENTER)
            tblpersons.heading("name", text='Name', anchor=CENTER)
            tblpersons.heading("address", text='Address', anchor=CENTER)
            tblpersons.heading("mobile", text='Mobile', anchor=CENTER)
            tblpersons.heading("email", text='Email', anchor=CENTER)
            tblpersons.heading("dob", text='DOB', anchor=CENTER)
            tblpersons.heading("gender", text='Gender', anchor=CENTER)
            tblpersons.heading("numberplate", text='Num Plate', anchor=CENTER)
            tblpersons.heading("password", text='Password', anchor=CENTER)

            global count
            count = 0

            # for record in records:
            for record in result:
                if count % 2 == 0:
                    tblpersons.insert(parent='', index='end', iid=count, text='',
                                      values=(record[0],
                                      record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                                      tags=('evenrow',))
                else:
                    tblpersons.insert(parent='', index='end', iid=count, text='',
                                      values=(record[0],
                                      record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                                      tags=('oddrow',))
                # increment counter
                count += 1


            tblpersons.pack()

            def selection(bid):
                selected = tblpersons.focus()
                temp = tblpersons.item(selected, 'values')
                return temp[1]

            tblpersons.bind('<ButtonRelease-1>', selection)

            def select_record(e):
                # Clear entry boxes
                nametxt.delete(0, END)
                addresstxt.delete(0, END)
                mobiletxt.delete(0, END)
                emailtxt.delete(0, END)
                age_txt.delete(0, END)
                gendertxt.delete(0, END)
                numplatetxt.delete(0, END)
                passwordtxt.delete(0, END)

                # Grab record Number
                selected = tblpersons.focus()
                # Grab record values
                values = tblpersons.item(selected, 'values')

                # outpus to entry boxes
                nametxt.insert(0, values[1])
                addresstxt.insert(0, values[2])
                mobiletxt.insert(0, values[3])
                emailtxt.insert(0, values[4])
                age_txt.insert(0, values[5])
                gendertxt.insert(0, values[6])
                numplatetxt.insert(0, values[7])
                passwordtxt.insert(0, values[8])

            tblpersons.bind('<ButtonRelease-1>', select_record)

            def selection(bid):

                selected = tblpersons.focus()
                temp = tblpersons.item(selected, 'values')
                return temp[1]

            def deletedriver():
                # get value while click in the table data
                selected = tblpersons.focus()
                temp = tblpersons.item(selected, 'values')

                # getting specific data from table
                did = temp[0]

                # Send values to search (Middleware)
                result = deleteDriver(did)
                # Display Message

                if result == True:
                    lblMessage['text'] = "Record Delete"
                else:
                    lblMessage['text'] = "Unsuccessfull"

                pass

            def saveDriver():

                # Read values from table
                selected = tblpersons.focus()
                temp = tblpersons.item(selected, 'values')

                # getting specific data from table
                did = temp[0]

                #update table
                tblpersons.item(selected, text="", values=(did,
                    nametxt.get(), addresstxt.get(), mobiletxt.get(), emailtxt.get(), age_txt.get(), gendertxt.get(),
                    passwordtxt.get()))

                # Update the database
                # Create a database or connect to one that exists
                conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')
                # Send values to save (Middleware)
                sql = "UPDATE driver set name=%s, address=%s, mobile=%s, email=%s, age=%s, gender=%s, password=%s WHERE did=%s"
                values = (
                nametxt.get(), addresstxt.get(), mobiletxt.get(), emailtxt.get(), age_txt.get(), gendertxt.get(),
                passwordtxt.get(), did)
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

            def addDriver():
                c1 = driverregister("", nametxt.get(), addresstxt.get(), mobiletxt.get(), emailtxt.get(), age_txt.get(), gendertxt.get(), numplatetxt.get(), passwordtxt.get())

                # Send values to save (database)
                result = driverinsert(c1)
                # Display Message
                if result['status'] == True:
                    # self.lblMessage['text']="Save Record"
                    messagebox.showinfo("Done", "Account created, Now you can log in using mobile number as password")

            delete_btn = Button(self.booking_frame, text="Delete", command=deletedriver)
            update_btn = Button(self.booking_frame, text="Update", command=saveDriver)
            add_btn = Button(self.booking_frame, text="Add", command=addDriver)


            delete_btn.place(x=315, y=400)
            update_btn.place(x=260, y=400)
            add_btn.place(x=370, y=400)


            #add label
            namelbl = Label(self.booking_frame, text="Name")
            addresslbl = Label(self.booking_frame, text="Address")
            mobilelbl = Label(self.booking_frame, text="Mobile")
            emaillbl = Label(self.booking_frame, text="Email")
            doblbl = Label(self.booking_frame, text="DOB")
            genderlbl = Label(self.booking_frame, text="Gender")
            numplatelbl = Label(self.booking_frame, text="Num Plate")
            passwordlbl = Label(self.booking_frame, text="Password")

            lblMessage = Label(self.booking_frame, text='', bg="gray")

            #add text box
            nametxt = Entry(self.booking_frame)
            addresstxt = Entry(self.booking_frame)
            mobiletxt = Entry(self.booking_frame)
            emailtxt = Entry(self.booking_frame)
            age_txt = Entry(self.booking_frame)
            gendertxt = Entry(self.booking_frame)
            numplatetxt = Entry(self.booking_frame)
            passwordtxt = Entry(self.booking_frame)


            namelbl.place(x=40, y=270)
            addresslbl.place(x=40, y=300)
            mobilelbl.place(x=250, y=270)
            emaillbl.place(x=250, y=300)
            doblbl.place(x=460, y=270)
            genderlbl.place(x=460, y=300)
            numplatelbl.place(x=250, y=330)
            passwordlbl.place(x=40, y=330)

            lblMessage.place(x=360, y=400)

            nametxt.place(x=100, y=270)
            addresstxt.place(x=100, y=300)
            mobiletxt.place(x=315, y=270)
            emailtxt.place(x=315, y=300)
            age_txt.place(x=520, y=270)
            gendertxt.place(x=520, y=300)
            numplatetxt.place(x=315, y=330)
            passwordtxt.place(x=100, y=330)

            pass
