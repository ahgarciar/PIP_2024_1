
import serial as conn

arduino = conn.Serial(port="/dev/cu.usbmodem11401", baudrate=9600, timeout=1)
print("conexion con arduino exitosa")

x = [i for i in range(10)]
y = [0 for i in range(10)]
i = 0
from matplotlib import pyplot as plt
while True:
    a = arduino.readline().decode().strip()
    y.pop(0)
    y.append(int(a))
    print(y)
    plt.plot(x, y)
    plt.grid = True
    plt.show()
