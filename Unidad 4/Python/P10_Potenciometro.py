
import serial as conn

arduino = conn.Serial(port="/dev/cu.usbmodem11401", baudrate=9600, timeout=1)
print("conexion con arduino exitosa")

while True:
    a = arduino.readline()
    a = a.decode()
    a = a.strip()
    print(a)


