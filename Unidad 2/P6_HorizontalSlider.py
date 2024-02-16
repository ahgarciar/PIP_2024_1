import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P6_HorizontalSlider.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_mascotas = {
            1: ["Hamster", "Comer", 1, "a+", ":/Mascotas/hamster.jpeg"],
            2: ["Gato", "Cazar", 3, "b+", ":/Mascotas/gato.jpeg"],
            3: ["Cuyo", "Jugar", 2, "c+", ":/Mascotas/cuyo.jpeg"],
            4: ["Perro", "Ladrar", 10, "d+", ":/Mascotas/perro.jpeg"],
            5: ["Conejo", "Saltar", 1, "e+", ":/Mascotas/conejo.jpeg"]
        }

        self.hs_mascotas.setMinimum(1)
        self.hs_mascotas.setMaximum(5)
        self.hs_mascotas.setSingleStep(1)
        self.hs_mascotas.setValue(1)
        self.hs_mascotas.valueChanged.connect(self.cambia)

    def cambia(self):
        dataClave = self.hs_mascotas.value()
        print(dataClave)
        imagen = self.datos_mascotas[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))


    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

