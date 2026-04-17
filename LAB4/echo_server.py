import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()

host = '0.0.0.0'
port = 6000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print("TCP Echo Server running...")
print("Waiting for connections...\n")

while True:
    client_socket, client_address = server_socket.accept()

    print("===================================")
    print("Connected client:", client_address)
    print("Time:", datetime.datetime.now())

    data = client_socket.recv(1024)

    if not data:
        client_socket.close()
        continue

    message = data.decode()

    print("Received message:", message)
    print("Client IP:", client_address[0])

    if message.lower() == "vaše_ime_prezime":
        response = "Unos nije podržan."
    else:
        response = message

    client_socket.send(response.encode())

    client_socket.close()