import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P7_CambiarColor.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.valorR.setMinimum(0)
        self.valorR.setMaximum(255)
        self.valorR.setSingleStep(1)
        self.valorR.setValue(0)
        self.valorR.valueChanged.connect(self.cambiaR)

        self.valorG.setMinimum(0)
        self.valorG.setMaximum(255)
        self.valorG.setSingleStep(1)
        self.valorG.setValue(0)
        self.valorG.valueChanged.connect(self.cambiaG)

        self.valorB.setMinimum(0)
        self.valorB.setMaximum(255)
        self.valorB.setSingleStep(1)
        self.valorB.setValue(0)
        self.valorB.valueChanged.connect(self.cambiaB)

        self.R = 0
        self.G = 0
        self.B = 0

    # Área de los Slots
    def cambiaR(self):
        self.R = self.valorR.value()
        estilo = ("background-color: rgb(" + str(self.R) +
                  "," + str(self.G) + "," + str(self.B) + ");")
        self.colorburguer.setStyleSheet(estilo)


    def cambiaG(self):
        self.G = self.valorG.value()
        estilo = ("background-color: rgb(" + str(self.R) +
                  "," + str(self.G) + "," + str(self.B) + ");")
        self.colorburguer.setStyleSheet(estilo)

    def cambiaB(self):
        self.B = self.valorB.value()
        estilo = ("background-color: rgb("+ str(self.R) +
                  "," + str(self.G) + "," + str(self.B) + ");")
        self.colorburguer.setStyleSheet(estilo)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

