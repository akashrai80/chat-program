import threading
import socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ip = "192.168.43.69"
s.connect(("192.168.43.69", 1234))
print("\t\t\t\t!! WELCOME TO MYCHAT !!")
print("\t\tRECEVING....\t\t\t\t\tSENDING.....")
def send():
	while True:
		data = input("\n\t\t\t\t\t\t\t<<< :")
		data = data.encode()
		s.send(data)

def rec():
	while True:
		z = s.recv(1024)
		z = z.decode()
		print("\n\t"+ip+": >>>"+z)


x1 = threading.Thread(target = rec)
x2 = threading.Thread(target = send)
x1.start()
x2.start()
