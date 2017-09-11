import sys
import os
import numpy as np
from PyQt5.QtGui import QImage, QPixmap


class FrameManager:
    def __init__(self, folder_name):
        """
        Constructor.
        :param folder_name: Path to folder where .RAW images are kept.
        """

        # TODO: test using higher dimensional ndarray instead of list of ndarrays.
        self.frames = []
        self.frame = np.zeros((208, 224, 240), dtype='uint8')
        self.slice = np.zeros((224, 240), dtype='uint8')
        self.slice_fft = np.zeros((224, 240), dtype='uint8')

        path = os.getcwd() + '/' + folder_name + '/'
        print(path)
        files = []
        fr_nums = range(1, 21)
        for f in fr_nums:
            files.append(path + folder_name + '_frame' + str(f).zfill(2) + '.raw')

        for f in files:
            frame = np.fromfile(f, dtype='uint8')
            frame = np.reshape(frame, (208, 224, 240))
            self.frames.append(frame)

        self.frame = self.frames[0]

    def change_frame(self, value):
        """
        Changes the internal frame data that the class supplies to the outside world.
        :param value: Index of the frame
        :return: Nothing. Internal data is changed only.
        """
        try:
            self.frame = self.frames[value]
        except IndexError:
            self.frame = self.frames[0]
            print("There are only {} frames.".format(len(self.frames)))

    def change_slice(self, value):
        """
        Changes the internal slice data that the class supplies to the outside world.
        :param value:  Index of the slice
        :return: Nothing. Internal data is changed only.
        """
        try:
            self.slice = self.frame[value, :, :]
            self.slice_fft = np.fft.fft2(self.slice)
            fshit=np.fft.fftshift(self.slice_fft)
            mag=20*np.log(np.abs(fshit))
            self.slice_fft = mag

        except IndexError:
            self.slice = self.frame[0, :, :]
            self.slice_fft = np.zeros((224, 240), dtype='uint8')
            print("There are only 208 slices in this frame.")

    def slice_as_pixmap(self):
        """
        Converts the current slice of type np.ndarray((224,240), dtype='uint8') to a QPixmap
        :return: A QPixmap equivalent of the ndarray.
        """
        # https://stackoverflow.com/questions/34232632/convert-python-opencv-image-numpy-array-to-pyqt-qpixmap-image
        height, width = self.slice.shape
        bytesPerLine = 1 * width
        qImg = QImage(self.slice.data, width, height, bytesPerLine, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qImg)
        return pixmap

    def slice_fft_as_pixmap(self):
        height, width = self.slice_fft.shape
        bytesPerLine = 1 * width
        qImg = QImage(self.slice_fft.data, width, height, bytesPerLine, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qImg)
        return pixmap
