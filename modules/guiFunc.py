from PySide6 import QtWidgets, QtCore, QtGui

# Custom import
from main import MainWindow
from sideGrip import SideGrip
from qssStyle import appStyle

# Glaobal variable
isMaximized = False

class guiFunction(MainWindow):

    def maximize(self):
        global isMaximized
        if not isMaximized:
            self.showMaximized()
            isMaximized = True
            #self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
        else:
            self.showNormal()
            isMaximized = False
            #self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
 