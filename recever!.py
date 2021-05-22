import threading
import socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ip = "192.168.43.69"
port = 1234
s.bind((ip , port))
s.listen()
c , addr  = s.accept()
sender_ip = str(addr[0])
print("\t\t\t\t!! WELLCOME TO MYCHAT !!\n\n\n")
print("\tRECEVING..\t\t\t\tSENDING...")
s.listen()
def rec():
    while True:
        z = c.recv(1024)
        z = z.decode()
        print("\t\n"+sender_ip+":>>> "+z)

def send():
    while True:
        data = input("\n\t\t\t\t\t\t<<< : ")
        data= data.encode()
        c.send(data)

x1 = threading.Thread(target = rec)
x2 = threading.Thread(target = send)
x1.start()
x2.start()
s.close()

