import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P11_SliderWithTimers.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_iniciar.clicked.connect(self.iniciar)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.carrusel)

        self.lista_imagenes = [
            ":/Mascotas/gato.jpeg",
            ":/Mascotas/hamster.jpeg",
            ":/Mascotas/cuyo.jpeg",
            ":/Mascotas/conejo.jpeg",
            ":/Mascotas/perro.jpeg"
        ]

    # Área de los Slots
    def iniciar(self):
        t = self.btn_iniciar.text()
        if t == "INICIAR":
            self.btn_iniciar.setText("DETENER")
            self.idx = 0
            self.segundoPlano.start(500)
        else:
            self.btn_iniciar.setText("INICIAR")
            self.segundoPlano.stop()

    def carrusel(self):
        self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.idx]))
        self.idx = (self.idx+1)%len(self.lista_imagenes)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

