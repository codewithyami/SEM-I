from Assignment.Classes.Booking.booking_classes import booking
from tkinter import *
import messagebox
from Assignment.Manager.booking.booking_database import *
from Assignment.Manager.customer.database import *
from Assignment.Manager.driver.driver_database import *
from tkinter import ttk
from tkcalendar import DateEntry


# create a class for customer dashboard
# every frame will work inside this class where tkinter is pass while calling the class CUSTOMER
class CUSTOMER():
    def __init__(self, master, cid):
        super().__init__()
        # passing the master to create a framework
        self.Window_main = master
        #passing the cid receive during login of the customer
        self.cid = cid

        screen_width = self.Window_main.winfo_screenwidth()
        screen_height = self.Window_main.winfo_screenheight()

        #creating seperate frames for an individual widgit purpose
        self.side_frame = Frame(self.Window_main, bg="#A7DBD8", height=screen_height, width=screen_width)
        self.side_frame.pack(side=LEFT, fill=BOTH)
        self.side_frame.pack_propagate(False)

        self.main_frame = Frame(self.side_frame, bg="#F38630", height=510, width=990)
        self.main_frame.pack(side=RIGHT, fill=BOTH, anchor=SE)

        self.booking_frame = Frame(self.main_frame, bg="#E0E4CC", height=450, width=700)
        self.booking_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

        #main buttons which will help to call the function as per needed
        dashboard_btn = Button(self.side_frame, text="Dashboard", font=("San Francisco", 20))
        booking_btn = Button(self.side_frame, text="Booking", command=self.Booking_btn)
        tripinfo_btn = Button(self.side_frame, text="Trip Information", command=self.tripinfo)
        delete_profile_btn = Button(self.side_frame, text="Profile", command=self.Account)
        payment_btn = Button(self.side_frame, text="Payment", command=self.payment)
        logout_btn = Button(self.side_frame, text="Logout", command=self.btn_clicked)

        dashboard_btn.place(x=2, y=50)
        booking_btn.place(x=13, y=200)
        tripinfo_btn.place(x=13, y=250)
        delete_profile_btn.place(x=13, y=300)
        payment_btn.place(x=13, y=350)
        logout_btn.place(x=13, y=400)

    def payment(self):
        self.delete_frame()
        payment_lbl = Label(self.booking_frame, text="Payment",font=("San Francisco", 20))
        d_num_lbl = Label(self.booking_frame, text="Driver number")
        p_option_lbl = Label(self.booking_frame, text="Payment Options")
        total_lbl = Label(self.booking_frame, text="Total")
        pay_lbl = Label(self.booking_frame, text="Amount")

        p_option_txt = ttk.Combobox(self.booking_frame)
        p_option_txt['values'] = ['Esawa','Kalthi']
        total_txt = Entry(self.booking_frame)
        d_num_txt = Entry(self.booking_frame)
        pay_txt = Entry(self.booking_frame)

        payment_lbl.place(x=70, y=100)
        d_num_lbl.place(x=70, y=150)
        p_option_lbl.place(x=70, y=200)
        total_lbl.place(x=70, y=250)
        pay_lbl.place(x=70, y=300)

        # payment_txt.place(x=140, y=300)
        d_num_txt.place(x=160, y=150)
        p_option_txt.place(x=160, y=200)
        total_txt.place(x=160, y=250)
        pay_txt.place(x=160, y=300)

        pay_btn = Button(self.booking_frame, text="Pay", command='')
        pay_btn.place(x=270, y=380)


#function to redirect in login page
    def btn_clicked(self):
        messagebox.askyesno("Confirm","Do you really want to logout")
        while True:
            self.login()

    def login(self):
        self.Window_main.destroy()
        from Assignment.UI import UI
        return UI
        pass

#function to delete the widgit while switching between different function operation
    def delete_frame(self):
        for frame in self.booking_frame.winfo_children():
            frame.destroy()


#booking button to make a trip order
    def Booking_btn(self):
        #removing widgit
        self.delete_frame()

        cid = self.cid
        #searching the pending date from the database for the further new request of trips
        conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')
        cursor = conn.cursor()
        sql = "SELECT * FROM booking WHERE cid=%s AND status=%s"
        CID = cid
        status = "pending"
        values = (CID, status)
        cursor.execute(sql, values)
        records = cursor.fetchall()


        lblMessage = Label(self.booking_frame, text='')
        lblMessage.place(x=350, y=180)

        if records==None:
            lblMessage['text'] = "Record not found"


        else:
            #frame for table
            tableframe = Frame(self.booking_frame)
            tableframe.place(x=25, y=20)

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
            #display record
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
                # Clear entry boxes
                date_txt.delete(0, END)
                hrs_txt.delete(0, END)
                min_txt.delete(0, END)
                pick_up_txt.delete(0, END)
                destination_txt.delete(0, END)

                # Grab record Number
                selected = tblpersons.focus()
                # Grab record values
                values = tblpersons.item(selected, 'values')

                # outpus to entry boxes
                date_txt.insert(0, values[2])
                time = []
                for t in values[3]:
                    time.append(t[0])

                hrs_txt.delete(0, len(hrs_txt.get()))
                hrs_txt.insert(0, time[1])
                hrs_txt.insert(0, time[0])
                min_txt.delete(0, len(min_txt.get()))
                min_txt.insert(0, time[6])
                min_txt.insert(0, time[3])

                pick_up_txt.insert(0, values[4])
                destination_txt.insert(0, values[5])

            tblpersons.bind('<ButtonRelease-1>', select_record)

            def savebooking():
                # Read values from Window
                Cid = self.cid
                date = date_txt.get_date()  # Read value from TextBox
                time = (hrs_txt.get() + min_txt.get() + "00")
                pick_up = (pick_up_txt.get())
                destination = (destination_txt.get())
                status = "pending"

                #validation during booking
                def validate_time(time):
                    if len(time)==None:
                        # Display an error message in a message box
                        messagebox.showerror("Error", "Please enter time")
                        return False
                    return True

                def validate_pick_up(pick_up):
                    if len(pick_up) == 0:
                        # Display an error message in a message box
                        messagebox.showerror("Error", "Please enter pick up address")
                        return False
                    return True

                def validate_destination(destintaion):
                    if len(destination) == 0:
                        # Display an error message in a message box
                        messagebox.showerror("Error", "Please enter destination address")
                        return False
                    return True

                TIME = validate_time(time)
                PICK_UP = validate_pick_up(pick_up)
                DESTINATION = validate_destination(destination)

                if DESTINATION==True:
                    # Send values to search (Middleware)
                    c1 = booking(Cid, date, time, pick_up, destination, status)

                    # Send values to save (Middleware)
                    result = bookinginsert(c1)
                    # Display Message

                    if result['status'] == True:
                        messagebox.showinfo("Done", "Booked")
                        lblMessage['text'] = "Save Record"
                    else:
                        lblMessage['text'] = "Error to save"


            #function to update the record of booked trip for readjustment
            def update_record():
                # Grab the record number
                selected = tblpersons.focus()
                time = (hrs_txt.get() + min_txt.get() + "00")
                cid = self.cid
                bd = []
                status = "pending"
                for b in selection(bid=selection):
                    bd.append(b[0])
                    lol_string = ''.join(map(str, bd))
                bid = lol_string

                # Update record
                tblpersons.item(selected, text="", values=(cid, bid,
                                                           date_txt.get(), time, pick_up_txt.get(),
                                                           destination_txt.get(),
                                                           status))

                # Update the database
                # Create a database or connect to one that exists
                conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')

                sql = "UPDATE booking SET date=%s, time=%s, pick_up=%s, destination=%sWHERE bid=%s"
                values = (date_txt.get(), time, pick_up_txt.get(),
                          destination_txt.get(), bid)
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

            # Add label
            date_lbl = Label(self.booking_frame, text="Date")
            time_lbl = Label(self.booking_frame, text="Time")
            hrs_lbl = Label(self.booking_frame, text="Hrs")
            min_lbl = Label(self.booking_frame, text="Min")
            pick_up_lbl = Label(self.booking_frame, text="Pick Up")
            destination_lbl = Label(self.booking_frame, text="Destination")

            # Add Record Entry Boxes
            #import clander from libery to make date selection
            date_txt = DateEntry(self.booking_frame, width=12, background='darkblue',
                                 foreground='white', borderwidth=2)
            date_txt.place(x=140, y=300)
            date_txt.bind("<<DateEntrySelected>>")

            hrs_txt = Entry(self.booking_frame, width=4)
            min_txt = Entry(self.booking_frame, width=5)
            pick_up_txt = Entry(self.booking_frame)
            destination_txt = Entry(self.booking_frame)

            #button to update and for new trip to book
            update_btn = Button(self.booking_frame, text="Update", command=lambda: [update_record()])
            book_btn = Button(self.booking_frame, text="Book", command=savebooking)

            date_lbl.place(x=70, y=300)
            time_lbl.place(x=70, y=335)
            hrs_lbl.place(x=170, y=335)
            min_lbl.place(x=235, y=335)
            pick_up_lbl.place(x=350, y=335)
            destination_lbl.place(x=350, y=300)

            hrs_txt.place(x=140, y=335)
            min_txt.place(x=200, y=335)
            pick_up_txt.place(x=450, y=335)
            destination_txt.place(x=450, y=300)

            update_btn.place(x=315, y=380)
            book_btn.place(x=270, y=380)

    #this function will provide the overall trip information of the customer
    def tripinfo(self):
        self.delete_frame()

        # Read values
        cid = [self.cid]
        result = bookinggetAll1(cid)

        # Display Message
        lblMessage = Label(self.booking_frame, text='')
        lblMessage.place(x=350, y=180)

        if result == None:
            lblMessage['text'] = "Record not found"
        else:

            tableframe = Frame(self.booking_frame)
            tableframe.place(x=25, y=20)

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

            #show record in txt,label and remove it before displaying
            def select_record(e):
                global bid, did
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

    # show only personal infornation
    def Account(self):
        self.delete_frame()
        # Read values
        CID = [self.cid]
        print(CID)
        #search customer personal information only
        result = customersearch1(CID)

        # Display Message
        lblMessage = Label(self.booking_frame, text='')
        lblMessage.place(x=350, y=180)

        if result == None:
            lblMessage['text'] = "Record not found"
        else:

            tableframe = Frame(self.booking_frame)
            tableframe.place(x=25, y=20)

            tblpersons = ttk.Treeview(tableframe)
            tblpersons['column'] = ('name', 'address', 'mobile', 'email', 'dob', 'gender', 'password')

            tblpersons.column("#0", width=0, stretch=NO)
            tblpersons.column("name", width=50, anchor=CENTER)
            tblpersons.column("address", width=100, anchor=CENTER)
            tblpersons.column("mobile", width=100, anchor=CENTER)
            tblpersons.column("email", width=100, anchor=CENTER)
            tblpersons.column("dob", width=100, anchor=CENTER)
            tblpersons.column("gender", width=100, anchor=CENTER)
            tblpersons.column("password", width=100, anchor=CENTER)

            tblpersons.heading("#0", text='', anchor=CENTER)
            tblpersons.heading("name", text='Name', anchor=CENTER)
            tblpersons.heading("address", text='Address', anchor=CENTER)
            tblpersons.heading("mobile", text='Mobile', anchor=CENTER)
            tblpersons.heading("email", text='Email', anchor=CENTER)
            tblpersons.heading("dob", text='DOB', anchor=CENTER)
            tblpersons.heading("gender", text='Gender', anchor=CENTER)
            tblpersons.heading("password", text='Password', anchor=CENTER)


            tblpersons.insert(parent='', index='end',
                              values=(result[1], result[2], result[3], result[4], result[5], result[6], result[7]))

            tblpersons.pack()

            def selection(cid):
                selected = tblpersons.focus()
                temp = tblpersons.item(selected, 'values')
                return temp[0]

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
                nametxt.insert(0, values[0])
                addresstxt.insert(0, values[1])
                mobiletxt.insert(0, values[2])
                emailtxt.insert(0, values[3])
                date_txt.insert(0, values[4])
                gendertxt.insert(0, values[5])
                passwordtxt.insert(0, values[6])

            tblpersons.bind('<ButtonRelease-1>', select_record)


            def deleteAccount():
                # cd = []
                # for c in selection(cid=selection):
                #     cd.append(c[0])
                #     lol_string = ''.join(map(str, cd))
                # cid = lol_string  # Read value from TextBox

                # selected = tblpersons.focus()
                # temp = tblpersons.item(selected, 'values')
                Cid = self.cid


                # Send values to search (Middleware)
                result = customerdelete(Cid)
                # Display Message

                if result == True:
                    # lblMessage['text'] = "Record Delete"
                    messagebox.showinfo("Done", "Delete")

                else:
                    # lblMessage['text'] = "Unsuccessfull"
                    messagebox.showerror("Error", "Unsuccessfull")


                pass

            #update customer data as per input
            def saveUser():
                result = customersearch1(CID)
                # Read values from table
                selected = tblpersons.focus()
                cid = result[0]

                #update table
                tblpersons.item(selected, text="", values=(
                    nametxt.get(), addresstxt.get(), mobiletxt.get(), emailtxt.get(), date_txt.get(), gendertxt.get(),
                    passwordtxt.get()))

                #display message
                if result == True:
                    messagebox.showerror("Error", "update unsuccessfull")
                else:
                    messagebox.showinfo("Done", "Update successfully")

                # Update the database
                # Create a database or connect to one that exists
                conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')
                # Send values to save (Middleware)
                sql = "UPDATE customer set name=%s, address=%s, mobile=%s, email=%s, dob=%s, gender=%s, password=%s WHERE cid=%s"
                values = (
                nametxt.get(), addresstxt.get(), mobiletxt.get(), emailtxt.get(), date_txt.get(), gendertxt.get(),
                passwordtxt.get(), cid)
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




            delete_btn = Button(self.booking_frame, text="Delete", command=lambda :[deleteAccount(), self.btn_clicked()])
            update_btn = Button(self.booking_frame, text="Update", command=saveUser)

            delete_btn.place(x=315, y=400)
            update_btn.place(x=260, y=400)

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
