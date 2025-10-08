import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
server_ip = "localhost"
socket.connect(f"tcp://{server_ip}:5555")

print("Mengirim data...")

i = 0
while True:
    socket.send_string(f"Data {i}")
    print(f"Kirim: Data {i}")
    i += 1
    time.sleep(1)