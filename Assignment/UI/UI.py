from tkinter import *
import tkinter as tk
import re
import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from Assignment.Manager.admin.admin_database import adminsearch
from Assignment.UI.Customer_Dashboard import CUSTOMER
from Assignment.UI.Admin_Dashboard import ADMIN
from Assignment.Classes.Driver.driver_class import driverregister
from Assignment.UI.DRIVER_Dashboard import DRIVER_DASHBOARD
from Assignment.Manager.customer.database import *
from Assignment.Manager.driver.driver_database import *





# create a class for login
# every frame will work inside this class where tkinter is pass while calling the class LOGIN
class LOGIN():

    def __init__(self, master):
        super().__init__()
        # passing the master to create a framework
        self.Window_main = master

        #create frame
        self.frame = Frame(self.Window_main, bg="#E0E4CC", height=400, width=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        #create label and text box
        self.headlbl = Label(self.frame, text="Welcome", font=("San Francisco", 26), bg="#E0E4CC")
        self.usernamelbl = Label(self.frame, text="Mobile:", font=("San Francisco", 14), bg="#E0E4CC")
        self.passwordlbl = Label(self.frame, text="Password:", font=("San Francisco", 14), bg="#E0E4CC")
        self.lblMessage = Label(self.frame, text='', bg="#E0E4CC")

        # Create a variable to store the password visibility
        self.show_password_var = tk.IntVar()

        self.usernametxt = Entry(self.frame, width=15, font=("San Francisco", 14), )
        self.passwordtxt = Entry(self.frame, width=15, show="*",font=("San Francisco", 14))

        self.loginbtn = Button(self.frame, text="Login", command=self.searchUser)
        self.registerbtn = Button(self.frame, text="Create a account", command=self.register_btn)

        self.headlbl.place(relx=0.5, rely=0.15, anchor=CENTER)
        self.usernamelbl.place(relx=0.15, rely=0.45, anchor=CENTER)
        self.passwordlbl.place(relx=0.15, rely=0.55, anchor=CENTER)
        self.usernametxt.place(relx=0.6, rely=0.45, anchor=CENTER)
        self.passwordtxt.place(relx=0.6, rely=0.55, anchor=CENTER)
        self.loginbtn.place(relx=0.7, rely=0.7, anchor=CENTER)

        self.registerbtn.place(relx=0.5, rely=0.85, anchor=CENTER)

        # Create the "show password" checkbutton
        self.show_password_checkbutton = tk.Checkbutton(self.frame, text="Show Password",
                                                        variable=self.show_password_var,
                                                        command=self.show_password)
        self.show_password_checkbutton.place(x=200, y=250, anchor=CENTER)

    #function to show password
    def show_password(self):
        if self.show_password_var.get() == 1:
            self.passwordtxt.config(show="")
        else:
            self.passwordtxt.config(show="*")



    def searchUser(self):
        # Read values from Window
        # Read value from TextBox
        mobile = (self.usernametxt.get())
        password = (self.passwordtxt.get())

        # Send values to search (Middleware)
        result = customersearch(mobile, password)
        admin = adminsearch(mobile, password)
        record = driversearch(mobile, password)
        print(result)

        def validate_mobile(mobile):
            if len(mobile) == 0:
                # Display an error message in a message box
                messagebox.showerror("Error", "Please enter a valid name")
                return False
            return True

        def validate_password(password):
            if len(password) == 0:
                # Display an error message in a message box
                messagebox.showerror("Error", "Please enter a valid address")
                return False
            return True

        MOBILE = validate_mobile(mobile)
        PASSWORD = validate_password(password)

        if MOBILE==True and PASSWORD==True:

            # Display Message
            #check users from mobile and password
            if mobile == "admin" and password == "admin":
                #passing root in admin dashboard after declaring neccessary window frame
                Window_main_admin = self.Window_main
                Window_main_admin.title("Taxi Booking System")
                mywidth = 1150
                myheight = 600
                screen_width = Window_main_admin.winfo_screenwidth()
                screen_height = Window_main_admin.winfo_screenheight()

                xCordinate = int((screen_width / 2) - (mywidth / 2))
                yCordinate = int((screen_height / 2) - (myheight / 2))
                Window_main_admin.geometry('{}x{}+{}+{}'.format(mywidth, myheight, xCordinate, yCordinate))
                Window_main_admin.resizable(False, False)
                window = ADMIN(Window_main_admin)
                Window_main_admin.mainloop()

                return window


            #check for customer users
            if result == None:
                self.lblMessage['text'] = "Record not found"
            else:
                id = []
                global cid
                #getting customer id for specific customer information while login
                for i in result:
                    j = str(i)
                    id.append(j[0])
                    lol_string = ''.join(map(str, id))
                    cid = lol_string[0]

                #passing root in customer dashboard after declaring neccessary window frame
                Window_main_customer = root
                Window_main_customer.title("Taxi Booking System")
                mywidth = 1150
                myheight = 600
                screen_width = Window_main_customer.winfo_screenwidth()
                screen_height = Window_main_customer.winfo_screenheight()

                xCordinate = int((screen_width / 2) - (mywidth / 2))
                yCordinate = int((screen_height / 2) - (myheight / 2))
                Window_main_customer.geometry('{}x{}+{}+{}'.format(mywidth, myheight, xCordinate, yCordinate))
                Window_main_customer.resizable(False, False)

                #call class CUSTOMER_DASHBOARD and passing frame and customer id
                window = CUSTOMER(Window_main_customer, cid)
                Window_main_customer.mainloop()

                return window

            #checking for driver user
            if record == None:
                messagebox.showerror("Error", "Cannot find your account. Please register first")
            else:
                id = []
                global did
                #getting driver id for specific driver information while login
                for i in record:
                    j = str(i)
                    id.append(j[0])
                    lol_string = ''.join(map(str, id))
                    did = lol_string[0]

                #passing root in driver dashboard after declaring neccessary window frame
                Window_main_driver = self.Window_main
                Window_main_driver.title("Taxi Booking System")
                mywidth = 1150
                myheight = 600
                screen_width = Window_main_driver.winfo_screenwidth()
                screen_height = Window_main_driver.winfo_screenheight()

                xCordinate = int((screen_width / 2) - (mywidth / 2))
                yCordinate = int((screen_height / 2) - (myheight / 2))
                Window_main_driver.geometry('{}x{}+{}+{}'.format(mywidth, myheight, xCordinate, yCordinate))
                Window_main_driver.resizable(False, False)
                #call class DRIVER_DASHBOARD and passing frame and driver id
                window = DRIVER_DASHBOARD(Window_main_driver, did)
                Window_main_driver.mainloop()

                return window

    #call register page
    def register_btn(self):
        # removing widgit
        self.frame.destroy()
        Window_main_register = self.Window_main
        window = REGISTER(Window_main_register)
        Window_main_register.mainloop()
        return window
        pass




from Assignment.Classes.Customer.Register import register
from Assignment.Manager.customer.database import customerinsert
# create a class for login
# every frame will work inside this class where tkinter is pass while calling the class LOGIN
class REGISTER():
    def __init__(self, master):
        super().__init__()
        # passing the master to create a framework
        self.Window_main = master
        #create frame
        self.frame = Frame(self.Window_main, bg="#E0E4CC", height=550, width=750)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Create a variable to store the password visibility
        self.show_password_var = tk.IntVar()

        #add label and text for registration
        self.headlbl = Label(self.frame, text="Register", font=("San Francisco", 26), bg="#E0E4CC")
        self.namelbl = Label(self.frame, text="Name", font=("San Francisco", 14), bg="#E0E4CC")
        self.addresslbl = Label(self.frame, text="Address", font=("San Francisco", 14), bg="#E0E4CC")
        self.mobilelbl = Label(self.frame, text="Mobile", font=("San Francisco", 14), bg="#E0E4CC")
        self.emaillbl = Label(self.frame, text="Email", font=("San Francisco", 14), bg="#E0E4CC")
        self.doblbl = Label(self.frame, text="DOB", font=("San Francisco", 14), bg="#E0E4CC")
        self.genderlbl = Label(self.frame, text="Gender", font=("San Francisco", 14), bg="#E0E4CC")
        self.passwordlbl = Label(self.frame, text="Password", font=("San Francisco", 14), bg="#E0E4CC")

        self.nametxt = Entry(self.frame, width=15, font=("San Francisco", 14), )
        self.addresstxt = Entry(self.frame, width=15, font=("San Francisco", 14))
        self.mobiletxt = Entry(self.frame, width=15, font=("San Francisco", 14))
        self.emailtxt = Entry(self.frame, width=15, font=("San Francisco", 14))
        self.dobtxt = Entry(self.frame, width=15, font=("San Francisco", 14))
        self.gendertxt = Entry(self.frame, width=15, font=("San Francisco", 14))
        self.passwordtxt = Entry(self.frame, width=15, show="*", font=("San Francisco", 14))

        self.loginbtn = Button(self.frame, text="Login", command=self.login)
        self.registerbtn = Button(self.frame, text="Register", command=self.saveUser)
        self.driverbtn = Button(self.frame, text="Driver Account", command=self.driver)

        self.headlbl.place(relx=0.5, rely=0.15, anchor=CENTER)
        self.namelbl.place(relx=0.35, rely=0.35, anchor=CENTER)
        self.addresslbl.place(relx=0.3655, rely=0.4, anchor=CENTER)
        self.mobilelbl.place(relx=0.353, rely=0.45, anchor=CENTER)
        self.emaillbl.place(relx=0.348, rely=0.5, anchor=CENTER)
        self.doblbl.place(relx=0.345, rely=0.55, anchor=CENTER)
        self.genderlbl.place(relx=0.358, rely=0.6, anchor=CENTER)
        self.passwordlbl.place(relx=0.375, rely=0.65, anchor=CENTER)

        self.nametxt.place(relx=0.6, rely=0.35, anchor=CENTER)
        self.addresstxt.place(relx=0.6, rely=0.4, anchor=CENTER)
        self.mobiletxt.place(relx=0.6, rely=0.45, anchor=CENTER)
        self.emailtxt.place(relx=0.6, rely=0.5, anchor=CENTER)

        self.dob_txt = DateEntry(self.frame,width=12, background='darkblue',foreground='white', borderwidth=2)
        self.dob_txt.place(relx=0.6, rely=0.55, width=170, anchor=CENTER)
        self.dob_txt.bind("<<DateEntrySelected>>")
        self.gendertxt.place(relx=0.6, rely=0.6, anchor=CENTER)
        self.passwordtxt.place(relx=0.6, rely=0.65, anchor=CENTER)

        # Create the "show password" checkbutton
        self.show_password_checkbutton = tk.Checkbutton(self.frame, text="Show Password",
                                                        variable=self.show_password_var,
                                                        command=self.show_password)
        self.show_password_checkbutton.place(x=400, y=400, anchor=CENTER)

        self.loginbtn.place(relx=0.9, rely=0.1, anchor=CENTER)
        self.registerbtn.place(x=480, y=450)
        self.driverbtn.place(x=10, y=20)

    # function to show password
    def show_password(self):
        if self.show_password_var.get() == 1:
            self.passwordtxt.config(show="")
        else:
            self.passwordtxt.config(show="*")

    #save new register
    def saveUser(self):

        # Read values from Window
        # Read value from TextBox
        name = (self.nametxt.get())
        address = (self.addresstxt.get())
        mobile = (self.mobiletxt.get())
        email = (self.emailtxt.get())
        dob = (self.dobtxt.get())
        gender = (self.gendertxt.get())
        password = (self.passwordtxt.get())

        def validate_name(name):
            if len(name) == 0:
                # Display an error message in a message box
                messagebox.showerror("Error", "Please enter a valid name")
                return False
            return True

        def validate_address(address):
            if len(address) == 0:
                # Display an error message in a message box
                messagebox.showerror("Error", "Please enter a valid address")
                return False
            return True

        def validate_mobile(mobile):
            num = [mobile]
            result = customergetAll1(num)
            if result:
                messagebox.showerror("Error", "Mobile number already exist")
                return False
            else:
                return True

        def validate_email(email):
            # Add your validation code here
            # For example, you can use a regular expression to check if the email is in the correct format
            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                messagebox.showerror("Error", "Please enter a valid email address")
                return False
            return True


        def validate_gender(gender):
            # Add your validation code here
            # For example, you can check if the gender is "male" or "female"
            if gender.lower() not in ["male", "female"]:
                messagebox.showerror("Error", "Please enter a valid gender (male or female)")
                return False
            return True

        def validate_password(password):
            # Add your validation code here
            # For example, you can check if the password meets certain criteria (e.g., length, complexity)
            if len(password) < 8:
                messagebox.showerror("Error", "Password must be at least 8 characters long")
                return False
            if not any(char.isdigit() for char in password):
                messagebox.showerror("Error", "Password must contain at least one digit")
                return False
            if not any(char.isupper() for char in password):
                messagebox.showerror("Error", "Password must contain at least one uppercase letter")
                return False
            if not any(char.islower() for char in password):
                messagebox.showerror("Error", "Password must contain at least one lowercase letter")
                return False
            return True

        NAME = validate_name(name)
        ADDRESS = validate_address(address)
        MOBILE = validate_mobile(mobile)
        EMAIL = validate_email(email)
        GENDER = validate_gender(gender)
        PASSWORD = validate_password(password)

        if NAME == True and ADDRESS == True and MOBILE == True and EMAIL == True and GENDER == True and PASSWORD == True:
            c1 = register("", name, address, mobile, email, self.dob_txt.get(), gender, password)

            # Send values to save (database)
            result = customerinsert(c1)
            # Display Message
            if result['status']==True:
                # self.lblMessage['text']="Save Record"
                messagebox.showinfo("Done", "Account created, Now you can log in using mobile number as password")

    #switch to login
    def login(self):
        self.frame.destroy()
        window = self.Window_main
        c = LOGIN(window)
        return c

    # switch driver frame
    def driver(self):
        self.frame.destroy()
        window = self.Window_main
        c = DRIVER(window)
        return c




# create a class for login
# every frame will work inside this class where tkinter is pass while calling the class LOGIN
class DRIVER():
    def __init__(self, master):
        super().__init__()
        # passing the master to create a framework
        self.Window_main = master
        #create frame
        self.frame = Frame(self.Window_main, bg="#E0E4CC", height=550, width=750)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        #add label and text box
        self.headlbl = Label(self.frame, text="Register", font=("San Francisco", 26), bg="#E0E4CC")
        self.namelbl = Label(self.frame, text="Name", font=("San Francisco", 14), bg="#E0E4CC")
        self.addresslbl = Label(self.frame, text="Address", font=("San Francisco", 14), bg="#E0E4CC")
        self.mobilelbl = Label(self.frame, text="Mobile", font=("San Francisco", 14), bg="#E0E4CC")
        self.emaillbl = Label(self.frame, text="Email", font=("San Francisco", 14), bg="#E0E4CC")
        self.doblbl = Label(self.frame, text="Age", font=("San Francisco", 14), bg="#E0E4CC")
        self.genderlbl = Label(self.frame, text="Gender", font=("San Francisco", 14), bg="#E0E4CC")
        self.passwordlbl = Label(self.frame, text="Password", font=("San Francisco", 14), bg="#E0E4CC")
        self.numberplatelbl = Label(self.frame, text="Num. Plate", font=("San Francisco", 14), bg="#E0E4CC")


        self.nametxt = Entry(self.frame, width=15, font=("San Francisco", 14), )
        self.addresstxt = Entry(self.frame, width=15, font=("San Francisco", 14))
        self.mobiletxt = Entry(self.frame, width=15, font=("San Francisco", 14))
        self.emailtxt = Entry(self.frame, width=15, font=("San Francisco", 14))
        self.dobtxt = Entry(self.frame, width=15, font=("San Francisco", 14))
        self.gendertxt = Entry(self.frame, width=15, font=("San Francisco", 14))
        self.passwordtxt = Entry(self.frame, width=15, show="*", font=("San Francisco", 14))

        self.numberplate = ttk.Combobox(self.frame,width=13, font=("San Francisco", 14))
        self.numberplate['values'] = ['STATE 1','STATE 2','STATE 3','STATE 4','STATE 5','STATE 6','STATE 7']

        self.registerbtn = Button(self.frame, text="Register", command=self.saveUser)

        self.headlbl.place(relx=0.5, rely=0.15, anchor=CENTER)
        self.namelbl.place(relx=0.35, rely=0.35, anchor=CENTER)
        self.addresslbl.place(relx=0.3655, rely=0.4, anchor=CENTER)
        self.mobilelbl.place(relx=0.353, rely=0.45, anchor=CENTER)
        self.emaillbl.place(relx=0.348, rely=0.5, anchor=CENTER)
        self.doblbl.place(relx=0.345, rely=0.55, anchor=CENTER)
        self.genderlbl.place(relx=0.358, rely=0.6, anchor=CENTER)
        self.passwordlbl.place(relx=0.375, rely=0.65, anchor=CENTER)
        self.numberplatelbl.place(relx=0.375, rely=0.7, anchor=CENTER)

        self.nametxt.place(relx=0.6, rely=0.35, anchor=CENTER)
        self.addresstxt.place(relx=0.6, rely=0.4, anchor=CENTER)
        self.mobiletxt.place(relx=0.6, rely=0.45, anchor=CENTER)
        self.emailtxt.place(relx=0.6, rely=0.5, anchor=CENTER)
        self.dobtxt.place(relx=0.6, rely=0.55, anchor=CENTER)
        self.gendertxt.place(relx=0.6, rely=0.6, anchor=CENTER)
        self.passwordtxt.place(relx=0.6, rely=0.65, anchor=CENTER)
        self.numberplate.place(relx=0.6, rely=0.7, anchor=CENTER)

        self.registerbtn.place(x=480, y=450)

        self.loginbtn = Button(self.frame, text="Login", command=self.login)
        self.loginbtn.place(relx=0.9, rely=0.1, anchor=CENTER)
    def saveUser(self):

        # Read values from Window
        # Read value from TextBox
        name = (self.nametxt.get())
        address = (self.addresstxt.get())
        mobile = (self.mobiletxt.get())
        email = (self.emailtxt.get())
        dob = (self.dobtxt.get())
        gender = (self.gendertxt.get())
        number_plate = (self.numberplate.get())
        password = (self.passwordtxt.get())
        status = "open"

        def validate_name(name):
            if len(name) == 0:
                # Display an error message in a message box
                messagebox.showerror("Error", "Please enter a valid name")
                return False
            return True

        def validate_address(address):
            if len(address) == 0:
                # Display an error message in a message box
                messagebox.showerror("Error", "Please enter a valid address")
                return False
            return True

        def validate_mobile(mobile):
            num = [mobile]
            result = customergetAll1(num)
            if result:
                messagebox.showerror("Error", "Mobile number already exist")
                return False
            else:
                return True

        def validate_email(email):
            # Add your validation code here
            # For example, you can use a regular expression to check if the email is in the correct format
            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                messagebox.showerror("Error", "Please enter a valid email address")
                return False
            return True

        def validate_dob(dob):
            if len(dob) == 0:
                # Display an error message in a message box
                messagebox.showerror("Error", "Please enter a valid date")
                return False
            return True

        def validate_gender(gender):
            # Add your validation code here
            # For example, you can check if the gender is "male" or "female"
            if gender.lower() not in ["male", "female"]:
                messagebox.showerror("Error", "Please enter a valid gender (male or female)")
                return False
            return True

        def validate_password(password):
            # Add your validation code here
            # For example, you can check if the password meets certain criteria (e.g., length, complexity)
            if len(password) < 8:
                messagebox.showerror("Error", "Password must be at least 8 characters long")
                return False
            if not any(char.isdigit() for char in password):
                messagebox.showerror("Error", "Password must contain at least one digit")
                return False
            if not any(char.isupper() for char in password):
                messagebox.showerror("Error", "Password must contain at least one uppercase letter")
                return False
            if not any(char.islower() for char in password):
                messagebox.showerror("Error", "Password must contain at least one lowercase letter")
                return False
            return True

        NAME = validate_name(name)
        ADDRESS = validate_address(address)
        MOBILE = validate_mobile(mobile)
        EMAIL = validate_email(email)
        DOB = validate_dob(dob)
        GENDER = validate_gender(gender)
        PASSWORD = validate_password(password)

        if NAME == True and ADDRESS == True and MOBILE == True and EMAIL == True and DOB == True and GENDER == True and PASSWORD == True:
            c1 = driverregister("", name, address, mobile, email, dob, gender, number_plate, password, status)

            # Send values to save (database)
            result = driverinsert(c1)
            # Display Message
            if result['status']==True:
                # self.lblMessage['text']="Save Record"
                messagebox.showinfo("Done", "Account created, Now you can log in using mobile number as password")

    #switch to login
    def login(self):
        self.frame.destroy()
        window = self.Window_main
        c = LOGIN(window)
        return c


#declearing main root
root = Tk()
root.title("Taxi Booking System")

mywidth = 1150
myheight = 600
#getting device display width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

xCordinate = int((screen_width / 2) - (mywidth / 2))
yCordinate = int((screen_height / 2) - (myheight / 2))
root.geometry('{}x{}+{}+{}'.format(mywidth, myheight, xCordinate, yCordinate))
root.resizable(False, False)
root['background']='#F38630'

#create frame
frame = Frame(root, bg="#E0E4CC", height=400, width=350)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#call login class
def login_main():
    window = LOGIN(root)
    return window

#call register class
def register_main():
    window2 = REGISTER(root)
    return window2

#add label
headlbl = Label(frame, text="Welcome", font=("San Francisco", 26), bg="#E0E4CC")
loginbtn = Button(frame, text="Login",width = 20, command=login_main)
registerbtn = Button(frame, text="Create a account",width= 20, command=register_main)

headlbl.place(relx=0.5, rely=0.15, anchor=CENTER)
loginbtn.place(relx=0.5, rely=0.47, anchor=CENTER)
registerbtn.place(relx=0.5, rely=0.6, anchor=CENTER)


root.mainloop()
