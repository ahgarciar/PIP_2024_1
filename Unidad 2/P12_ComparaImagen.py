import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P12_ComparaImagen.ui"  # Nombre del archivo aquí.
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


        self.btn_atras.clicked.connect(self.atras)
        self.btn_siguiente.clicked.connect(self.siguiente)
        self.index_control = 0
        self.btn_atras.setEnabled(False)

        self.btn_validar.clicked.connect(self.validar)

        self.idx = 0

    # Área de los Slots
    def validar(self):
        res = self.index_control == self.idx
        msj = QtWidgets.QMessageBox()
        msj.setText(str(res))
        msj.exec_()

    def iniciar(self):
        t = self.btn_iniciar.text()
        if t == "INICIAR":
            self.btn_iniciar.setText("DETENER")
            self.idx = 0
            self.segundoPlano.start(80)
        else:
            self.btn_iniciar.setText("INICIAR")
            self.segundoPlano.stop()

    def carrusel(self):
        self.idx = (self.idx + 1) % len(self.lista_imagenes)
        self.imagenPC.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.idx]))
        print(self.idx)

    def atras(self):
        if self.index_control > 0:
            self.index_control -= 1
            self.btn_siguiente.setEnabled(True)
            ##change img
            self.imagenUsu.setPixmap(
                QtGui.QPixmap(self.lista_imagenes[self.index_control]))

        if self.index_control == 0:
             self.btn_atras.setEnabled(False)

        print(self.index_control)

    def siguiente(self):
        if self.index_control < len(self.lista_imagenes)-1:
            self.btn_atras.setEnabled(True)
            self.index_control += 1
            ##change img
            self.imagenUsu.setPixmap(
                QtGui.QPixmap(self.lista_imagenes[self.index_control]))
        if self.index_control == len(self.lista_imagenes)-1:
             self.btn_siguiente.setEnabled(False)

        print(self.index_control)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

