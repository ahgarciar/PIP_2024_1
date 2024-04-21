from UI_to_Python import P1_Ejemplo

import sys
from PyQt5 import uic, QtWidgets, QtGui
#qtCreatorFile = "P1_Ejemplo.ui"  # Nombre del archivo aquí.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, P1_Ejemplo.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        P1_Ejemplo.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.btn_saludar

    #Area de Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

