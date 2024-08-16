import socket
from viz import ShiftingGraph

from time import time_ns

toSec = 1e9


#localIP     = "146.136.88.23"
localPort   = 5555
bufferSize  = 1024 # 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind(('', localPort))
print("UDP server up and listening")




SG = ShiftingGraph()



min = -1
max = -1
mean = 0

t0 = time_ns()
# Listen for incoming datagrams
while(True):

    # Wait for UDP message
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]

    t_message = time_ns() - t0
    print("Time between messages received:", t_message/toSec ,"s")
    if t_message/toSec > 0.1: 
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    t0 = time_ns()
    
    SG.updateViz(int(message))
    
    t_new = time_ns()
    diff = t_new - t0
    t = t_new
    if(diff < min or min<0):
        min = diff
    if diff > max:
        max = diff
    mean += diff

    print("Plotting time:                 ", diff/toSec, "s")

    #num = int(message)
    #print(int)

    #address = bytesAddressPair[1]

    #clientMsg = "Message from Client:{}".format(message)
    #clientIP  = "Client IP Address:{}".format(address)
    
    #print(clientMsg)
    #print(clientIP)



