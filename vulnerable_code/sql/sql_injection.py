import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="security_user",
  password="pass1234",
  database="security_testing"
)

cursor = mydb.cursor()


# ' or '' = '
username = input("Enter the username: ")
userpass = input("Enter the password: ")

sql = "SELECT * FROM users WHERE name = %s AND password = %s;"
print(sql)

login = (username, userpass)

cursor.execute(sql, login)

myresult = cursor.fetchall()

for x in myresult:
  print(x)
