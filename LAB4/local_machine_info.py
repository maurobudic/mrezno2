import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)

    print("=== Local Machine Info ===")
    print(f"Host name: {host_name}")
    print(f"IP address: {ip_address}")
    print("==========================")