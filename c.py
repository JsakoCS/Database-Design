import mysql.connector


# connect to the MySQL server
db = mysql.connector.connect(
   host="localhost",
   user="sqluser",
   password="password"
)


# create the user database and select it
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS user")
cursor.execute("USE user")


# create the user table
cursor.execute("CREATE TABLE IF NOT EXISTS user ("
              "username VARCHAR(255) PRIMARY KEY,"
              "password VARCHAR(255),"
              "firstName VARCHAR(255),"
              "lastName VARCHAR(255),"
              "email VARCHAR(255) UNIQUE)")




# function to register a new user
def register():
   username = input("Enter a username: ")
   password = input("Enter a password: ")
   firstName = input("Enter your first name: ")
   lastName = input("Enter your last name: ")
   email = input("Enter your email: ")


   # insert the new user into the user table
   cursor.execute("INSERT INTO user (username, password, firstName, lastName, email) "
                  "VALUES (%s, %s, %s, %s, %s)",
                  (username, password, firstName, lastName, email))
   db.commit()
   print("Registration successful!")




# function to log in an existing user
def login():
   username = input("Enter your username: ")
   password = input("Enter your password: ")


   # check if the user exists in the user table
   cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s",
                  (username, password))
   user = cursor.fetchone()


   if user:
       print("Login successful!")
   else:
       print("Invalid username or password")




# test the registration and login functions
register()
login()

