import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P3_ComboBox.ui"  # Nombre del archivo aquí.
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

        self.combo_mascotas.addItem("Selecciona...", 0)
        self.combo_mascotas.addItem("Hamster", 1)
        self.combo_mascotas.addItem("Gato", 2)
        self.combo_mascotas.addItem("Cuyo", 3)
        self.combo_mascotas.addItem("Perro", 4)
        self.combo_mascotas.addItem("Conejo", 5)

        self.combo_mascotas.currentIndexChanged.connect(self.cambia)

    def cambia(self):
        print("Text: " + self.combo_mascotas.currentText())
        print("Index: " + str(self.combo_mascotas.currentIndex()))
        print("Data: " + str(self.combo_mascotas.currentData()))

        dataClave = self.combo_mascotas.currentData()
        imagen = self.datos_mascotas[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))


    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

