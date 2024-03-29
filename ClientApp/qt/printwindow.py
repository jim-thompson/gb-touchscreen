# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/printwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PrintWindow(object):
    def setupUi(self, PrintWindow):
        PrintWindow.setObjectName("PrintWindow")
        PrintWindow.resize(800, 480)
        PrintWindow.setMaximumSize(QtCore.QSize(800, 480))
        self.tabWidget = QtWidgets.QTabWidget(PrintWindow)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 781, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.SD = QtWidgets.QWidget()
        self.SD.setObjectName("SD")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.SD)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FileList = QtWidgets.QTableWidget(self.SD)
        self.FileList.setObjectName("FileList")
        self.FileList.setColumnCount(2)
        self.FileList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.FileList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FileList.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.FileList)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ScanSD = QtWidgets.QPushButton(self.SD)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScanSD.sizePolicy().hasHeightForWidth())
        self.ScanSD.setSizePolicy(sizePolicy)
        self.ScanSD.setMinimumSize(QtCore.QSize(100, 0))
        self.ScanSD.setMaximumSize(QtCore.QSize(100, 100))
        self.ScanSD.setObjectName("ScanSD")
        self.verticalLayout.addWidget(self.ScanSD)
        self.StartPrint = QtWidgets.QPushButton(self.SD)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartPrint.sizePolicy().hasHeightForWidth())
        self.StartPrint.setSizePolicy(sizePolicy)
        self.StartPrint.setMinimumSize(QtCore.QSize(100, 0))
        self.StartPrint.setMaximumSize(QtCore.QSize(100, 100))
        self.StartPrint.setObjectName("StartPrint")
        self.verticalLayout.addWidget(self.StartPrint)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.SD, "")
        self.USB = QtWidgets.QWidget()
        self.USB.setObjectName("USB")
        self.tabWidget.addTab(self.USB, "")
        self.widget = QtWidgets.QWidget(PrintWindow)
        self.widget.setGeometry(QtCore.QRect(10, 350, 781, 121))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Back = QtWidgets.QPushButton(self.widget)
        self.Back.setMaximumSize(QtCore.QSize(100, 100))
        self.Back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back.setIcon(icon)
        self.Back.setIconSize(QtCore.QSize(100, 100))
        self.Back.setObjectName("Back")
        self.horizontalLayout_2.addWidget(self.Back)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.StopPrint = QtWidgets.QPushButton(self.widget)
        self.StopPrint.setMinimumSize(QtCore.QSize(100, 0))
        self.StopPrint.setMaximumSize(QtCore.QSize(100, 100))
        self.StopPrint.setObjectName("StopPrint")
        self.horizontalLayout_2.addWidget(self.StopPrint)
        self.ActivePrint = QtWidgets.QPushButton(self.widget)
        self.ActivePrint.setMinimumSize(QtCore.QSize(100, 0))
        self.ActivePrint.setMaximumSize(QtCore.QSize(100, 100))
        self.ActivePrint.setObjectName("ActivePrint")
        self.horizontalLayout_2.addWidget(self.ActivePrint)

        self.retranslateUi(PrintWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PrintWindow)

    def retranslateUi(self, PrintWindow):
        _translate = QtCore.QCoreApplication.translate
        PrintWindow.setWindowTitle(_translate("PrintWindow", "ControlWindow"))
        item = self.FileList.horizontalHeaderItem(0)
        item.setText(_translate("PrintWindow", "Name"))
        item = self.FileList.horizontalHeaderItem(1)
        item.setText(_translate("PrintWindow", "Size"))
        self.ScanSD.setText(_translate("PrintWindow", "Scan SD"))
        self.StartPrint.setText(_translate("PrintWindow", "Start Print"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SD), _translate("PrintWindow", "SD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.USB), _translate("PrintWindow", "USB"))
        self.StopPrint.setText(_translate("PrintWindow", "Stop Print"))
        self.ActivePrint.setText(_translate("PrintWindow", "Active Print"))

