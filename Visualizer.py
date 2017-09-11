from FrameManager import FrameManager
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene
import os
import numpy as np


def load_patient_data(folder_name):
    """

    :param folder_name: path to folder where .RAW files are kept
    :return: list of ndarray(208,224,240)
    """
    frames = []
    path = os.getcwd() + '/' + folder_name + '/'
    print(path)
    files = []
    fr_nums = range(1, 21)
    for f in fr_nums:
        files.append(path + folder_name + '_frame' + str(f).zfill(2) + '.raw')

    for f in files:
        frame = np.fromfile(f, dtype='uint8')
        frame = np.reshape(frame, (208, 224, 240))
        frames.append(frame)

    return frames


class Visualizer(object):
    def __init__(self, Form):
        self.frm = FrameManager('Patient1')
        self.SetupUI(Form)

    def SetupUI(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 300)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graphicsView_Input = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_Input.setMaximumSize(QtCore.QSize(240, 16777215))
        self.graphicsView_Input.setObjectName("graphicsView")
        self.graphicsView_Input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_Input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.horizontalLayout_3.addWidget(self.graphicsView_Input)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.graphicsView_FFT = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_FFT.setMaximumSize(QtCore.QSize(240, 16777215))
        self.graphicsView_FFT.setObjectName("graphicsView_2")
        self.graphicsView_FFT.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_FFT.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.horizontalLayout_3.addWidget(self.graphicsView_FFT)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.graphicsView_Output = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_Output.setMaximumSize(QtCore.QSize(240, 16777215))
        self.graphicsView_Output.setObjectName("graphicsView_3")
        self.graphicsView_Output.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_Output.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.horizontalLayout_3.addWidget(self.graphicsView_Output)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.label.setText("Slice")
        self.horizontalLayout.addWidget(self.label)
        self.sliceSlider = QtWidgets.QSlider(self.layoutWidget)
        self.sliceSlider.setMaximum(207)
        self.sliceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sliceSlider.setObjectName("horizontalSlider")
        self.sliceSlider.valueChanged.connect(self.slice_slider_changed)

        self.horizontalLayout.addWidget(self.sliceSlider)
        self.lineEdit_slice = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_slice.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_slice.setObjectName("lineEdit")
        self.lineEdit_slice.setDisabled(True)
        self.horizontalLayout.addWidget(self.lineEdit_slice)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Frame")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.frameSlider = QtWidgets.QSlider(self.layoutWidget)
        self.frameSlider.setMaximum(20)
        self.frameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frameSlider.setObjectName("horizontalSlider_2")
        self.frameSlider.valueChanged.connect(self.frame_slider_changed)

        self.horizontalLayout_2.addWidget(self.frameSlider)
        self.lineEdit_frame = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_frame.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_frame.setObjectName("lineEdit_2")
        self.lineEdit_frame.setDisabled(True)
        self.horizontalLayout_2.addWidget(self.lineEdit_frame)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

    def slice_slider_changed(self, value):
        # update the data structure
        self.frm.change_slice(value)
        # change the textbox for the user
        self.lineEdit_slice.setText(str(value))

        # update the pixmap
        pixmap = self.frm.slice_as_pixmap()
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.graphicsView_Input.setScene(scene)

        fft_pixmap = self.frm.slice_fft_as_pixmap()
        fft_scene = QGraphicsScene()
        fft_scene.addPixmap(fft_pixmap)
        self.graphicsView_FFT.setScene(fft_scene)

    def frame_slider_changed(self, value):
        # when a frame is changed we need to load in the new frame data
        # and also update the current slice to match the newly loaded frame
        self.frm.change_frame(value)
        cs = self.sliceSlider.value()
        self.frm.change_slice(cs)
        self.lineEdit_frame.setText(str(value))

        pixmap = self.frm.slice_as_pixmap()
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.graphicsView_Input.setScene(scene)
