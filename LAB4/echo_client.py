import socket
from local_machine_info import print_machine_info

print_machine_info()

host = '127.0.0.1'
port = 6000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = input("Enter message: ")

client_socket.send(message.encode())

response = client_socket.recv(1024)

print("Server response:", response.decode())

client_socket.close()