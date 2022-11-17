import mysql.connector as c
 
con=c.connect(host="localhost",user="sammy",password="password",database="db_name")

cursor=con.cursor()

query="INSERT INTO url_detail ('username','password') values (%s,%s,%s)"

cursor.execute(query)
con.commit()
print('add sussessfully')