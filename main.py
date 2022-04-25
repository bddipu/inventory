import sys
from PySide6 import QtWidgets, QtCore, QtGui
from openpyxl import load_workbook
from datetime import date
import sqlite3
import datetime

# Custom import
from sideGrip import SideGrip
from qssStyle import appStyle, stockViewStyle, usageStyle, receiveStyle, reviewStyle
import images
from func import *
# import resources_rc
from app import *

# qtObjName, qtObjClass = loadUiType('ui\\app.ui')

isMaximized = False

<<<<<<< HEAD
class MainWindow(QtWidgets.QMainWindow):
=======

class MainWindow(qtObjClass):
>>>>>>> main

    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        # self.ui = qtObjName()
        self.ui.setupUi(self)

        guiFunction.uiInit(self)
        self.showNormal()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPosition().toPoint()
            
    def menuItemSelected(self):
        guiFunction.decorateLeftMenu(self, self.sender())
     
    def resizeEvent(self, event):
        guiFunction.updateGrips(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(":/images/images/icon.ico"))
    w = MainWindow()

    try:
        sys.exit(app.exec())
    except Exception:
        print('Exiting')
