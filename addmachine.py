from qt.addmachinewindow import *
from Server.gigabotclient import *
from PySide2.QtCore import Qt


#   AddMachineWindow implemented the QtDesigner generated class, Ui_addmachine
class AddMachineWindow(QtWidgets.QWidget, Ui_addmachine):
#   Pass in the list of gigabotclient objects that contain data on gigabot.
    def __init__(self, gigabots, parent = None):
        super(AddMachineWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.Tool)
        
        self.main = parent
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

#       Populate the Qtable with the avalible gigabots. 
        self.refreshtable()

#       Connect the ok button to retrieving the gigabot.
        ok = self.Button.button(QtWidgets.QDialogButtonBox.Ok)
        ok.clicked.connect(self.addmod)
#       Connecting the Quit Button to quiting.
        close = self.Button.button(QtWidgets.QDialogButtonBox.Cancel)
        close.clicked.connect(self.close)
        self.Refresh.clicked.connect(self.refreshtable)

    def refreshtable(self):
        self.Devices.setRowCount(0)
        if len(self.gigabots)>0:
            for g in self.gigabots:
                rowpos = self.Devices.rowCount()
                self.Devices.insertRow(rowpos)
                item = QtWidgets.QTableWidgetItem(g.ipaddress)
                #item.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                item.setFlags( Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.Devices.setItem(rowpos, 0, item)
    def addmod(self):
        if(len(self.gigabots) >0):
            selected = self.Devices.currentRow()
            gigabotnum = self.Devices.item(selected,1)
            if gigabotnum and len(gigabotnum.text()) != 0: self.gigabots[selected].idnum= gigabotnum.text()
            self.main.addModule(self.gigabots[selected])
        self.close()
