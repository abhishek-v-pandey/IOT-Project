import sqlite3
import socket 
s = socket.socket() 
host = '127.0.0.1' 
port = 12345
s.connect((host, port))  
a=s.recv(1024).decode()
print (a)    
conn = sqlite3.connect("TESTDB" )
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS TIME1")
conn.execute("CREATE TABLE TIME1 (d1  CHAR(90))");
print("\\connected To Db")
sql= "INSERT INTO TIME1(d1)VALUES(?)"
try:
   cursor.execute(sql,[a])
   conn.commit()
except:
   conn.rollback()
conn.close()
s.close() 


