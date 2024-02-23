import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P8_Timers.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_iniciar_2.clicked.connect(self.iniciar2)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.contar)

    # Área de los Slots
    def iniciar(self):
        import time as t
        n = int(self.txt_numero.text())
        print(n)
        for i in range(n):
            self.txt_contador.setText((str)(i+1))
            t.sleep(0.5)
            print(i+1)

    def iniciar2(self):
        self.num = int(self.txt_numero_2.text())
        print(self.num)
        self.segundoPlano.start(500)
        self.cont = 1
        self.txt_contador_2.setText("1")
       
    def contar(self):
        if self.cont < self.num:
            self.cont += 1
            self.txt_contador_2.setText(str(self.cont))
        else:
            self.segundoPlano.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

