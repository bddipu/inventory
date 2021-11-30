from PySide6 import QtWidgets, QtCore, QtGui

class SideGrip(QtWidgets.QWidget):
    
    def __init__(self, parent, edge):
        QtWidgets.QWidget.__init__(self)
        self.parent = parent
        self.setParent(parent)
        self.gripFrame = gripFrame()

        if edge == QtCore.Qt.LeftEdge:
            self.gripFrame.left(self)
            self.setGeometry(0, 10, 10, self.parent.height())
            self.setMaximumWidth(10)
            self.gripFrame.gripLeft.mouseMoveEvent = self.resizeLeft
        
        elif edge == QtCore.Qt.TopEdge:
            self.gripFrame.top(self)
            self.setGeometry(0, 0, self.parent.width(), 10)
            self.setMaximumHeight(10)
            self.top_Left = QtWidgets.QSizeGrip(self.gripFrame.topLeft)
            self.top_Right = QtWidgets.QSizeGrip(self.gripFrame.topRight)
            self.gripFrame.gripTop.mouseMoveEvent = self.resizeTop
        
        elif edge == QtCore.Qt.RightEdge:
            self.gripFrame.right(self)
            self.setGeometry(self.parent.width() - 10, 10, 10, self.parent.height())
            self.setMaximumWidth(10)
            self.gripFrame.gripRight.mouseMoveEvent = self.resizeRight
        
        else:
            self.gripFrame.bottom(self)
            self.setGeometry(0, self.parent.height() - 10, self.parent.width(), 10)
            self.setMaximumHeight(10)
            self.bottom_Left = QtWidgets.QSizeGrip(self.gripFrame.bottomLeft)
            self.bottom_Right = QtWidgets.QSizeGrip(self.gripFrame.bottomRight)
            self.gripFrame.gripBottom.mouseMoveEvent = self.resizeBottom

    def resizeLeft(self, delta):
        window = self.parent
        width = max(window.minimumWidth(), window.width() - delta.x())
        geo = window.geometry()
        geo.setLeft(geo.right() - width)
        window.setGeometry(geo)

    def resizeTop(self, delta):
        window = self.parent
        height = max(window.minimumHeight(), window.height() - delta.y())
        geo = window.geometry()
        geo.setTop(geo.bottom() - height)
        window.setGeometry(geo)

    def resizeRight(self, delta):
        window = self.parent
        width = max(window.minimumWidth(), window.width() + delta.x())
        window.resize(width, window.height())

    def resizeBottom(self, delta):
        window = self.parent
        height = max(window.minimumHeight(), window.height() + delta.y())
        window.resize(window.width(), height)

    def resizeEvent(self, event):
        if hasattr(self.gripFrame, 'gripTop'):
            self.gripFrame.gripTop.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.gripFrame, 'gripBottom'):
            self.gripFrame.gripBottom.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.gripFrame, 'gripLeft'):
            self.gripFrame.gripLeft.setGeometry(0, 0, 10, self.height() - 20)

        elif hasattr(self.gripFrame, 'gripRight'):
            self.gripFrame.gripRight.setGeometry(0, 0, 10, self.height() - 20)
 
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mousePos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mousePos is not None:
            delta = event.pos() - self.mousePos
            self.resizeFunc(delta)

    def mouseReleaseEvent(self, event):
        self.mousePos = None


class gripFrame(object):

    def top(self, frame):
        if not frame.objectName():
            frame.setObjectName(u"frame")
        self.gripTop = QtWidgets.QFrame(frame)
        self.gripTop.setObjectName(u"gripTop")
        self.gripTop.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.gripTop.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.topLeft = QtWidgets.QFrame(self.gripTop)
        self.topLeft.setObjectName(u"topLeft")
        self.topLeft.setMinimumSize(QtCore.QSize(10, 10))
        self.topLeft.setMaximumSize(QtCore.QSize(10, 10))
        self.topLeft.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
        self.topLeft.setStyleSheet(u"background-color: transparent;")
        self.topLeft.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.topMiddle = QtWidgets.QFrame(self.gripTop)
        self.topMiddle.setObjectName(u"topMiddle")
        self.topMiddle.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.topMiddle.setStyleSheet(u"background-color: transparent;")
        self.topMiddle.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.topRight = QtWidgets.QFrame(self.gripTop)
        self.topRight.setObjectName(u"topRight")
        self.topRight.setMinimumSize(QtCore.QSize(10, 10))
        self.topRight.setMaximumSize(QtCore.QSize(10, 10))
        self.topRight.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))
        self.topRight.setStyleSheet(u"background-color: transparent;")
        self.topRight.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.topLayout = QtWidgets.QHBoxLayout(self.gripTop)
        self.topLayout.setObjectName(u"topLayout")
        self.topLayout.setSpacing(0)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.addWidget(self.topLeft)
        self.topLayout.addWidget(self.topMiddle)
        self.topLayout.addWidget(self.topRight)

    def bottom(self, frame):
        if not frame.objectName():
            frame.setObjectName(u"frame")
        self.gripBottom = QtWidgets.QFrame(frame)
        self.gripBottom.setObjectName(u"gripBottom")
        self.gripBottom.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.gripBottom.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.bottomLeft = QtWidgets.QFrame(self.gripBottom)
        self.bottomLeft.setObjectName(u"bottomLeft")
        self.bottomLeft.setMinimumSize(QtCore.QSize(10, 10))
        self.bottomLeft.setMaximumSize(QtCore.QSize(10, 10))
        self.bottomLeft.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))
        self.bottomLeft.setStyleSheet(u"background-color: transparent;")
        self.bottomLeft.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.bottomMiddle = QtWidgets.QFrame(self.gripBottom)
        self.bottomMiddle.setObjectName(u"bottomMiddle")
        self.bottomMiddle.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.bottomMiddle.setStyleSheet(u"background-color: transparent;")
        self.bottomMiddle.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.bottomRight = QtWidgets.QFrame(self.gripBottom)
        self.bottomRight.setObjectName(u"bottomRight")
        self.bottomRight.setMinimumSize(QtCore.QSize(10, 10))
        self.bottomRight.setMaximumSize(QtCore.QSize(10, 10))
        self.bottomRight.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
        self.bottomRight.setStyleSheet(u"background-color: transparent;")
        self.bottomRight.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.bottomLayout = QtWidgets.QHBoxLayout(self.gripBottom)
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.bottomLayout.setSpacing(0)
        self.bottomLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomLayout.addWidget(self.bottomLeft)
        self.bottomLayout.addWidget(self.bottomMiddle)
        self.bottomLayout.addWidget(self.bottomRight)

    def left(self, frame):
        if not frame.objectName():
            frame.setObjectName(u"frame")
        self.gripLeft = QtWidgets.QFrame(frame)
        self.gripLeft.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.gripLeft.setStyleSheet(u"background-color: transparent;")
        self.gripLeft.setFrameShape(QtWidgets.QFrame.NoFrame)

    def right(self, frame):
        if not frame.objectName():
            frame.setObjectName(u"frame")
        self.gripRight = QtWidgets.QFrame(frame)
        self.gripRight.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.gripRight.setStyleSheet(u"background-color: transparent;")
        self.gripRight.setFrameShape(QtWidgets.QFrame.NoFrame)