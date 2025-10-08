import zmq
import socket

context = zmq.Context()
zmq_socket = context.socket(zmq.PULL) 

hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname)
print(f"Server IP: {server_ip}")

zmq_socket.bind(f"tcp://{server_ip}:5555")
print("Server siap menerima data di port 5555...")

while True:
    data = zmq_socket.recv_string()
    print(f"Terima: {data}")