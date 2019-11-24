import socket      
import time 
s = socket.socket()      
host = '127.0.0.1'  
port = 12345
s.bind((host, port))    
s.listen(5)   
while True: 
   c, addr = s.accept()         
   print ('got connecton from addr', addr) 
   date = time.asctime() 
   d = str(date) 
   c.send(d.encode())       
   c.close() 
