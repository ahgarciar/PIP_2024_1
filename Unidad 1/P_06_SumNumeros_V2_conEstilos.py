import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_06_SumNumeros_V2_ConEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.txt_resultado.setEnabled(False)

    # Área de los Slots
    def sumar(self):
        ##el usuario ingresara los numeros separados por espacios...
        numeros = self.txt_numeros.text() #entrada ejemplo : 5 6 7 8 9
        lista = numeros.split(" ") #convierte la entra de numeros en una lista  Ejemplo ['1', '2', '4', '53']
        print(lista)
        lista_en_numeros = [int(i) for i in lista] #conversion de los caracteres a nums, por lista de comprension
        print(lista_en_numeros)

        suma = sum(lista_en_numeros)

        self.txt_resultado.setText(str(suma))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

