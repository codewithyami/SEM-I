
from tkinter import *
from Assignment.Manager.booking.booking_database import *
from Assignment.Manager.customer.database import *
from Assignment.Manager.driver.driver_database import *
from tkinter import ttk



# create a class for driver dashboard
# every frame will work inside this class where tkinter is pass while calling the class DRIVER_DASHBOARD
class DRIVER_DASHBOARD():
    def __init__(self, master, did):
        super().__init__()

        # passing the master to create a framework
        self.Window_main = master

        #passing the cid receive during login of the driver
        self.did = did

        screen_width = self.Window_main.winfo_screenwidth()
        screen_height = self.Window_main.winfo_screenheight()

        # creating seperate frames for an individual widgit purpose
        self.side_frame = Frame(self.Window_main, bg="#A7DBD8", height=screen_height, width=screen_width)
        self.side_frame.pack(side=LEFT, fill=BOTH)
        self.side_frame.pack_propagate(False)

        self.main_frame = Frame(self.side_frame, bg="#F38630", height=510, width=990)
        self.main_frame.pack(side=RIGHT, fill=BOTH, anchor=SE)

        self.booking_frame = Frame(self.main_frame, bg="#E0E4CC", height=450, width=800)
        self.booking_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

        #main buttons which will help to call the function as per needed
        dashboard_btn = Button(self.side_frame, text="Dashboard", font=("San Francisco", 20))
        booking_btn = Button(self.side_frame, text="Customer", command=self.View_Booking_btn)
        tripinfo_btn = Button(self.side_frame, text="Trip Information", command=self.tripinfo)
        delete_profile_btn = Button(self.side_frame, text="Profile", command=self.Account)
        logout_btn = Button(self.side_frame, text="Logout", command=self.btn_clicked)

        dashboard_btn.place(x=2, y=50)
        booking_btn.place(x=13, y=200)
        tripinfo_btn.place(x=13, y=250)
        delete_profile_btn.place(x=13, y=300)
        logout_btn.place(x=13, y=350)

    # function to redirect in login page
    def btn_clicked(self):
        while True:
            self.login()

    def login(self):
        self.Window_main.destroy()
        from Assignment.UI import UI
        return UI
        pass

    # function to delete the widgit while switching between different function operation
    def delete_frame(self):
        for frame in self.booking_frame.winfo_children():
            frame.destroy()

    # viewbooking button to see a next trip
    def View_Booking_btn(self):
        self.delete_frame()

        # Send values to search (Middleware)
        did = self.did

        #searching the active data from the database
        conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')
        cursor = conn.cursor()
        sql = "SELECT * FROM booking WHERE did=%s AND status=%s"
        DID = did
        status = "active"
        values = (DID, status)
        cursor.execute(sql, values)
        records = cursor.fetchall()

        #searching the ongoingg data from the database
        conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')
        cursor = conn.cursor()
        sql = "SELECT * FROM booking WHERE did=%s AND status=%s"
        DID = did
        status = "ongoing"
        values = (DID, status)
        cursor.execute(sql, values)
        records1 = cursor.fetchall()


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
            #to display active record at a single time
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

            #to display ongoing display at a single time
            for record in records1:
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
                # global values
                global bid, did
                # Clear entry boxes
                date_lbl1.config(text="")
                time_lbl1.config(text="")
                pick_up_lbl1.config(text="")
                destination_lbl1.config(text="")


                d_name_lbl1.config(text="")
                d_mobile_lbl1.config(text="")
                d_gender_lbl1.config(text="")

                # Grab record Number
                selected = tblpersons.focus()
                # Grab record values
                values = tblpersons.item(selected, 'values')

                #get booking id of selected value
                bid = values[0]
                BID = [bid]

                #search values in database regarding the booking id
                record1 = customersearch1(BID)

                #passing driver id retrived from database which was assigh to the customer by admin
                d_values = record1

                # outpus to entry boxes
                date_lbl1.config(text=values[2])
                time_lbl1.config(text=values[3])
                pick_up_lbl1.config(text=values[4])
                destination_lbl1.config(text=values[5])

                d_name_lbl1.config(text=d_values[1])
                d_mobile_lbl1.config(text=d_values[3])
                d_gender_lbl1.config(text=d_values[6])


            tblpersons.bind('<ButtonRelease-1>', select_record)


            def startbooking():
                # Grab the record number
                selected = tblpersons.focus()

                cid = self.did
                bd = []
                status = "ongoing"
                for b in selection(bid=selection):
                    bd.append(b[0])
                    lol_string = ''.join(map(str, bd))
                bid = lol_string  # Read value from TextBox

                # Update record
                # tblpersons.item(selected, text="", values=(cid, bid,
                #                                            date_txt.get(), time, pick_up_txt.get(),
                #                                            destination_txt.get(),
                #                                            status))

                # Update the database
                # Create a database or connect to one that exists
                conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')

                sql = "UPDATE booking SET status=%s WHERE bid=%s"
                values = (status, bid)
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

            def completebooking():
                # Grab the record number
                selected = tblpersons.focus()

                cid = self.did
                bd = []
                status = "Complete"
                for b in selection(bid=selection):
                    bd.append(b[0])
                    lol_string = ''.join(map(str, bd))
                bid = lol_string  # Read value from TextBox
                print(bid)
                # Update record
                # tblpersons.item(selected, text="", values=(cid, bid,
                #                                            date_txt.get(), time, pick_up_txt.get(),
                #                                            destination_txt.get(),
                #                                            status))

                # Update the database
                # Create a database or connect to one that exists
                conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='',
                                               database='tbs')

                sql = "UPDATE booking SET status=%s WHERE bid=%s"
                # sql = "UPDATE`booking` SET `cid` = '%s', `date` = '%s', `time` = '%s', `pick_up` = '%s', `destination` = '%s', `status` = '%s' WHERE bid = '%s'"
                values = (status, bid)
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

            # trip heading
            active_lbl = Label(self.booking_frame, text="Trip", font=("San Francisco", 15))
            active_lbl.place(x=340, y=260)

            #add label for trip information
            date_lbl = Label(self.booking_frame, text="Date")
            time_lbl = Label(self.booking_frame, text="Time")
            pick_up_lbl = Label(self.booking_frame, text="Pick Up")
            destination_lbl = Label(self.booking_frame, text="Destination")
            driver_lbl = Label(self.booking_frame, text="Driver Information")

            #add label for customer information
            d_name_lbl = Label(self.booking_frame, text="Name")
            d_mobile_lbl = Label(self.booking_frame, text="Mobile")
            d_gender_lbl = Label(self.booking_frame, text="Gender")

            lblMessage = Label(self.booking_frame, text='', bg="gray")

            date_lbl.place(x=70, y=295)
            time_lbl.place(x=70, y=325)
            pick_up_lbl.place(x=70, y=355)
            destination_lbl.place(x=70, y=385)

            d_name_lbl.place(x=420, y=295)
            d_mobile_lbl.place(x=420, y=325)
            d_gender_lbl.place(x=420, y=355)

            driver_lbl.place(x=430, y=260)
            lblMessage.place(x=250, y=400)

            # add label for trip information, put data from table
            date_lbl1 = Label(self.booking_frame, text="")
            time_lbl1 = Label(self.booking_frame, text="")
            pick_up_lbl1 = Label(self.booking_frame, text="")
            destination_lbl1 = Label(self.booking_frame, text="")

            # add label for customer information to show to the driver who is their customer and customer related information
            # will display the customer information through reciving customer id from booking database
            # and passing it to the database table to get customer information
            d_name_lbl1 = Label(self.booking_frame, text="")
            d_mobile_lbl1 = Label(self.booking_frame, text="")
            d_gender_lbl1 = Label(self.booking_frame, text="")

            date_lbl1.place(x=140, y=295)
            time_lbl1.place(x=140, y=325)
            pick_up_lbl1.place(x=140, y=355)
            destination_lbl1.place(x=140, y=385)

            d_name_lbl1.place(x=520, y=295)
            d_mobile_lbl1.place(x=520, y=325)
            d_gender_lbl1.place(x=520, y=355)

            start_btn = Button(self.booking_frame, text="Start",
                                command=lambda: [startbooking()])
            start_btn.place(x=300, y=420)
            complete_btn = Button(self.booking_frame, text="Complete",
                                command=lambda: [completebooking()])
            complete_btn.place(x=360, y=420)



    def tripinfo(self):
        self.delete_frame()
        did = [self.did]
        # Read values from Window

        # Send values to search (database)
        result = bookinggetAll2(did)

        # Display Message
        lblMessage = Label(self.booking_frame, text='')
        lblMessage.place(x=350, y=180)

        if result == None:
            lblMessage['text'] = "Record not found"
        else:

            tableframe = Frame(self.booking_frame)

            tableframe.place(x=70, y=20)

            tblpersons = ttk.Treeview(tableframe)
            tblpersons['column'] = ('cid', 'bid', 'date', 'time', 'pickup', 'destination', 'status')

            tblpersons.column("#0", width=0, stretch=NO)
            tblpersons.column("cid", width=50, anchor=CENTER)
            tblpersons.column("bid", width=100, anchor=CENTER)
            tblpersons.column("date", width=100, anchor=CENTER)
            tblpersons.column("time", width=100, anchor=CENTER)
            tblpersons.column("pickup", width=100, anchor=CENTER)
            tblpersons.column("destination", width=100, anchor=CENTER)
            tblpersons.column("status", width=100, anchor=CENTER)

            tblpersons.heading("#0", text='', anchor=CENTER)
            tblpersons.heading("cid", text='CID', anchor=CENTER)
            tblpersons.heading("bid", text='BID', anchor=CENTER)
            tblpersons.heading("date", text='DATE', anchor=CENTER)
            tblpersons.heading("time", text='TIME', anchor=CENTER)
            tblpersons.heading("pickup", text='PICK UP', anchor=CENTER)
            tblpersons.heading("destination", text='DESTINATION', anchor=CENTER)
            tblpersons.heading("status", text='STATUS', anchor=CENTER)

            for dt in result:
                tblpersons.insert(parent='', index='end', values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]))


            tblpersons.pack()

            pass

        pass


    def Account(self):

        self.delete_frame()

        # Read values from Window
        DID = [self.did]

        # Send values to search (database)
        result = driversearch1(DID)

        # Display Message
        lblMessage = Label(self.booking_frame, text='')
        lblMessage.place(x=350, y=180)

        if result == None:
            lblMessage['text'] = "Record not found"
        else:

            tableframe = Frame(self.booking_frame)

            tableframe.place(x=15, y=20)

            tblpersons = ttk.Treeview(tableframe)
            tblpersons['column'] = ('name', 'address', 'mobile', 'email', 'age', 'gender', 'num_plate', 'password')

            tblpersons.column("#0", width=0, stretch=NO)
            tblpersons.column("name", width=100, anchor=CENTER)
            tblpersons.column("address", width=100, anchor=CENTER)
            tblpersons.column("mobile", width=100, anchor=CENTER)
            tblpersons.column("email", width=120, anchor=CENTER)
            tblpersons.column("age", width=50, anchor=CENTER)
            tblpersons.column("gender", width=100, anchor=CENTER)
            tblpersons.column("num_plate", width=100, anchor=CENTER)
            tblpersons.column("password", width=100, anchor=CENTER)

            tblpersons.heading("#0", text='', anchor=CENTER)
            tblpersons.heading("name", text='Name', anchor=CENTER)
            tblpersons.heading("address", text='Address', anchor=CENTER)
            tblpersons.heading("mobile", text='Mobile', anchor=CENTER)
            tblpersons.heading("email", text='Email', anchor=CENTER)
            tblpersons.heading("age", text='AGE', anchor=CENTER)
            tblpersons.heading("gender", text='Gender', anchor=CENTER)
            tblpersons.heading("num_plate", text='Num Plate', anchor=CENTER)
            tblpersons.heading("password", text='Password', anchor=CENTER)


            tblpersons.insert(parent='', index='end',
                              values=(result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))

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
                age_txt.delete(0, END)
                gendertxt.delete(0, END)
                num_platetxt.delete(0, END)
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
                age_txt.insert(0, values[4])
                gendertxt.insert(0, values[5])
                num_platetxt.insert(0, values[6])
                passwordtxt.insert(0, values[7])

            tblpersons.bind('<ButtonRelease-1>', select_record)

            def deleteAccount():
                cd = []
                for c in selection(cid=selection):
                    cd.append(c[0])
                    lol_string = ''.join(map(str, cd))
                cid = lol_string  # Read value from TextBox
                print(cid)

                # Send values to search (Middleware)
                result = customerdelete(cid)
                # Display Message

                if result == True:
                    lblMessage['text'] = "Record Delete"
                else:
                    lblMessage['text'] = "Unsuccessfull"

                pass

            def saveUser():
                result = driversearch1(DID)
                # Read values from Window
                selected = tblpersons.focus()

                did = result[0]

                #update table
                tblpersons.item(selected, text="", values=(
                    nametxt.get(), addresstxt.get(), mobiletxt.get(), emailtxt.get(), age_txt.get(), gendertxt.get(), num_platetxt.get(),
                    passwordtxt.get()))

                # Update the database
                # Create a database or connect to one that exists
                conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='tbs')
                # Send values to save (database)
                sql = "UPDATE driver set name=%s, address=%s, mobile=%s, email=%s, age=%s, gender=%s, number_plate=%s, password=%s WHERE did=%s"
                values = (
                    nametxt.get(), addresstxt.get(), mobiletxt.get(), emailtxt.get(), age_txt.get(), gendertxt.get(),num_platetxt.get(),
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

            delete_btn = Button(self.booking_frame, text="Delete", command=deleteAccount)
            update_btn = Button(self.booking_frame, text="Update", command=saveUser)

            delete_btn.place(x=315, y=400)
            update_btn.place(x=260, y=400)

            namelbl = Label(self.booking_frame, text="Name")
            addresslbl = Label(self.booking_frame, text="Address")
            mobilelbl = Label(self.booking_frame, text="Mobile")
            emaillbl = Label(self.booking_frame, text="Email")
            doblbl = Label(self.booking_frame, text="AGE")
            genderlbl = Label(self.booking_frame, text="Gender")
            num_platelbl = Label(self.booking_frame, text="Num Plate")
            passwordlbl = Label(self.booking_frame, text="Password")

            # lblMessage = Label(self.booking_frame, text='', bg="gray")

            nametxt = Entry(self.booking_frame)
            addresstxt = Entry(self.booking_frame)
            mobiletxt = Entry(self.booking_frame)
            emailtxt = Entry(self.booking_frame)

            gendertxt = Entry(self.booking_frame)
            num_platetxt = Entry(self.booking_frame)
            passwordtxt = Entry(self.booking_frame)
            age_txt = Entry(self.booking_frame)


            namelbl.place(x=40, y=270)
            addresslbl.place(x=40, y=300)
            mobilelbl.place(x=250, y=270)
            emaillbl.place(x=250, y=300)
            doblbl.place(x=460, y=270)
            genderlbl.place(x=460, y=300)
            num_platelbl.place(x=40, y=330)
            passwordlbl.place(x=250, y=330)

            lblMessage.place(x=360, y=400)

            nametxt.place(x=100, y=270)
            addresstxt.place(x=100, y=300)
            mobiletxt.place(x=310, y=270)
            emailtxt.place(x=310, y=300)
            age_txt.place(x=520, y=270)
            gendertxt.place(x=520, y=300)
            num_platetxt.place(x=100, y=330)
            passwordtxt.place(x=310, y=330)

            pass