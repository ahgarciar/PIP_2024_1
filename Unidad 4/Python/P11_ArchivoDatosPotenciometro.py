
import serial as conn

arduino = conn.Serial(port="/dev/cu.usbmodem11401", baudrate=9600, timeout=1)
print("conexion con arduino exitosa")

archivo = open("../Archivos/dato_potenciometro.csv","w")
i = 0
while i < 10:
    a = arduino.readline()
    a = a.decode()
    a = a.strip()
    print(a)
    archivo.write(a + "\n")
    i += 1
archivo.flush()
archivo.close()


