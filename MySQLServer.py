import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword", 
  database="alx_book_store"
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
except mysql.connector.Error as e:
    print("Failed to connect to database!")


print("Database 'alx_book_store' created successfully!")