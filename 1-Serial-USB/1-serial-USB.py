import serial
import time

com = "COM3"  # Ganti dengan port serial yang sesuai
baud = 9600 # Sesuaikan dengan baud rate
ser = serial.Serial(com, baud)
print("Mengirim data...")

i = 0
while True:
    data = i % 2 
    ser.write(f"{data}\n".encode())
    print(f"Kirim: {data}")
    i += 1
    time.sleep(1)