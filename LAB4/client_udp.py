import socket
from local_machine_info import print_machine_info

print_machine_info()

host = '127.0.0.1'
port = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter message: ")

client_socket.sendto(message.encode(), (host, port))

data, server = client_socket.recvfrom(1024)

print("Response from server:", data.decode())

client_socket.close()