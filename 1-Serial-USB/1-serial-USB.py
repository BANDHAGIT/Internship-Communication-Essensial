import serial
import time

com = "COM3"  # Ganti dengan port serial yang sesuai
port = 9600
ser = serial.Serial(com, port)
print("Mengirim data...")

i = 0
while True:
    ser.write(f"Data {i}\n".encode())
    print(f"Kirim: Data {i}")
    i += 1
    time.sleep(1)