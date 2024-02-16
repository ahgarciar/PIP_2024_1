import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P1_DescripcionImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_mascotas = {
            1:["Hamster", "Comer", 1, "a+", ":/Mascotas/hamster.jpeg"],
            2: ["Gato", "Cazar", 3, "b+", ":/Mascotas/gato.jpeg"],
            3: ["Cuyo", "Jugar", 2, "c+",":/Mascotas/cuyo.jpeg"],
            4: ["Perro", "Ladrar", 10, "d+",":/Mascotas/perro.jpeg"],
            5: ["Conejo", "Saltar", 1, "e+",":/Mascotas/conejo.jpeg"]
        }

        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)

        self.index_control = 0

        self.btn_atras.setEnabled(False)

    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            datos = self.datos_mascotas[self.index_control]
            print(datos)
            self.btn_adelante.setEnabled(True)
            ##change img
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))

        if self.index_control == 1:
             self.btn_atras.setEnabled(False)

    def adelante(self):
        if self.index_control < 5:
            self.btn_atras.setEnabled(True)
            self.index_control += 1
            datos = self.datos_mascotas[self.index_control]
            print(datos)
            ##change img
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
        if self.index_control == 5:
             self.btn_adelante.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

