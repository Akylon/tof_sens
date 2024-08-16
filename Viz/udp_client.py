import socket

class udpClient:
    def __init__(self):
        self.UDP_IP = "146.136.40.44"
        self.UDP_PORT = 5555
        #self.MESSAGE = "Hello, World!"

        print("UDP target IP:", self.UDP_IP)
        print("UDP target port:", self.UDP_PORT)
        #print("message:", self.MESSAGE)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

    def udpClientSend(self, num):
        print("Sending: ",num)
        self.sock.sendto(bytes(str(num), "utf-8"), (self.UDP_IP, self.UDP_PORT))
