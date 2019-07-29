# This Python file uses the following encoding: utf-8
import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
#from dashboardwindow import *
from dashboardwindowFRAMETEST import *
from module_gigabot import *
from addmachine import *
from Server.server_main import serverhandler
from Server.gigabotclient import *
import time

#   Server Thread used to handle the blocking server call, listen_for_clients()
#   This Thread spawns other Threads for each Client connected.
class server_thread(QtCore.QThread):
    def __init__(self, handler, parent = None):
        QtCore.QThread.__init__(self,parent)
        self.handler= handler
    def run(self):
        while(True):
            self.handler.listen_for_clients()

#   View Thread, that updates the view whenever new data comes in from the server side.
class view_thread(QtCore.QThread):
    def __init__(self, serv_handler, dashboard, parent=None):
        QtCore.QThread.__init__(self,parent)
        self.dashboard = dashboard
        self.serv_handler = serv_handler
    def run(self):
        while(True):
#            if len(self.serv_handler.gigabotthreads):
#                serv_handler.message = self.serv_handler.gigabotthreads[0].printstuff
#                self.serv_handler.gigabotthreads[0].printstuff = ""
#            if self.serv_handler.message != "":
#                self.view.refresh_text_box(self.serv_handler.message)
#                self.serv_handler.message = ""
                
            #else: self.view.refresh_text_box("ping")
            for g in self.dashboard.modules:
                g.update()
            QtWidgets.QApplication.processEvents()
            time.sleep(0.5)



#   Gigabot Modules Class
#   Initalize gigabotmodule
class GigabotModule(QtWidgets.QWidget , Ui_GigabotModule):
    def __init__(self, gigabot):
        super(GigabotModule,self).__init__()
        self.setupUi(self)
        self.gigabot = gigabot
        self.GigabotNum.setText(gigabot.idnum)
        self.update()
    def update(self):
        self.Nozzle1Text.setText(str(self.gigabot.temp1))
        self.Nozzle2Text.setText(str(self.gigabot.temp2))
        self.BedText.setText(str(self.gigabot.btemp))

#    def mousePressEvent(self, event):
#        self.__mousePressPos = None
#        self.__mouseMovePos = None
#        if event.button() == QtCore.Qt.LeftButton:
#            self.__mousePressPos = event.globalPos()
#            self.__mouseMovePos = event.globalPos()
#        super(GigabotModule, self).mousePressEvent(event)


class AddMachineWindow(QtWidgets.QWidget, Ui_addmachine):
#   Pass in the list of gigabotclient objects that contain data on gigabot.
    def __init__(self, gigabots, mainwin):
        super(AddMachineWindow, self).__init__()
        self.setupUi(self)
        self.main = mainwin
        self.gigabots = gigabots
#       Move Window to Middle of Screen
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
#       Make the selection Behavior as selecting the entire row
        self.Devices.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
#       Hide the vertical header which contains the Index of the row.
        self.Devices.verticalHeader().hide()
#       Stretch out the horizontal header to take up the entire view
        header = self.Devices.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        rowpos = self.Devices.rowCount()

        self.gigabots.append(gigabotclient("192.168.1.169"))
#        self.gigabots.append(gigabotclient("192.168.1.151"))
#        self.gigabots.append(gigabotclient("192.168.1.49"))
#        self.gigabots.append(gigabotclient("192.168.1.12"))

        if len(gigabots)>0:
            for g in self.gigabots:
                rowpos = self.Devices.rowCount()
                self.Devices.insertRow(rowpos)
                item = QtWidgets.QTableWidgetItem(g.ipaddress)
                #item.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                item.setFlags( Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.Devices.setItem(rowpos, 0, item)

#       Connect the ok button to retrieving the gigabot.
        ok = self.Button.button(QtWidgets.QDialogButtonBox.Ok)
        ok.clicked.connect(self.add)
#       Connecting the Quit Button to quiting.
        close = self.Button.button(QtWidgets.QDialogButtonBox.Cancel)
        close.clicked.connect(self.close)

    def add(self):
        selected = self.Devices.currentRow()
        gigabotnum = self.Devices.item(selected,1)
        if gigabotnum and len(gigabotnum.text()) != 0: self.gigabots[selected].idnum= gigabotnum.text()

        self.main.addModule(self.gigabots[selected])
        self.close()



#   MainWindow class
class MainWindow(QtWidgets.QMainWindow, Ui_DashboardWindow):
    def __init__(self, handler):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.modules = []
#       Set the Dashboard as a MainWindow Object so a DockWidget can be nested inside.
        self.Dashboard = QtWidgets.QMainWindow()
        self.Dashboard.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks)
#       Set the sizePolicy so that the application is responsive
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dashboard.sizePolicy().hasHeightForWidth())
        self.Dashboard.setSizePolicy(sizePolicy)
#       Add the MainWindow to the grid layout.
        self.gridLayout.addWidget(self.Dashboard, 1, 0, 1, 1)


        self.handler = handler
#       Determine the size of the window
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        wid = sizeObject.width()
        hei = sizeObject.height()
        self.resize( wid-100, hei-100)
        self.showMaximized()
#       AddModule function connected to the Addmachine menu Option.
        self.AddMachine.triggered.connect(self.add_machine)
        self.Quit.clicked.connect(self.closeall)

    def closeall(self):
        self.handler.quit()
        #send all data to database
        self.close()

    def add_machine(self):
        self.pop =AddMachineWindow(self.handler.gigabots, self)
        self.pop.show()

    def addModule(self, gigabot):
        #self.Dashboard.removeWidget(self.Null)
        mod = GigabotModule(gigabot)
        wid = QtWidgets.QDockWidget(self)
        wid.setWidget(mod)

        wid.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
        #self.wid.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable | QtWidgets.QDockWidget.DockWidgetClosable)
        #self.wid.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
        wid.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)
        #wid[i].setWindowFlags(Qt.FramelessWindowHint)
        wid.setAttribute(Qt.WA_TranslucentBackground)
        self.Dashboard.addDockWidget(Qt.RightDockWidgetArea,wid)
        wid.setFloating(True)
        self.modules.append(wid)



    def refresh_text_box(self, astring):
#        self.Serveroutput.append(astring)
        QtWidgets.QApplication.processEvents()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

#   Start Server Handler
    serv_handler = serverhandler()

#   Main Dashboard Window
    dashboardwindow = MainWindow(serv_handler)


    serv_thread = server_thread(serv_handler)
    view_thread = view_thread(serv_handler, dashboardwindow)

    serv_thread.start()
    view_thread.start()

    dashboardwindow.show()

    app.exec_()
    #sys.exit(app.exec_())


    #        mods = []
    #        dockwids = []
    #        for i in range(6):
    #            mods.append(GigabotModule(str(i)))
    #            dockwids.append(QtWidgets.QDockWidget(self))
    #        for i in range(6):
    #            dockwids[i].setWidget(mods[i])
    #            dockwids[i].setFeatures(QtWidgets.QDockWidget.DockWidgetMovable | QtWidgets.QDockWidget.DockWidgetClosable)
    #            dockwids[i].setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
    #            #dockwids[i].setWindowFlags(Qt.FramelessWindowHint)
    #            dockwids[i].setAttribute(Qt.WA_TranslucentBackground)
    #            dockwids[i].setFloating(True)
    #        for i in range(6):
    #            self.Dashboard.addDockWidget(Qt.NoDockWidgetArea,dockwids[i])
