import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtUiTools import loadUiType
# Custom import
from app_class import *

qtObjName, qtObjClass = loadUiType('ui\\app.ui')

class MainWindow(qtObjClass):

    def __init__(self):
        qtObjClass.__init__(self)
        self.ui = qtObjName()
        self.ui.setupUi(self)

        guiFunction.uiInit(self)
        self.showMaximized()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPosition().toPoint()

    def resizeEvent(self, event):
        guiFunction.updateGrips(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon.ico"))
    w = MainWindow()

    try:
        sys.exit(app.exec())
    except Exception:
        print('Exiting')