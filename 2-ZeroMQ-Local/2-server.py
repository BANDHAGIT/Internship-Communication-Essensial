import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind(f"tcp://*:5555")

print("Server siap menerima data di port 5555...")

while True:
    data = socket.recv_string()
    print(f"Terima: {data}")