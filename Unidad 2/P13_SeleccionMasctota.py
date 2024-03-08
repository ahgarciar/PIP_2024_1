import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P13_SeleccionMascota.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rb_Gato.clicked.connect(self.clic_gato)
        self.rb_Gato.toggled.connect(self.toggle_gato)

    # Área de los Slots
    def clic_gato(self):
        print("Hiciste clic al gato")

    def toggle_gato(self):
        estado = self.rb_Gato.isChecked()
        print(f"El gato cambio de estado (toggle). Nuevo Estado: {estado}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

