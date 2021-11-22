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

sql = "Select * from users where name = '" + username + "' AND password = '"+ userpass +"';"
print(sql)

cursor.execute(sql)

myresult = cursor.fetchall()

for x in myresult:
  print(x)
