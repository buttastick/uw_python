"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50001
host must be present if you want to provide port
"""

import socket 
import sys

host = 'localhost' 
port = 50001
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

#s = socket.socket(socket.AF_INET, 
#                 socket.SOCK_STREAM) 
#s.connect((host,port))

#This is where you started fucking with shit

run_check = True

while run_check:
    echo = raw_input ("What would you like to echo?")
    s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
    s.connect((host,port))
    if echo == '':
        run_check = False
    else:
        s.send(echo)
        data = s.recv(size)
        print data
#s.send('Hello, world') 
##data = s.recv(size)

#and here
##print data
#end hash

s.close() 
#print 'from (%s,%s) %s' % (host, port, data)

