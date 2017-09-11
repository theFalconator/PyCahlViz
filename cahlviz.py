from PyQt5.QtWidgets import QApplication, QWidget
import sys, os
from Visualizer3 import Visualizer3


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('Patient1')
    form = Visualizer3(w)
    w.show()

    sys.exit(app.exec_())
