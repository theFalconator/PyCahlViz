import os
import numpy as np
from PyQt5.QtGui import QImage, QPixmap


def load_frame(folder, n):
    path = os.getcwd()
    path += "/" + folder + "/" + folder + "_frame" + str(n).zfill(2) + ".raw"

    frame = np.fromfile(path, dtype='uint8')
    frame = np.reshape(frame, (208, 224, 240))
    return frame


def ndarray2pixmap(ndarray):
    height, width = ndarray.shape
    bytesPerLine = 1 * width
    qImg = QImage(ndarray.data, width, height, bytesPerLine, QImage.Format_Grayscale8)
    pixmap = QPixmap.fromImage(qImg)
    return pixmap