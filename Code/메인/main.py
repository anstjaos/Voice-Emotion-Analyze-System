from main_view import MainView
from main_controller import MainController
from mfcc_svm import Voice
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    voice = Voice()
    main_view = MainView(MainWindow)
    main_controller = MainController(voice, main_view)

    MainWindow.show()
    sys.exit(app.exec_())