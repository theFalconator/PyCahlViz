import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    w.setWindowTitle('Patient1')
    form = Ui_MainWindow(w)
    w.show()

    sys.exit(app.exec_())
