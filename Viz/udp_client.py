import socket

class udpClient:
    def __init__(self):
        self.UDP_IP = "146.136.40.46"
        self.UDP_PORT = 5555

        print("UDP target IP:", self.UDP_IP)
        print("UDP target port:", self.UDP_PORT)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

    def udpClientSend(self, num):
        print("Sending: ",num)
        self.sock.sendto(bytes(str(num), "utf-8"), (self.UDP_IP, self.UDP_PORT))

if __name__ == "__main__":
    
    udp = udpClient()
    
    for i in range(400):
        udp.udpClientSend(i)
