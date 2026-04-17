import socket
from local_machine_info import print_machine_info

print_machine_info()

host = '0.0.0.0'
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

print(f"UDP server listening on port {port}...\n")

while True:
    data, client_address = server_socket.recvfrom(1024)

    message = data.decode()
    print(f"Received from {client_address}: {message}")

    response = f"Server received: {message}"
    server_socket.sendto(response.encode(), client_address)