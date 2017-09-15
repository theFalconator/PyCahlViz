import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene

from util import load_frame, ndarray2pixmap


class Visualizer3(object):
    def __init__(self, Form):
        self.frames = []
        for i in range(1, 20):
            self.frames.append(load_frame('Patient1', i))

        # keep track of what frame is being displayed
        self.frame = self.frames[0]

        # initialize ndarrays for views with zeros
        self.top = np.zeros((224, 240), dtype='uint8')
        self.front = np.zeros((208, 240), dtype='uint8')
        self.side = np.zeros((208, 224), dtype='uint8')

        self.setup_ui(Form)

        # finish "setting up" the ui with some default values for sliders
        # so that images load on launch not after user input
        self.frameSlider.setValue(1)
        self.frontSliceSlider.setValue(100)
        self.topSliceSlider.setValue(100)
        self.sideSliceSlider.setValue(100)

    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(830, 300)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 802, 286))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topView = QtWidgets.QGraphicsView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topView.sizePolicy().hasHeightForWidth())
        self.topView.setSizePolicy(sizePolicy)
        self.topView.setMaximumSize(QtCore.QSize(224, 240))
        self.topView.setObjectName("topView")
        self.topView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.topView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.verticalLayout_2.addWidget(self.topView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.topSliceSlider = QtWidgets.QSlider(self.layoutWidget)
        self.topSliceSlider.setMaximum(207)
        self.topSliceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.topSliceSlider.setObjectName("topSliceSlider")
        self.horizontalLayout_4.addWidget(self.topSliceSlider)
        self.topSliceLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.topSliceLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topSliceLineEdit.sizePolicy().hasHeightForWidth())
        self.topSliceLineEdit.setSizePolicy(sizePolicy)
        self.topSliceLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.topSliceLineEdit.setReadOnly(False)
        self.topSliceLineEdit.setObjectName("topSliceLineEdit")
        self.horizontalLayout_4.addWidget(self.topSliceLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frontView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.frontView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.frontView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frontView.sizePolicy().hasHeightForWidth())
        self.frontView.setSizePolicy(sizePolicy)
        self.frontView.setMaximumSize(QtCore.QSize(224, 240))
        self.frontView.setObjectName("frontView")
        self.verticalLayout_3.addWidget(self.frontView)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frontSliceSlider = QtWidgets.QSlider(self.layoutWidget)
        self.frontSliceSlider.setMaximum(207)
        self.frontSliceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frontSliceSlider.setObjectName("frontSliceSlider")
        self.horizontalLayout_5.addWidget(self.frontSliceSlider)
        self.frontSliceLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.frontSliceLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frontSliceLineEdit.sizePolicy().hasHeightForWidth())
        self.frontSliceLineEdit.setSizePolicy(sizePolicy)
        self.frontSliceLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frontSliceLineEdit.setReadOnly(False)
        self.frontSliceLineEdit.setObjectName("frontSliceLineEdit")
        self.horizontalLayout_5.addWidget(self.frontSliceLineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sideView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.sideView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sideView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sideView.sizePolicy().hasHeightForWidth())
        self.sideView.setSizePolicy(sizePolicy)
        self.sideView.setMaximumSize(QtCore.QSize(224, 240))
        self.sideView.setObjectName("sideView")
        self.verticalLayout_4.addWidget(self.sideView)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sideSliceSlider = QtWidgets.QSlider(self.layoutWidget)
        self.sideSliceSlider.setMaximum(207)
        self.sideSliceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sideSliceSlider.setObjectName("sideSliceSlider")

        self.horizontalLayout_6.addWidget(self.sideSliceSlider)
        self.sideSliceLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.sideSliceLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sideSliceLineEdit.sizePolicy().hasHeightForWidth())
        self.sideSliceLineEdit.setSizePolicy(sizePolicy)
        self.sideSliceLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.sideSliceLineEdit.setReadOnly(False)
        self.sideSliceLineEdit.setObjectName("sideSliceLineEdit")
        self.horizontalLayout_6.addWidget(self.sideSliceLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.frameSlider = QtWidgets.QSlider(self.layoutWidget)
        self.frameSlider.setMaximum(19)
        self.frameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frameSlider.setObjectName("frameSlider")
        self.horizontalLayout_2.addWidget(self.frameSlider)
        self.frameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.frameLineEdit.setEnabled(False)
        self.frameLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameLineEdit.setObjectName("frameLineEdit")
        self.horizontalLayout_2.addWidget(self.frameLineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.topSliceSlider.valueChanged.connect(self.top_slider_changed)
        self.frontSliceSlider.valueChanged.connect(self.front_slider_changed)
        self.sideSliceSlider.valueChanged.connect(self.side_slider_changed)

        self.frameSlider.valueChanged.connect(self.frame_slider_changed)

    def top_slider_changed(self, value):
        self.top = self.frame[value, :, :].copy()
        self.topSliceLineEdit.setText(str(value))
        p = ndarray2pixmap(self.top)
        scene = QGraphicsScene()
        scene.addPixmap(p)
        self.topView.setScene(scene)

    def front_slider_changed(self, value):
        self.front = self.frame[:, value, :].copy()
        self.frontSliceLineEdit.setText(str(value))
        p = ndarray2pixmap(self.front)
        scene = QGraphicsScene()
        scene.addPixmap(p)
        self.frontView.setScene(scene)

    def side_slider_changed(self, value):
        self.side = self.frame[:, :, value].copy()
        self.sideSliceLineEdit.setText(str(value))
        p = ndarray2pixmap(self.side)
        scene = QGraphicsScene()
        scene.addPixmap(p)
        self.sideView.setScene(scene)

    def frame_slider_changed(self, value):
        self.frame = self.frames[value - 1]

        self.frameLineEdit.setText(str(value))

        t = self.topSliceSlider.value()
        f = self.frontSliceSlider.value()
        s = self.sideSliceSlider.value()

        self.top = self.frame[t, :, :].copy()
        self.front = self.frame[:, f, :].copy()
        self.side = self.frame[:, :, s].copy()
        p_top = ndarray2pixmap(self.top)
        p_front = ndarray2pixmap(self.front)
        p_side = ndarray2pixmap(self.side)

        scene_top = QGraphicsScene()
        scene_front = QGraphicsScene()
        scene_side = QGraphicsScene()

        scene_top.addPixmap(p_top)
        scene_front.addPixmap(p_front)
        scene_side.addPixmap(p_side)

        self.topView.setScene(scene_top)
        self.frontView.setScene(scene_front)
        self.sideView.setScene(scene_side)
