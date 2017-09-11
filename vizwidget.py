from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene
from FrameManager import FrameManager


class VizWidget(object):
    def __init__(self, Form):
        # holds all the data
        # probably don't need a class for this
        # TODO: come up with a better solution for frame storage.
        self.frm = FrameManager('Patient1')

        Form.setObjectName("Form")
        Form.resize(500, 400)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 481, 381))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setText("Slice")
        self.horizontalLayout.addWidget(self.label)
        self.sliceSlider = QtWidgets.QSlider(self.widget)
        self.sliceSlider.setMaximum(207)
        self.sliceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sliceSlider.setObjectName("horizontalSlider")
        self.sliceSlider.valueChanged.connect(self.slice_slider_changed)
        self.horizontalLayout.addWidget(self.sliceSlider)
        self.slice_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.slice_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))

        self.slice_lineEdit.setObjectName("slice_lineEdit")
        self.slice_lineEdit.setDisabled(True)
        self.horizontalLayout.addWidget(self.slice_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Frame")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.frameSlider = QtWidgets.QSlider(self.widget)
        self.frameSlider.setMaximum(19)
        self.frameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frameSlider.setObjectName("horizontalSlider_2")
        self.frameSlider.valueChanged.connect(self.frame_slider_changed)
        self.horizontalLayout_2.addWidget(self.frameSlider)
        self.frame_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.frame_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_lineEdit.setObjectName("frame_lineEdit")
        self.frame_lineEdit.setDisabled(True)
        self.horizontalLayout_2.addWidget(self.frame_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.sliceSlider.raise_()
        self.slice_lineEdit.raise_()
        self.graphicsView.raise_()

        self.frameSlider.setValue(0)
        self.sliceSlider.setValue(0)
        self.frame_lineEdit.setText('0')
        self.slice_lineEdit.setText('0')

        pixmap = self.frm.slice_as_pixmap()
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)

        self.graphicsView.setScene(scene)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Slice"))
        self.label_2.setText(_translate("Form", "Frame"))

    def slice_slider_changed(self, value):
        # update the data structure
        self.frm.change_slice(value)
        # change the textbox for the user
        self.slice_lineEdit.setText(str(value))

        # update the pixmap
        pixmap = self.frm.slice_as_pixmap()
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.graphicsView.setScene(scene)

    def frame_slider_changed(self, value):
        # when a frame is changed we need to load in the new frame data
        # and also update the current slice to match the newly loaded frame
        self.frm.change_frame(value)
        cs = self.sliceSlider.value()
        self.frm.change_slice(cs)
        self.frame_lineEdit.setText(str(value))

        pixmap = self.frm.slice_as_pixmap()
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.graphicsView.setScene(scene)
