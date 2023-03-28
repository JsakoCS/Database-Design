
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import *
# End Imports .
db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="katty"
        # user="sqluser",
        # password="password"
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

# create the "items" table
        cursor.execute("CREATE TABLE IF NOT EXISTS items ("
           "id INT AUTO_INCREMENT PRIMARY KEY,"
           "user_id VARCHAR(255),"
           "title VARCHAR(255),"
           "description TEXT,"
           "category VARCHAR(255),"
           "price DECIMAL(10, 2),"
           "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        db.commit() 
    else:
        invalidlabel = tk.Label(root, bg="pink", text="DB already initialized")
        invalidlabel.pack()
        
post_count = 0
# Define a function to create a new window for the register page .
def homepage():

    def post_item():
        global post_count
        first = title_entry.get()
        last = description_entry.get()
        user = category_entry.get()
        passw = price_entry.get()

        if(first == "" or last == "" or user == "" or passw == "" ):
            popup = tk.Toplevel()
            label = tk.Label(popup, text='Fields cannot be empty')
            label.pack(side="top", fill="x", pady=10)
            B1 = tk.Button(popup, text="OK", command=popup.destroy)
            B1.pack()
        else:
            result = create1(first, last,user,passw)
            if result == "success":
                success_popup = tk.Toplevel()
                success_label = tk.Label(success_popup, text='Item inserted successfully.')
                post_count += 1
                success_label.pack(side="top", fill="x", pady=10)
                success_B1 = tk.Button(success_popup, text="OK", command=success_popup.destroy)
                    # clear the entry fields
                title_entry.delete(0, tk.END)
                description_entry.delete(0, tk.END)
                category_entry.delete(0, tk.END)
                price_entry.delete(0, tk.END)

                success_B1.pack()
            else:
                error_popup = tk.Toplevel()
                error_label = tk.Label(error_popup, text='Error: You can only post 3 items a day.')
                error_label.pack(side="top", fill="x", pady=10)
                error_B1 = tk.Button(error_popup, text="OK", command=error_popup.destroy)
                error_B1.pack()

    def create1(first,last,username, password):
        # create the user database and select it
        cursor = db.cursor()

        
        cursor.execute("SELECT username FROM user WHERE username = %s", (username,))
        result = cursor.fetchone()
        if result is not None:
            user_id = result[0]
        else:
            # handle the case where the query returned no results
            if post_count >= 3:
                cursor.close()
                return "error"

        # Insert the item into the database
        cursor.execute("INSERT INTO items (title, description, category, price) VALUES ( %s, %s, %s, %s)", ( title_entry.get(), description_entry.get(), category_entry.get(), price_entry.get()))
        db.commit()
        cursor.close()
        return "success"




    # create a new Toplevel window
    home_window = tk.Toplevel(root)
    home_window.title("Home Page")
    home_window.configure(bg="pink")
    home_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a title label ( Register ) .
    home_label = tk.Label(home_window, bg="pink", text="Welcome!", font=50)
    home_label.pack()

    # Create a form to insert an item
    item_frame = tk.Frame(home_window, bg="pink")
    item_frame.pack(pady=10)

    title_label = tk.Label(item_frame, text="Title:", font=20, bg="pink")
    title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    title_entry = tk.Entry(item_frame, font=20)
    title_entry.grid(row=0, column=1, padx=5, pady=5)

    description_label = tk.Label(item_frame, text="Description:", font=20, bg="pink")
    description_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    description_entry = tk.Entry(item_frame, font=20)
    description_entry.grid(row=1, column=1, padx=5, pady=5)

    category_label = tk.Label(item_frame, text="Category:", font=20, bg="pink")
    category_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    category_entry = tk.Entry(item_frame, font=20)
    category_entry.grid(row=2, column=1, padx=5, pady=5)

    price_label = tk.Label(item_frame, text="Price:", font=20, bg="pink")
    price_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    price_entry = tk.Entry(item_frame, font=20)
    price_entry.grid(row=3, column=1, padx=5, pady=5)

    insert_button = tk.Button(item_frame, text="Insert", font=20, command=post_item)
    insert_button.grid(row=4, column=1, padx=5, pady=5)



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

