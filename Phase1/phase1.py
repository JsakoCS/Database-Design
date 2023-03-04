# Imports ...
import tkinter as tk
# End Imports .



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

# Define a function to create a new window for the register page .
def register():
    # Create a new window .
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
    register_window_button = tk.Button(register_window, bg="black", fg="pink", activebackground="pink", activeforeground="pink", text="R e g i s t e r", width=30, height=3)
    register_window_button.pack(pady=40)
    
# Define a function to create a new window for the login page .
def login():
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
    login_window_button = tk.Button(login_window, bg="black", fg="pink", activebackground="pink", activeforeground="pink", text="L o g i n", width=30, height=3)
    login_window_button.pack(pady=40)

# Create the Register , Login , and Initialize Database buttons for the main window .
register_button = tk.Button(root, bg="pink", fg="black", activebackground="black", activeforeground="black", text="Register", width=25, height=5, command=register)
register_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

login_button = tk.Button(root, bg="pink", fg="black", activebackground="black", activeforeground="black", text="Login", width=25, height=5, command=login)
login_button.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

initialize_database_button = tk.Button(root, bg="pink", fg="black", activebackground="black", activeforeground="black", text="Initialize Database", width=25, height=5) # add command=initialize_database
initialize_database_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)



# Start the GUI .
root.mainloop()
