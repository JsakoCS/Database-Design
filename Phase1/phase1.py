
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import *
# End Imports .
db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456"
    )
if (db):
    print("coneccted")
else:
    print("not connect")

# Create the main window ( root ) .
root = tk.Tk()
root.title("Phase1")
root.configure(bg="black")

# Set the window size and position it at the center of the screen .
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

def initialize():


    # create the user database and select it
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")
    if "user" not in cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS user")
        cursor.execute("USE user")

    # create the user table
        cursor.execute("CREATE TABLE IF NOT EXISTS user ("
                   "username VARCHAR(255) PRIMARY KEY,"
                   "password VARCHAR(255),"
                   "firstName VARCHAR(255),"
                   "lastName VARCHAR(255),"
                   "email VARCHAR(255) UNIQUE)")
        db.commit()
    else:
        invalidlabel = tk.Label(root, bg="pink", text="DB already initialized")
        invalidlabel.pack()

# Define a function to create a new window for the register page .
def homepage():
    home_window = tk.Toplevel(root)
    home_window.title("Home Page")
    home_window.configure(bg="pink")
    home_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a title label ( Register ) .
    home_label = tk.Label(home_window, bg="pink", text="Welcome!", font=50)
    home_label.pack()

def register():
    def create():
        first = first_name_entry.get()
        last = last_name_entry.get()
        user = username_entry.get()
        passw = password_entry.get()
        confirmpass = confirm_password_entry.get()
        email = email_entry.get()
        if(first == "" or last == "" or user == "" or passw == "" or confirmpass == "" or email == ""):
            popup = tk.Tk()
            label = tk.Label(popup, text='Fields cannot be empty')
            label.pack(side="top", fill="x", pady=10)
            B1 = tk.Button(popup, text="OK", command=popup.destroy)
            B1.pack()
            #popup.mainloop()

        else:
            create1(first, last,user,passw,confirmpass,email)

    def create1(first,last,username, password,confirm,email):


        # create the user database and select it
        cursor = db.cursor()

        #cursor.execute("SHOW DATABASES")


        cursor.execute("USE user")
        cursor.execute("SELECT * FROM user WHERE username = %s OR email = %s",
                       (username, email))
        user = cursor.fetchone()

        if user:


            print("User name or email already exists")
            invalidlabel = tk.Label(register_window, bg="pink", text="Username or email already exists")
            invalidlabel.pack()
        else:
            if (password == confirm):

                cursor.execute("INSERT INTO user (username, password, firstName, lastName, email) "
                           "VALUES (%s, %s, %s, %s, %s)",
                           (username, password, first, last, email))
                db.commit()
                popup = tk.Tk()
                label = tk.Label(popup, text='Account Registered!')
                label.pack(side="top", fill="x", pady=10)
                B1 = tk.Button(popup, text="OK", command=popup.destroy)
                B1.pack()
            else:
                print("Passwords not match")
                invalidlabel = tk.Label(register_window, bg="pink", text="Passwords not match")
                invalidlabel.pack()



    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.configure(bg="pink")
    register_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a title label ( Register ) .
    register_label = tk.Label(register_window, bg="pink", text="R e g i s t e r", font=50)
    register_label.pack(pady=40)

    # Create 6 labels and entry boxes ( for first name , last name , username , email , password , and confirm password ) .
    # ( 1 ) .
    first_name_label = tk.Label(register_window, bg="pink", text="First Name :")
    first_name_label.pack()
    first_name_entry = tk.Entry(register_window, bg="black", fg="pink", width=50)
    first_name_entry.pack()
    # ( 2 ) .
    last_name_label = tk.Label(register_window, bg="pink", text="Last Name :")
    last_name_label.pack()
    last_name_entry = tk.Entry(register_window, bg="black", fg="pink", width=50)
    last_name_entry.pack()
    # ( 3 ) .
    username_label = tk.Label(register_window, bg="pink", text="Username :")
    username_label.pack()
    username_entry = tk.Entry(register_window, bg="black", fg="pink", width=50)
    username_entry.pack()
    # ( 4 ) .
    email_label = tk.Label(register_window, bg="pink", text="Email :")
    email_label.pack()
    email_entry = tk.Entry(register_window, bg="black", fg="pink", width=50)
    email_entry.pack()
    # ( 5 ) .
    password_label = tk.Label(register_window, bg="pink", text="Password :")
    password_label.pack()
    password_entry = tk.Entry(register_window, bg="black", fg="pink", width=50, show="•")
    password_entry.pack()
    # ( 6 ) .
    confirm_password_label = tk.Label(register_window, bg="pink", text="Confirm Password :")
    confirm_password_label.pack()
    confirm_password_entry = tk.Entry(register_window, bg="black", fg="pink", width=50, show="•")
    confirm_password_entry.pack()

    # Create a register button .
    register_window_button = tk.Button(register_window,command=create, bg="black", fg="pink", activebackground="pink",
                                       activeforeground="pink", text="R e g i s t e r", width=30, height=3)
    register_window_button.pack(pady=40)


# Define a function to create a new window for the login page .

def login():
    def submit():
        username = username_entry_login.get()
        password = password_entry_login.get()
        if(username == "" or password == ""):
            invalidlabel = tk.Label(login_window, bg="pink", text="Fields are empty")
            invalidlabel.pack()
        else:
            submit1(username, password)

    def submit1(username, password):


        # create the user database and select it
        cursor = db.cursor()

        cursor.execute("USE user")

        cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s",
                       (username, password))
        user = cursor.fetchone()

        if user:
            homepage()

        else:
            print("invalud")
            invalidlabel = tk.Label(login_window, bg="pink", text="Wrong username or password")
            invalidlabel.pack()

    # Create a new window .
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.configure(bg="pink")
    login_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a title label ( Login ) .
    login_label = tk.Label(login_window, bg="pink", text="L o g i n", font=50)
    login_label.pack(pady=40)

    # Create 2 labels and entry boxes ( for username and password ) .
    # ( 1 ) .
    username_label_login = tk.Label(login_window, bg="pink", text="Username :")
    username_label_login.pack()
    username_entry_login = tk.Entry(login_window, bg="black", fg="pink", width=50)
    username_entry_login.pack()
    # ( 2 ) .
    password_label_login = tk.Label(login_window, bg="pink", text="Password :")
    password_label_login.pack()
    password_entry_login = tk.Entry(login_window, bg="black", fg="pink", width=50, show="•")
    password_entry_login.pack()

    # Create a login button .
    login_window_button = tk.Button(login_window,command=submit, bg="black", fg="pink", activebackground="pink",
                                    activeforeground="pink", text="L o g i n", width=30, height=3)
    login_window_button.pack(pady=40)



# Create the Register , Login , and Initialize Database buttons for the main window .
register_button = tk.Button(root, bg="pink", fg="black", activebackground="black", activeforeground="black",
                            text="Register", width=25, height=5, command=register)
register_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

login_button = tk.Button(root, bg="pink", fg="black", activebackground="black", activeforeground="black", text="Login",
                         width=25, height=5, command=login)
login_button.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

initialize_database_button = tk.Button(root, bg="pink", fg="black", activebackground="black", activeforeground="black",
                                       text="Initialize Database", width=25,
                                       height=5, command=initialize)  # add command=initialize_database
initialize_database_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

# Start the GUI .
root.mainloop()

