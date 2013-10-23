import socket, sys, select

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("localhost", 5555))

data = my_socket.recv(1024)
print "received: \n%s" % data
"""message = sys.stdin.readline()
my_socket.send(message)
data2 = my_socket.recv(1024)
print data2
"""

running = True
while running:
    inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [], [])
    
    for s in inputready:
        
        if s == my_socket:
            msg = s.recv(1024)
            sys.stdout.write(msg)

        elif s == sys.stdin:
            message = sys.stdin.readline()
            my_socket.send(message)

        else:
            print "Disconnected from server!"
            running = False

my_socket.close()

