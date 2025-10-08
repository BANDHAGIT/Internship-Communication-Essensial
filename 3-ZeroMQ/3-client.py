import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
server_ip = "192.168.18.165"
socket.connect(f"tcp://{server_ip}:5555")

print("Mengirim data...")

i = 0
while True:
    data = i % 2
    socket.send_string(str(data))
    print(f"Kirim: {data}")
    i += 1
    time.sleep(1)