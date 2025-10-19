mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword", 
  database="alx_book_store"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM Books"
mycursor.execute(sql)