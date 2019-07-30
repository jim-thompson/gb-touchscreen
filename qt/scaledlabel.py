from PySide2 import QtCore, QtGui, QtWidgets

class ScaledLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self)
        
    def setpix(self):
        self._pixmap = QtGui.QPixmap(self.pixmap())

    def resizeEvent(self, event):
        self.setPixmap(self._pixmap.scaled(self.width(), self.height(),QtCore.Qt.KeepAspectRatio))
    
    def changepix(self, file):
        self.setPixmap(QtGui.QPixmap(file))
        self.setpix()