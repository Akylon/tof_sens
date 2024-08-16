import socket

#localIP     = "146.136.88.23"
localPort   = 5555
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind(('', localPort))
print("UDP server up and listening")

# Listen for incoming datagrams
while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    print(int(message))
    #num = int(message)
    #print(int)

    #address = bytesAddressPair[1]

    #clientMsg = "Message from Client:{}".format(message)
    #clientIP  = "Client IP Address:{}".format(address)
    
    #print(clientMsg)
    #print(clientIP)

    # TODO Call visualization func


