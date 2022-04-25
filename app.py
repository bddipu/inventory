# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appJOsRNJ.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(993, 548)
        self.widget_app = QWidget(MainWindow)
        self.widget_app.setObjectName(u"widget_app")
        self.widget_app.setMinimumSize(QSize(950, 500))
        self.gridLayout_3 = QGridLayout(self.widget_app)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_app = QFrame(self.widget_app)
        self.frame_app.setObjectName(u"frame_app")
        self.frame_app.setStyleSheet(u"")
        self.frame_app.setFrameShape(QFrame.StyledPanel)
        self.frame_app.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_app)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_titleBar = QFrame(self.frame_app)
        self.frame_titleBar.setObjectName(u"frame_titleBar")
        self.frame_titleBar.setMinimumSize(QSize(0, 40))
        self.frame_titleBar.setMaximumSize(QSize(16777215, 40))
        self.frame_titleBar.setStyleSheet(u"")
        self.frame_titleBar.setFrameShape(QFrame.StyledPanel)
        self.frame_titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_titleBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_appLogo = QFrame(self.frame_titleBar)
        self.frame_appLogo.setObjectName(u"frame_appLogo")
        self.frame_appLogo.setMinimumSize(QSize(50, 40))
        self.frame_appLogo.setMaximumSize(QSize(50, 40))
        self.frame_appLogo.setFrameShape(QFrame.NoFrame)
        self.frame_appLogo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_appLogo)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.btn_appLogo = QPushButton(self.frame_appLogo)
        self.btn_appLogo.setObjectName(u"btn_appLogo")
        self.btn_appLogo.setEnabled(True)
        self.btn_appLogo.setMinimumSize(QSize(45, 40))
        self.btn_appLogo.setMaximumSize(QSize(45, 40))
        font = QFont()
        font.setPointSize(12)
        self.btn_appLogo.setFont(font)
        self.btn_appLogo.setFocusPolicy(Qt.NoFocus)
#if QT_CONFIG(statustip)
        self.btn_appLogo.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.btn_appLogo.setStyleSheet(u"")
        self.btn_appLogo.setIconSize(QSize(24, 24))
        self.btn_appLogo.setFlat(False)

        self.verticalLayout_3.addWidget(self.btn_appLogo)


        self.horizontalLayout.addWidget(self.frame_appLogo)

        self.frame_appTitle = QFrame(self.frame_titleBar)
        self.frame_appTitle.setObjectName(u"frame_appTitle")
        self.frame_appTitle.setMinimumSize(QSize(0, 40))
        self.frame_appTitle.setMaximumSize(QSize(16777215, 40))
        self.frame_appTitle.setFrameShape(QFrame.NoFrame)
        self.frame_appTitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_appTitle)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 0, 0, 0)
        self.label_appTitle = QLabel(self.frame_appTitle)
        self.label_appTitle.setObjectName(u"label_appTitle")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_appTitle.setFont(font1)
        self.label_appTitle.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.label_appTitle)


        self.horizontalLayout.addWidget(self.frame_appTitle)

        self.frame_appTitleBtn = QFrame(self.frame_titleBar)
        self.frame_appTitleBtn.setObjectName(u"frame_appTitleBtn")
        self.frame_appTitleBtn.setMinimumSize(QSize(110, 40))
        self.frame_appTitleBtn.setMaximumSize(QSize(110, 40))
        self.frame_appTitleBtn.setFrameShape(QFrame.NoFrame)
        self.frame_appTitleBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_appTitleBtn)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.btn_minimizeApp = QPushButton(self.frame_appTitleBtn)
        self.btn_minimizeApp.setObjectName(u"btn_minimizeApp")
        self.btn_minimizeApp.setMinimumSize(QSize(25, 25))
        self.btn_minimizeApp.setMaximumSize(QSize(25, 25))
        self.btn_minimizeApp.setFocusPolicy(Qt.TabFocus)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizeApp.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_minimizeApp)

        self.btn_maximizeApp = QPushButton(self.frame_appTitleBtn)
        self.btn_maximizeApp.setObjectName(u"btn_maximizeApp")
        self.btn_maximizeApp.setMinimumSize(QSize(25, 25))
        self.btn_maximizeApp.setMaximumSize(QSize(25, 25))
        self.btn_maximizeApp.setFocusPolicy(Qt.TabFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximizeApp.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_maximizeApp)

        self.btn_closeApp = QPushButton(self.frame_appTitleBtn)
        self.btn_closeApp.setObjectName(u"btn_closeApp")
        self.btn_closeApp.setMinimumSize(QSize(25, 25))
        self.btn_closeApp.setMaximumSize(QSize(25, 25))
        self.btn_closeApp.setFocusPolicy(Qt.TabFocus)
        self.btn_closeApp.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeApp.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_closeApp)


        self.horizontalLayout.addWidget(self.frame_appTitleBtn)


        self.verticalLayout_2.addWidget(self.frame_titleBar)

        self.frame_contentBar = QFrame(self.frame_app)
        self.frame_contentBar.setObjectName(u"frame_contentBar")
        self.frame_contentBar.setStyleSheet(u"")
        self.frame_contentBar.setFrameShape(QFrame.NoFrame)
        self.frame_contentBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_contentBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_leftMenu = QFrame(self.frame_contentBar)
        self.frame_leftMenu.setObjectName(u"frame_leftMenu")
        self.frame_leftMenu.setMinimumSize(QSize(200, 0))
        self.frame_leftMenu.setMaximumSize(QSize(0, 16777215))
        self.frame_leftMenu.setFrameShape(QFrame.NoFrame)
        self.frame_leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_leftMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_leftMenu)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMinimumSize(QSize(200, 60))
        self.frame_toggle.setMaximumSize(QSize(200, 60))
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 15, 0, 0)
        self.frame_toggleInner = QFrame(self.frame_toggle)
        self.frame_toggleInner.setObjectName(u"frame_toggleInner")
        self.frame_toggleInner.setMinimumSize(QSize(200, 45))
        self.frame_toggleInner.setMaximumSize(QSize(200, 45))
        self.frame_toggleInner.setBaseSize(QSize(0, 45))
        self.frame_toggleInner.setFrameShape(QFrame.NoFrame)
        self.frame_toggleInner.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_toggleInner)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_toggleMenu = QPushButton(self.frame_toggleInner)
        self.btn_toggleMenu.setObjectName(u"btn_toggleMenu")
        self.btn_toggleMenu.setEnabled(True)
        self.btn_toggleMenu.setMinimumSize(QSize(50, 45))
        self.btn_toggleMenu.setMaximumSize(QSize(50, 45))
        self.btn_toggleMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggleMenu.setFocusPolicy(Qt.TabFocus)
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggleMenu.setIcon(icon3)
        self.btn_toggleMenu.setFlat(False)

        self.horizontalLayout_5.addWidget(self.btn_toggleMenu)

        self.btn_LMenuToggleText = QPushButton(self.frame_toggleInner)
        self.btn_LMenuToggleText.setObjectName(u"btn_LMenuToggleText")
        self.btn_LMenuToggleText.setEnabled(True)
        self.btn_LMenuToggleText.setMinimumSize(QSize(150, 45))
        self.btn_LMenuToggleText.setMaximumSize(QSize(150, 45))
        font2 = QFont()
        font2.setPointSize(14)
        self.btn_LMenuToggleText.setFont(font2)
        self.btn_LMenuToggleText.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_LMenuToggleText.setFocusPolicy(Qt.NoFocus)
        self.btn_LMenuToggleText.setLayoutDirection(Qt.LeftToRight)
        self.btn_LMenuToggleText.setStyleSheet(u"btn_LMenuToggleText {\n"
"	color: red;\n"
"	text-align: left;\n"
"}")
        self.btn_LMenuToggleText.setFlat(False)

        self.horizontalLayout_5.addWidget(self.btn_LMenuToggleText)


        self.verticalLayout_5.addWidget(self.frame_toggleInner)


        self.verticalLayout_4.addWidget(self.frame_toggle)

        self.frame_LMenuMdl = QFrame(self.frame_leftMenu)
        self.frame_LMenuMdl.setObjectName(u"frame_LMenuMdl")
        self.frame_LMenuMdl.setMinimumSize(QSize(200, 300))
        self.frame_LMenuMdl.setMaximumSize(QSize(200, 16777215))
        self.frame_LMenuMdl.setStyleSheet(u"")
        self.frame_LMenuMdl.setFrameShape(QFrame.NoFrame)
        self.frame_LMenuMdl.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_LMenuMdl)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_stockMenu = QFrame(self.frame_LMenuMdl)
        self.frame_stockMenu.setObjectName(u"frame_stockMenu")
        self.frame_stockMenu.setMinimumSize(QSize(200, 45))
        self.frame_stockMenu.setMaximumSize(QSize(200, 45))
        self.frame_stockMenu.setBaseSize(QSize(0, 45))
        self.frame_stockMenu.setFrameShape(QFrame.NoFrame)
        self.frame_stockMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_stockMenu)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_stockMenu = QPushButton(self.frame_stockMenu)
        self.btn_stockMenu.setObjectName(u"btn_stockMenu")
        self.btn_stockMenu.setEnabled(True)
        self.btn_stockMenu.setMinimumSize(QSize(50, 45))
        self.btn_stockMenu.setMaximumSize(QSize(50, 45))
        self.btn_stockMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stockMenu.setFocusPolicy(Qt.TabFocus)
        self.btn_stockMenu.setStyleSheet(u"")
        self.btn_stockMenu.setText(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-view-column.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stockMenu.setIcon(icon4)
        self.btn_stockMenu.setFlat(False)

        self.horizontalLayout_6.addWidget(self.btn_stockMenu)

        self.btn_stockMenuText = QPushButton(self.frame_stockMenu)
        self.btn_stockMenuText.setObjectName(u"btn_stockMenuText")
        self.btn_stockMenuText.setEnabled(True)
        self.btn_stockMenuText.setMinimumSize(QSize(150, 45))
        self.btn_stockMenuText.setMaximumSize(QSize(150, 45))
        self.btn_stockMenuText.setFont(font2)
        self.btn_stockMenuText.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stockMenuText.setFocusPolicy(Qt.NoFocus)
        self.btn_stockMenuText.setLayoutDirection(Qt.LeftToRight)
        self.btn_stockMenuText.setStyleSheet(u"btn_LMenuToggleText {\n"
"	color: red;\n"
"	text-align: left;\n"
"}")
        self.btn_stockMenuText.setFlat(False)

        self.horizontalLayout_6.addWidget(self.btn_stockMenuText)


        self.verticalLayout.addWidget(self.frame_stockMenu)

        self.frame_user = QFrame(self.frame_LMenuMdl)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setMinimumSize(QSize(200, 45))
        self.frame_user.setMaximumSize(QSize(200, 45))
        self.frame_user.setBaseSize(QSize(0, 45))
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_receiveMenu = QPushButton(self.frame_user)
        self.btn_receiveMenu.setObjectName(u"btn_receiveMenu")
        self.btn_receiveMenu.setEnabled(True)
        self.btn_receiveMenu.setMinimumSize(QSize(50, 45))
        self.btn_receiveMenu.setMaximumSize(QSize(50, 45))
        self.btn_receiveMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_receiveMenu.setFocusPolicy(Qt.TabFocus)
        self.btn_receiveMenu.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_receiveMenu.setIcon(icon5)
        self.btn_receiveMenu.setFlat(False)

        self.horizontalLayout_4.addWidget(self.btn_receiveMenu)

        self.btn_receiveMenuText = QPushButton(self.frame_user)
        self.btn_receiveMenuText.setObjectName(u"btn_receiveMenuText")
        self.btn_receiveMenuText.setEnabled(True)
        self.btn_receiveMenuText.setMinimumSize(QSize(150, 45))
        self.btn_receiveMenuText.setMaximumSize(QSize(150, 45))
        self.btn_receiveMenuText.setFont(font2)
        self.btn_receiveMenuText.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_receiveMenuText.setFocusPolicy(Qt.NoFocus)
        self.btn_receiveMenuText.setLayoutDirection(Qt.LeftToRight)
        self.btn_receiveMenuText.setStyleSheet(u"btn_LMenuToggleText {\n"
"	color: red;\n"
"	text-align: left;\n"
"}")
        self.btn_receiveMenuText.setFlat(False)

        self.horizontalLayout_4.addWidget(self.btn_receiveMenuText)


        self.verticalLayout.addWidget(self.frame_user)

        self.frame_user_2 = QFrame(self.frame_LMenuMdl)
        self.frame_user_2.setObjectName(u"frame_user_2")
        self.frame_user_2.setMinimumSize(QSize(200, 45))
        self.frame_user_2.setMaximumSize(QSize(200, 45))
        self.frame_user_2.setBaseSize(QSize(0, 45))
        self.frame_user_2.setFrameShape(QFrame.NoFrame)
        self.frame_user_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_user_2)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.btn_reviewMenu = QPushButton(self.frame_user_2)
        self.btn_reviewMenu.setObjectName(u"btn_reviewMenu")
        self.btn_reviewMenu.setEnabled(True)
        self.btn_reviewMenu.setMinimumSize(QSize(50, 45))
        self.btn_reviewMenu.setMaximumSize(QSize(50, 45))
        self.btn_reviewMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reviewMenu.setFocusPolicy(Qt.TabFocus)
        self.btn_reviewMenu.setStyleSheet(u"")
        self.btn_reviewMenu.setIcon(icon5)
        self.btn_reviewMenu.setFlat(False)

        self.horizontalLayout_52.addWidget(self.btn_reviewMenu)

        self.btn_reviewMenuText = QPushButton(self.frame_user_2)
        self.btn_reviewMenuText.setObjectName(u"btn_reviewMenuText")
        self.btn_reviewMenuText.setEnabled(True)
        self.btn_reviewMenuText.setMinimumSize(QSize(150, 45))
        self.btn_reviewMenuText.setMaximumSize(QSize(150, 45))
        self.btn_reviewMenuText.setFont(font2)
        self.btn_reviewMenuText.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reviewMenuText.setFocusPolicy(Qt.NoFocus)
        self.btn_reviewMenuText.setLayoutDirection(Qt.LeftToRight)
        self.btn_reviewMenuText.setStyleSheet(u"btn_LMenuToggleText {\n"
"	color: red;\n"
"	text-align: left;\n"
"}")
        self.btn_reviewMenuText.setFlat(False)

        self.horizontalLayout_52.addWidget(self.btn_reviewMenuText)


        self.verticalLayout.addWidget(self.frame_user_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.verticalLayout_4.addWidget(self.frame_LMenuMdl, 0, Qt.AlignTop)

        self.frame_LMenuBtm = QFrame(self.frame_leftMenu)
        self.frame_LMenuBtm.setObjectName(u"frame_LMenuBtm")
        self.frame_LMenuBtm.setFrameShape(QFrame.NoFrame)
        self.frame_LMenuBtm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_LMenuBtm)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_exitMenu = QFrame(self.frame_LMenuBtm)
        self.frame_exitMenu.setObjectName(u"frame_exitMenu")
        self.frame_exitMenu.setMinimumSize(QSize(200, 45))
        self.frame_exitMenu.setMaximumSize(QSize(200, 45))
        self.frame_exitMenu.setBaseSize(QSize(0, 45))
        self.frame_exitMenu.setFrameShape(QFrame.NoFrame)
        self.frame_exitMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_exitMenu)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_exitMenu = QPushButton(self.frame_exitMenu)
        self.btn_exitMenu.setObjectName(u"btn_exitMenu")
        self.btn_exitMenu.setEnabled(True)
        self.btn_exitMenu.setMinimumSize(QSize(50, 45))
        self.btn_exitMenu.setMaximumSize(QSize(50, 45))
        self.btn_exitMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exitMenu.setFocusPolicy(Qt.TabFocus)
        self.btn_exitMenu.setStyleSheet(u"")
        self.btn_exitMenu.setText(u"")
        self.btn_exitMenu.setIcon(icon4)
        self.btn_exitMenu.setFlat(False)

        self.horizontalLayout_13.addWidget(self.btn_exitMenu)

        self.btn_exitMenuText = QPushButton(self.frame_exitMenu)
        self.btn_exitMenuText.setObjectName(u"btn_exitMenuText")
        self.btn_exitMenuText.setEnabled(True)
        self.btn_exitMenuText.setMinimumSize(QSize(150, 45))
        self.btn_exitMenuText.setMaximumSize(QSize(150, 45))
        self.btn_exitMenuText.setFont(font2)
        self.btn_exitMenuText.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exitMenuText.setFocusPolicy(Qt.NoFocus)
        self.btn_exitMenuText.setLayoutDirection(Qt.LeftToRight)
        self.btn_exitMenuText.setStyleSheet(u"btn_LMenuToggleText {\n"
"	color: red;\n"
"	text-align: left;\n"
"}")
        self.btn_exitMenuText.setFlat(False)

        self.horizontalLayout_13.addWidget(self.btn_exitMenuText)


        self.verticalLayout_10.addWidget(self.frame_exitMenu)


        self.verticalLayout_4.addWidget(self.frame_LMenuBtm, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_leftMenu)

        self.frame_mainContent = QFrame(self.frame_contentBar)
        self.frame_mainContent.setObjectName(u"frame_mainContent")
        self.frame_mainContent.setFrameShape(QFrame.NoFrame)
        self.frame_mainContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_mainContent)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frameStackedWidget = QFrame(self.frame_mainContent)
        self.frameStackedWidget.setObjectName(u"frameStackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameStackedWidget.sizePolicy().hasHeightForWidth())
        self.frameStackedWidget.setSizePolicy(sizePolicy)
        self.frameStackedWidget.setFrameShape(QFrame.NoFrame)
        self.frameStackedWidget.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frameStackedWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frameStackedWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet(u"#btn_LMenuToggleText {\n"
"	text-align: left;\n"
"}")
        self.page_stockView = QWidget()
        self.page_stockView.setObjectName(u"page_stockView")
        self.verticalLayout_11 = QVBoxLayout(self.page_stockView)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_pageStockView = QFrame(self.page_stockView)
        self.frame_pageStockView.setObjectName(u"frame_pageStockView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_pageStockView.sizePolicy().hasHeightForWidth())
        self.frame_pageStockView.setSizePolicy(sizePolicy1)
        self.frame_pageStockView.setFrameShape(QFrame.StyledPanel)
        self.frame_pageStockView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_pageStockView)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_tableStock = QFrame(self.frame_pageStockView)
        self.frame_tableStock.setObjectName(u"frame_tableStock")
        self.frame_tableStock.setStyleSheet(u"")
        self.frame_tableStock.setFrameShape(QFrame.StyledPanel)
        self.frame_tableStock.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_tableStock)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.item_tbl = QTableWidget(self.frame_tableStock)
        self.item_tbl.setObjectName(u"item_tbl")

        self.verticalLayout_7.addWidget(self.item_tbl)


        self.verticalLayout_12.addWidget(self.frame_tableStock)

        self.frame_btnStock = QFrame(self.frame_pageStockView)
        self.frame_btnStock.setObjectName(u"frame_btnStock")
        self.frame_btnStock.setMinimumSize(QSize(0, 50))
        self.frame_btnStock.setMaximumSize(QSize(16777215, 50))
        self.frame_btnStock.setStyleSheet(u"")
        self.frame_btnStock.setFrameShape(QFrame.NoFrame)
        self.frame_btnStock.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_btnStock)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_btnStock)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.itemList_cmb = QComboBox(self.frame_2)
        self.itemList_cmb.setObjectName(u"itemList_cmb")
        font3 = QFont()
        font3.setPointSize(11)
        self.itemList_cmb.setFont(font3)
        self.itemList_cmb.setEditable(False)

        self.horizontalLayout_42.addWidget(self.itemList_cmb)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_12)

        self.itemCode_cmb = QComboBox(self.frame_2)
        self.itemCode_cmb.setObjectName(u"itemCode_cmb")
        self.itemCode_cmb.setFont(font3)
        self.itemCode_cmb.setEditable(False)

        self.horizontalLayout_42.addWidget(self.itemCode_cmb)


        self.horizontalLayout_7.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_btnStock)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 0, 10, 0)
        self.btn_stockConsolidate = QPushButton(self.frame)
        self.btn_stockConsolidate.setObjectName(u"btn_stockConsolidate")

        self.horizontalLayout_11.addWidget(self.btn_stockConsolidate)

        self.btn_stockExpand = QPushButton(self.frame)
        self.btn_stockExpand.setObjectName(u"btn_stockExpand")

        self.horizontalLayout_11.addWidget(self.btn_stockExpand)

        self.btn_stock_report = QPushButton(self.frame)
        self.btn_stock_report.setObjectName(u"btn_stock_report")

        self.horizontalLayout_11.addWidget(self.btn_stock_report)


        self.horizontalLayout_7.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_btnStock)


        self.verticalLayout_11.addWidget(self.frame_pageStockView)

        self.stackedWidget.addWidget(self.page_stockView)
        self.page_usage = QWidget()
        self.page_usage.setObjectName(u"page_usage")
        sizePolicy.setHeightForWidth(self.page_usage.sizePolicy().hasHeightForWidth())
        self.page_usage.setSizePolicy(sizePolicy)
        self.verticalLayout_18 = QVBoxLayout(self.page_usage)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_pageUsage = QFrame(self.page_usage)
        self.frame_pageUsage.setObjectName(u"frame_pageUsage")
        sizePolicy.setHeightForWidth(self.frame_pageUsage.sizePolicy().hasHeightForWidth())
        self.frame_pageUsage.setSizePolicy(sizePolicy)
        self.frame_pageUsage.setStyleSheet(u"")
        self.frame_pageUsage.setFrameShape(QFrame.NoFrame)
        self.frame_pageUsage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_pageUsage)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_pageUsageDetails = QFrame(self.frame_pageUsage)
        self.frame_pageUsageDetails.setObjectName(u"frame_pageUsageDetails")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_pageUsageDetails.sizePolicy().hasHeightForWidth())
        self.frame_pageUsageDetails.setSizePolicy(sizePolicy2)
        self.frame_pageUsageDetails.setMinimumSize(QSize(0, 240))
        self.frame_pageUsageDetails.setMaximumSize(QSize(16777215, 240))
        self.frame_pageUsageDetails.setFrameShape(QFrame.NoFrame)
        self.frame_pageUsageDetails.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_pageUsageDetails)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.frame_pageUsageDetails)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(350, 250))
        self.groupBox_4.setMaximumSize(QSize(16777215, 250))
        self.groupBox_4.setFont(font)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.groupBox_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_9)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 5, 10, 0)
        self.frame_5 = QFrame(self.frame_9)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(120, 0))
        self.label_24.setMaximumSize(QSize(100, 16777215))
        self.label_24.setFont(font3)
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_24)

        self.outUserName_txt = QLineEdit(self.frame_5)
        self.outUserName_txt.setObjectName(u"outUserName_txt")
        self.outUserName_txt.setMinimumSize(QSize(200, 0))
        self.outUserName_txt.setMaximumSize(QSize(16777215, 16777215))
        self.outUserName_txt.setFont(font3)
        self.outUserName_txt.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.outUserName_txt)


        self.verticalLayout_16.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(120, 0))
        self.label_17.setMaximumSize(QSize(100, 16777215))
        self.label_17.setFont(font3)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_17)

        self.outDate_dt = QDateEdit(self.frame_6)
        self.outDate_dt.setObjectName(u"outDate_dt")
        self.outDate_dt.setMinimumSize(QSize(200, 0))
        self.outDate_dt.setMaximumSize(QSize(16777215, 16777215))
        self.outDate_dt.setFont(font3)
        self.outDate_dt.setCalendarPopup(True)

        self.horizontalLayout_15.addWidget(self.outDate_dt)


        self.verticalLayout_16.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.outInfo_lbl = QLabel(self.frame_7)
        self.outInfo_lbl.setObjectName(u"outInfo_lbl")
        self.outInfo_lbl.setMinimumSize(QSize(120, 0))
        self.outInfo_lbl.setMaximumSize(QSize(100, 16777215))
        self.outInfo_lbl.setFont(font3)
        self.outInfo_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.outInfo_lbl)

        self.outInfo_txt = QLineEdit(self.frame_7)
        self.outInfo_txt.setObjectName(u"outInfo_txt")
        self.outInfo_txt.setMinimumSize(QSize(200, 0))
        self.outInfo_txt.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setItalic(False)
        self.outInfo_txt.setFont(font4)
        self.outInfo_txt.setStyleSheet(u"")
        self.outInfo_txt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.outInfo_txt)


        self.verticalLayout_16.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.outUsage_lbl = QLabel(self.frame_8)
        self.outUsage_lbl.setObjectName(u"outUsage_lbl")
        self.outUsage_lbl.setMinimumSize(QSize(120, 0))
        self.outUsage_lbl.setMaximumSize(QSize(100, 16777215))
        self.outUsage_lbl.setFont(font3)
        self.outUsage_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.outUsage_lbl)

        self.outUsage_txt = QLineEdit(self.frame_8)
        self.outUsage_txt.setObjectName(u"outUsage_txt")
        self.outUsage_txt.setMinimumSize(QSize(120, 0))
        self.outUsage_txt.setMaximumSize(QSize(120, 16777215))
        self.outUsage_txt.setFont(font4)
        self.outUsage_txt.setAlignment(Qt.AlignCenter)
        self.outUsage_txt.setReadOnly(False)

        self.horizontalLayout_17.addWidget(self.outUsage_txt)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_7)


        self.verticalLayout_16.addWidget(self.frame_8)

        self.frame_21 = QFrame(self.frame_9)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 45))
        self.frame_21.setMaximumSize(QSize(16777215, 45))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_21)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(200, 40))
        self.frame_13.setMaximumSize(QSize(16777215, 40))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_3)

        self.btn_itemOut = QPushButton(self.frame_13)
        self.btn_itemOut.setObjectName(u"btn_itemOut")
        self.btn_itemOut.setMinimumSize(QSize(40, 40))
        self.btn_itemOut.setMaximumSize(QSize(16777215, 40))
        self.btn_itemOut.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/images/images/cil-transfer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_itemOut.setIcon(icon6)
        self.btn_itemOut.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.btn_itemOut)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_27.addWidget(self.frame_13, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.frame_21)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_2)


        self.verticalLayout_13.addWidget(self.frame_9)


        self.horizontalLayout_21.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame_pageUsageDetails)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(350, 250))
        self.groupBox_5.setMaximumSize(QSize(16777215, 250))
        self.groupBox_5.setFont(font)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 9, 0)
        self.frame_10 = QFrame(self.groupBox_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 5, 10, 0)
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_12)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(120, 0))
        self.label_25.setMaximumSize(QSize(100, 16777215))
        self.label_25.setFont(font3)
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_25)

        self.outType_txt = QLineEdit(self.frame_12)
        self.outType_txt.setObjectName(u"outType_txt")
        self.outType_txt.setMinimumSize(QSize(200, 0))
        self.outType_txt.setMaximumSize(QSize(16777215, 16777215))
        self.outType_txt.setFont(font3)
        self.outType_txt.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.outType_txt)


        self.verticalLayout_14.addWidget(self.frame_12)

        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_16)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(120, 0))
        self.label_26.setMaximumSize(QSize(100, 16777215))
        self.label_26.setFont(font3)
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_26)

        self.outCode_txt = QLineEdit(self.frame_16)
        self.outCode_txt.setObjectName(u"outCode_txt")
        self.outCode_txt.setMinimumSize(QSize(200, 0))
        self.outCode_txt.setMaximumSize(QSize(16777215, 16777215))
        self.outCode_txt.setFont(font3)
        self.outCode_txt.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.outCode_txt)


        self.verticalLayout_14.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_10)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_17)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(120, 0))
        self.label_27.setMaximumSize(QSize(100, 16777215))
        self.label_27.setFont(font3)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_27)

        self.outBatch_txt = QLineEdit(self.frame_17)
        self.outBatch_txt.setObjectName(u"outBatch_txt")
        self.outBatch_txt.setMinimumSize(QSize(200, 0))
        self.outBatch_txt.setMaximumSize(QSize(16777215, 16777215))
        self.outBatch_txt.setFont(font3)
        self.outBatch_txt.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.outBatch_txt)


        self.verticalLayout_14.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_10)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_18)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(120, 0))
        self.label_28.setMaximumSize(QSize(100, 16777215))
        self.label_28.setFont(font3)
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_28)

        self.outStock_txt = QLineEdit(self.frame_18)
        self.outStock_txt.setObjectName(u"outStock_txt")
        self.outStock_txt.setMinimumSize(QSize(120, 0))
        self.outStock_txt.setMaximumSize(QSize(120, 16777215))
        self.outStock_txt.setFont(font3)
        self.outStock_txt.setAlignment(Qt.AlignCenter)
        self.outStock_txt.setReadOnly(True)

        self.horizontalLayout_24.addWidget(self.outStock_txt)

        self.outUnit_txt = QLineEdit(self.frame_18)
        self.outUnit_txt.setObjectName(u"outUnit_txt")
        self.outUnit_txt.setMinimumSize(QSize(120, 0))
        self.outUnit_txt.setMaximumSize(QSize(120, 16777215))
        self.outUnit_txt.setFont(font3)
        self.outUnit_txt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.outUnit_txt.setReadOnly(True)

        self.horizontalLayout_24.addWidget(self.outUnit_txt)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_5)


        self.verticalLayout_14.addWidget(self.frame_18)

        self.frame_20 = QFrame(self.frame_10)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_20)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(120, 0))
        self.label_30.setMaximumSize(QSize(120, 16777215))
        self.label_30.setFont(font3)
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.label_30)

        self.frame_4 = QFrame(self.frame_20)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 30))
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_2)

        self.btn_toStandby = QPushButton(self.frame_4)
        self.btn_toStandby.setObjectName(u"btn_toStandby")
        self.btn_toStandby.setMinimumSize(QSize(25, 25))
        self.btn_toStandby.setMaximumSize(QSize(25, 25))
        icon7 = QIcon()
        icon7.addFile(u":/images/images/cil-chevron-double-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toStandby.setIcon(icon7)

        self.horizontalLayout_19.addWidget(self.btn_toStandby)

        self.btn_toStock = QPushButton(self.frame_4)
        self.btn_toStock.setObjectName(u"btn_toStock")
        self.btn_toStock.setMinimumSize(QSize(25, 25))
        self.btn_toStock.setMaximumSize(QSize(25, 25))
        icon8 = QIcon()
        icon8.addFile(u":/images/images/cil-chevron-double-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toStock.setIcon(icon8)

        self.horizontalLayout_19.addWidget(self.btn_toStock)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_26.addWidget(self.frame_4, 0, Qt.AlignLeft)


        self.verticalLayout_14.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_10)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_19)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(120, 0))
        self.label_29.setMaximumSize(QSize(100, 16777215))
        self.label_29.setFont(font3)
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_29)

        self.outStandby_txt = QLineEdit(self.frame_19)
        self.outStandby_txt.setObjectName(u"outStandby_txt")
        self.outStandby_txt.setMinimumSize(QSize(120, 0))
        self.outStandby_txt.setMaximumSize(QSize(120, 16777215))
        self.outStandby_txt.setFont(font3)
        self.outStandby_txt.setAlignment(Qt.AlignCenter)
        self.outStandby_txt.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.outStandby_txt)

        self.outUnit_txt_2 = QLineEdit(self.frame_19)
        self.outUnit_txt_2.setObjectName(u"outUnit_txt_2")
        self.outUnit_txt_2.setMinimumSize(QSize(120, 0))
        self.outUnit_txt_2.setMaximumSize(QSize(120, 16777215))
        self.outUnit_txt_2.setFont(font3)
        self.outUnit_txt_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.outUnit_txt_2.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.outUnit_txt_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer)


        self.verticalLayout_14.addWidget(self.frame_19)


        self.verticalLayout_15.addWidget(self.frame_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)


        self.horizontalLayout_21.addWidget(self.groupBox_5)


        self.verticalLayout_6.addWidget(self.frame_pageUsageDetails)

        self.frame_3 = QFrame(self.frame_pageUsage)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_3)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.usage_tbl = QTableWidget(self.frame_3)
        self.usage_tbl.setObjectName(u"usage_tbl")
        sizePolicy1.setHeightForWidth(self.usage_tbl.sizePolicy().hasHeightForWidth())
        self.usage_tbl.setSizePolicy(sizePolicy1)

        self.verticalLayout_17.addWidget(self.usage_tbl)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_18.addWidget(self.frame_pageUsage)

        self.stackedWidget.addWidget(self.page_usage)
        self.pageReceive = QWidget()
        self.pageReceive.setObjectName(u"pageReceive")
        self.verticalLayout_19 = QVBoxLayout(self.pageReceive)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_pageReceive = QFrame(self.pageReceive)
        self.frame_pageReceive.setObjectName(u"frame_pageReceive")
        sizePolicy.setHeightForWidth(self.frame_pageReceive.sizePolicy().hasHeightForWidth())
        self.frame_pageReceive.setSizePolicy(sizePolicy)
        self.frame_pageReceive.setStyleSheet(u"")
        self.frame_pageReceive.setFrameShape(QFrame.NoFrame)
        self.frame_pageReceive.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_pageReceive)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_pageReceiveDetails = QFrame(self.frame_pageReceive)
        self.frame_pageReceiveDetails.setObjectName(u"frame_pageReceiveDetails")
        sizePolicy2.setHeightForWidth(self.frame_pageReceiveDetails.sizePolicy().hasHeightForWidth())
        self.frame_pageReceiveDetails.setSizePolicy(sizePolicy2)
        self.frame_pageReceiveDetails.setMinimumSize(QSize(0, 220))
        self.frame_pageReceiveDetails.setMaximumSize(QSize(16777215, 220))
        self.frame_pageReceiveDetails.setFrameShape(QFrame.NoFrame)
        self.frame_pageReceiveDetails.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_pageReceiveDetails)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(10, 3, 10, 0)
        self.groupBox_7 = QGroupBox(self.frame_pageReceiveDetails)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(350, 200))
        self.groupBox_7.setMaximumSize(QSize(16777215, 200))
        self.groupBox_7.setFont(font)
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.groupBox_7)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_26)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(10, 10, 10, 0)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_27)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(120, 0))
        self.label_32.setMaximumSize(QSize(100, 16777215))
        self.label_32.setFont(font3)
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.label_32)

        self.inType_cmb = QComboBox(self.frame_27)
        self.inType_cmb.setObjectName(u"inType_cmb")
        self.inType_cmb.setFont(font3)

        self.horizontalLayout_35.addWidget(self.inType_cmb)


        self.verticalLayout_23.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_28)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(120, 0))
        self.label_33.setMaximumSize(QSize(100, 16777215))
        self.label_33.setFont(font3)
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_33)

        self.inCode_cmb = QComboBox(self.frame_28)
        self.inCode_cmb.setObjectName(u"inCode_cmb")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        self.inCode_cmb.setFont(font5)
        self.inCode_cmb.setStyleSheet(u"	#inCode_cmb {\n"
"		border: none;\n"
"		background-color: lightyellow;\n"
"		border-bottom: 2px solid red;\n"
"		font: 12pt \"Segoe UI\";\n"
"	}")
        self.inCode_cmb.setEditable(True)

        self.horizontalLayout_36.addWidget(self.inCode_cmb)


        self.verticalLayout_23.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_29)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(120, 0))
        self.label_34.setMaximumSize(QSize(100, 16777215))
        self.label_34.setFont(font3)
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_34)

        self.inBatch_cmb = QComboBox(self.frame_29)
        self.inBatch_cmb.setObjectName(u"inBatch_cmb")
        self.inBatch_cmb.setFont(font5)
        self.inBatch_cmb.setStyleSheet(u"	#inBatch_cmb {\n"
"		border: none;\n"
"		background-color: lightyellow;\n"
"		border-bottom: 2px solid red;\n"
"		font: 12pt \"Segoe UI\";\n"
"	}")
        self.inBatch_cmb.setEditable(True)

        self.horizontalLayout_37.addWidget(self.inBatch_cmb)


        self.verticalLayout_23.addWidget(self.frame_29)

        self.frame_22 = QFrame(self.frame_26)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.outInfo_lbl_2 = QLabel(self.frame_22)
        self.outInfo_lbl_2.setObjectName(u"outInfo_lbl_2")
        self.outInfo_lbl_2.setMinimumSize(QSize(120, 0))
        self.outInfo_lbl_2.setMaximumSize(QSize(100, 16777215))
        self.outInfo_lbl_2.setFont(font3)
        self.outInfo_lbl_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.outInfo_lbl_2)

        self.inDescription_txt = QLineEdit(self.frame_22)
        self.inDescription_txt.setObjectName(u"inDescription_txt")
        self.inDescription_txt.setMinimumSize(QSize(200, 0))
        self.inDescription_txt.setMaximumSize(QSize(16777215, 16777215))
        self.inDescription_txt.setFont(font4)
        self.inDescription_txt.setStyleSheet(u"")
        self.inDescription_txt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.inDescription_txt)


        self.verticalLayout_23.addWidget(self.frame_22)

        self.frame_31 = QFrame(self.frame_26)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.outInfo_lbl_3 = QLabel(self.frame_31)
        self.outInfo_lbl_3.setObjectName(u"outInfo_lbl_3")
        self.outInfo_lbl_3.setMinimumSize(QSize(120, 0))
        self.outInfo_lbl_3.setMaximumSize(QSize(100, 16777215))
        self.outInfo_lbl_3.setFont(font3)
        self.outInfo_lbl_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.outInfo_lbl_3)

        self.inComment_txt = QLineEdit(self.frame_31)
        self.inComment_txt.setObjectName(u"inComment_txt")
        self.inComment_txt.setMinimumSize(QSize(200, 0))
        self.inComment_txt.setMaximumSize(QSize(16777215, 16777215))
        self.inComment_txt.setFont(font4)
        self.inComment_txt.setStyleSheet(u"")
        self.inComment_txt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.inComment_txt)


        self.verticalLayout_23.addWidget(self.frame_31)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_3)


        self.verticalLayout_22.addWidget(self.frame_26)


        self.horizontalLayout_28.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.frame_pageReceiveDetails)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(350, 200))
        self.groupBox_6.setMaximumSize(QSize(16777215, 200))
        self.groupBox_6.setFont(font)
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.groupBox_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_11)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(10, 10, 10, 0)
        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_14)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(140, 0))
        self.label_31.setMaximumSize(QSize(140, 16777215))
        self.label_31.setFont(font3)
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_31)

        self.inUserName_txt = QLineEdit(self.frame_14)
        self.inUserName_txt.setObjectName(u"inUserName_txt")
        self.inUserName_txt.setMinimumSize(QSize(200, 0))
        self.inUserName_txt.setMaximumSize(QSize(16777215, 16777215))
        self.inUserName_txt.setFont(font3)
        self.inUserName_txt.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.inUserName_txt)


        self.verticalLayout_21.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(140, 0))
        self.label_18.setMaximumSize(QSize(140, 16777215))
        self.label_18.setFont(font3)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_18)

        self.inDate_dt = QDateEdit(self.frame_15)
        self.inDate_dt.setObjectName(u"inDate_dt")
        self.inDate_dt.setMinimumSize(QSize(160, 0))
        self.inDate_dt.setMaximumSize(QSize(16777215, 16777215))
        self.inDate_dt.setFont(font3)
        self.inDate_dt.setCalendarPopup(True)

        self.horizontalLayout_30.addWidget(self.inDate_dt)


        self.verticalLayout_21.addWidget(self.frame_15)

        self.frame_30 = QFrame(self.frame_11)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_30)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(140, 0))
        self.label_35.setMaximumSize(QSize(140, 16777215))
        self.label_35.setFont(font3)
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.label_35)

        self.inQty_txt = QLineEdit(self.frame_30)
        self.inQty_txt.setObjectName(u"inQty_txt")
        self.inQty_txt.setMinimumSize(QSize(120, 0))
        self.inQty_txt.setMaximumSize(QSize(120, 16777215))
        self.inQty_txt.setFont(font3)
        self.inQty_txt.setAlignment(Qt.AlignCenter)
        self.inQty_txt.setReadOnly(False)

        self.horizontalLayout_38.addWidget(self.inQty_txt)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_11)


        self.verticalLayout_21.addWidget(self.frame_30)

        self.frame_33 = QFrame(self.frame_11)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_33)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(140, 0))
        self.label_37.setMaximumSize(QSize(140, 16777215))
        self.label_37.setFont(font3)
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.label_37)

        self.inTransitQty_txt = QLineEdit(self.frame_33)
        self.inTransitQty_txt.setObjectName(u"inTransitQty_txt")
        self.inTransitQty_txt.setMinimumSize(QSize(120, 0))
        self.inTransitQty_txt.setMaximumSize(QSize(120, 16777215))
        self.inTransitQty_txt.setFont(font3)
        self.inTransitQty_txt.setAlignment(Qt.AlignCenter)
        self.inTransitQty_txt.setReadOnly(False)

        self.horizontalLayout_41.addWidget(self.inTransitQty_txt)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_14)


        self.verticalLayout_21.addWidget(self.frame_33)

        self.frame_23 = QFrame(self.frame_11)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.outUsage_lbl_2 = QLabel(self.frame_23)
        self.outUsage_lbl_2.setObjectName(u"outUsage_lbl_2")
        self.outUsage_lbl_2.setMinimumSize(QSize(140, 0))
        self.outUsage_lbl_2.setMaximumSize(QSize(140, 16777215))
        self.outUsage_lbl_2.setFont(font3)
        self.outUsage_lbl_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.outUsage_lbl_2)

        self.inUnit_cmb = QComboBox(self.frame_23)
        self.inUnit_cmb.setObjectName(u"inUnit_cmb")
        self.inUnit_cmb.setFont(font5)
        self.inUnit_cmb.setStyleSheet(u"	#inUnit_cmb {\n"
"		border: none;\n"
"		background-color: lightyellow;\n"
"		border-bottom: 2px solid red;\n"
"		font: 12pt \"Segoe UI\";\n"
"	}")
        self.inUnit_cmb.setEditable(True)

        self.horizontalLayout_32.addWidget(self.inUnit_cmb)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_8)


        self.verticalLayout_21.addWidget(self.frame_23)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_4)


        self.verticalLayout_20.addWidget(self.frame_11)


        self.horizontalLayout_28.addWidget(self.groupBox_6)


        self.verticalLayout_24.addWidget(self.frame_pageReceiveDetails)

        self.frame_25 = QFrame(self.frame_pageReceive)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(200, 40))
        self.frame_25.setMaximumSize(QSize(16777215, 40))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_9)

        self.btn_itemIn = QPushButton(self.frame_25)
        self.btn_itemIn.setObjectName(u"btn_itemIn")
        self.btn_itemIn.setMinimumSize(QSize(120, 40))
        self.btn_itemIn.setMaximumSize(QSize(120, 40))
        self.btn_itemIn.setFont(font)
        self.btn_itemIn.setIconSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.btn_itemIn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_10)


        self.verticalLayout_24.addWidget(self.frame_25)

        self.frame_receive_tbl = QFrame(self.frame_pageReceive)
        self.frame_receive_tbl.setObjectName(u"frame_receive_tbl")
        sizePolicy3.setHeightForWidth(self.frame_receive_tbl.sizePolicy().hasHeightForWidth())
        self.frame_receive_tbl.setSizePolicy(sizePolicy3)
        self.frame_receive_tbl.setFrameShape(QFrame.NoFrame)
        self.frame_receive_tbl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_receive_tbl)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(10, 10, 10, 10)
        self.received_tbl = QTableWidget(self.frame_receive_tbl)
        self.received_tbl.setObjectName(u"received_tbl")
        sizePolicy1.setHeightForWidth(self.received_tbl.sizePolicy().hasHeightForWidth())
        self.received_tbl.setSizePolicy(sizePolicy1)

        self.verticalLayout_25.addWidget(self.received_tbl)


        self.verticalLayout_24.addWidget(self.frame_receive_tbl)


        self.verticalLayout_19.addWidget(self.frame_pageReceive)

        self.stackedWidget.addWidget(self.pageReceive)
        self.pageReview = QWidget()
        self.pageReview.setObjectName(u"pageReview")
        self.verticalLayout_29 = QVBoxLayout(self.pageReview)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_pageReview = QFrame(self.pageReview)
        self.frame_pageReview.setObjectName(u"frame_pageReview")
        sizePolicy.setHeightForWidth(self.frame_pageReview.sizePolicy().hasHeightForWidth())
        self.frame_pageReview.setSizePolicy(sizePolicy)
        self.frame_pageReview.setStyleSheet(u"")
        self.frame_pageReview.setFrameShape(QFrame.NoFrame)
        self.frame_pageReview.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_pageReview)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_pageReviewDetails = QFrame(self.frame_pageReview)
        self.frame_pageReviewDetails.setObjectName(u"frame_pageReviewDetails")
        sizePolicy2.setHeightForWidth(self.frame_pageReviewDetails.sizePolicy().hasHeightForWidth())
        self.frame_pageReviewDetails.setSizePolicy(sizePolicy2)
        self.frame_pageReviewDetails.setMinimumSize(QSize(0, 220))
        self.frame_pageReviewDetails.setMaximumSize(QSize(16777215, 220))
        self.frame_pageReviewDetails.setFrameShape(QFrame.NoFrame)
        self.frame_pageReviewDetails.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_pageReviewDetails)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_6)

        self.frame_48 = QFrame(self.frame_pageReviewDetails)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 120))
        self.frame_48.setMaximumSize(QSize(16777215, 120))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_48)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_45)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_46)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(120, 0))
        self.label_43.setMaximumSize(QSize(100, 16777215))
        self.label_43.setFont(font3)
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_53.addWidget(self.label_43)

        self.review_db_cmb = QComboBox(self.frame_46)
        self.review_db_cmb.addItem("")
        self.review_db_cmb.addItem("")
        self.review_db_cmb.setObjectName(u"review_db_cmb")
        self.review_db_cmb.setFont(font3)

        self.horizontalLayout_53.addWidget(self.review_db_cmb)


        self.verticalLayout_30.addWidget(self.frame_46)

        self.frame_34 = QFrame(self.frame_45)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_34)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(120, 0))
        self.label_36.setMaximumSize(QSize(100, 16777215))
        self.label_36.setFont(font3)
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_36)

        self.review_type_cmb = QComboBox(self.frame_34)
        self.review_type_cmb.addItem("")
        self.review_type_cmb.setObjectName(u"review_type_cmb")
        self.review_type_cmb.setFont(font3)

        self.horizontalLayout_40.addWidget(self.review_type_cmb)


        self.verticalLayout_30.addWidget(self.frame_34)

        self.frame_47 = QFrame(self.frame_45)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_47)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(120, 0))
        self.label_44.setMaximumSize(QSize(100, 16777215))
        self.label_44.setFont(font3)
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_54.addWidget(self.label_44)

        self.review_code_cmb = QComboBox(self.frame_47)
        self.review_code_cmb.addItem("")
        self.review_code_cmb.setObjectName(u"review_code_cmb")
        self.review_code_cmb.setFont(font3)

        self.horizontalLayout_54.addWidget(self.review_code_cmb)


        self.verticalLayout_30.addWidget(self.frame_47)


        self.horizontalLayout_57.addWidget(self.frame_45)

        self.frame_35 = QFrame(self.frame_48)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_35)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 20, 0)
        self.frame_40 = QFrame(self.frame_35)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_40)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(140, 0))
        self.label_21.setMaximumSize(QSize(100, 16777215))
        self.label_21.setFont(font3)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_48.addWidget(self.label_21)

        self.reviewStart_dt = QDateEdit(self.frame_40)
        self.reviewStart_dt.setObjectName(u"reviewStart_dt")
        self.reviewStart_dt.setMinimumSize(QSize(200, 0))
        self.reviewStart_dt.setMaximumSize(QSize(16777215, 16777215))
        self.reviewStart_dt.setFont(font3)
        self.reviewStart_dt.setCalendarPopup(True)

        self.horizontalLayout_48.addWidget(self.reviewStart_dt)


        self.verticalLayout_32.addWidget(self.frame_40)

        self.frame_49 = QFrame(self.frame_35)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_49)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(140, 0))
        self.label_22.setMaximumSize(QSize(100, 16777215))
        self.label_22.setFont(font3)
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_58.addWidget(self.label_22)

        self.reviewEnd_dt = QDateEdit(self.frame_49)
        self.reviewEnd_dt.setObjectName(u"reviewEnd_dt")
        self.reviewEnd_dt.setMinimumSize(QSize(200, 0))
        self.reviewEnd_dt.setMaximumSize(QSize(16777215, 16777215))
        self.reviewEnd_dt.setFont(font3)
        self.reviewEnd_dt.setCalendarPopup(True)

        self.horizontalLayout_58.addWidget(self.reviewEnd_dt)


        self.verticalLayout_32.addWidget(self.frame_49)


        self.horizontalLayout_57.addWidget(self.frame_35)


        self.verticalLayout_27.addWidget(self.frame_48)

        self.frame_24 = QFrame(self.frame_pageReviewDetails)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 80))
        self.frame_24.setMaximumSize(QSize(16777215, 80))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_24)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 0))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_32)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(9, 0, 10, 0)
        self.review_keyword_lbl = QLabel(self.frame_32)
        self.review_keyword_lbl.setObjectName(u"review_keyword_lbl")
        self.review_keyword_lbl.setMinimumSize(QSize(400, 25))
        self.review_keyword_lbl.setMaximumSize(QSize(400, 25))
        self.review_keyword_lbl.setFont(font3)
        self.review_keyword_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.review_keyword_lbl)

        self.review_keyword_txt = QLineEdit(self.frame_32)
        self.review_keyword_txt.setObjectName(u"review_keyword_txt")
        self.review_keyword_txt.setMinimumSize(QSize(0, 25))
        self.review_keyword_txt.setMaximumSize(QSize(16777215, 25))
        self.review_keyword_txt.setFont(font4)
        self.review_keyword_txt.setStyleSheet(u"")
        self.review_keyword_txt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.review_keyword_txt)


        self.horizontalLayout_33.addWidget(self.frame_32)

        self.frame_44 = QFrame(self.frame_24)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(200, 60))
        self.frame_44.setMaximumSize(QSize(16777215, 60))
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_16)

        self.review_search_btn = QPushButton(self.frame_44)
        self.review_search_btn.setObjectName(u"review_search_btn")
        self.review_search_btn.setMinimumSize(QSize(120, 40))
        self.review_search_btn.setMaximumSize(QSize(120, 40))
        self.review_search_btn.setFont(font)
        self.review_search_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_51.addWidget(self.review_search_btn)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_13)

        self.review_report_btn = QPushButton(self.frame_44)
        self.review_report_btn.setObjectName(u"review_report_btn")
        self.review_report_btn.setMinimumSize(QSize(120, 40))
        self.review_report_btn.setMaximumSize(QSize(120, 40))
        self.review_report_btn.setFont(font)
        self.review_report_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_51.addWidget(self.review_report_btn)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_17)


        self.horizontalLayout_33.addWidget(self.frame_44)


        self.verticalLayout_27.addWidget(self.frame_24)


        self.verticalLayout_28.addWidget(self.frame_pageReviewDetails)

        self.frame_review_tbl = QFrame(self.frame_pageReview)
        self.frame_review_tbl.setObjectName(u"frame_review_tbl")
        sizePolicy3.setHeightForWidth(self.frame_review_tbl.sizePolicy().hasHeightForWidth())
        self.frame_review_tbl.setSizePolicy(sizePolicy3)
        self.frame_review_tbl.setFrameShape(QFrame.NoFrame)
        self.frame_review_tbl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_review_tbl)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(10, 10, 10, 10)
        self.review_tbl = QTableWidget(self.frame_review_tbl)
        self.review_tbl.setObjectName(u"review_tbl")
        sizePolicy1.setHeightForWidth(self.review_tbl.sizePolicy().hasHeightForWidth())
        self.review_tbl.setSizePolicy(sizePolicy1)

        self.verticalLayout_31.addWidget(self.review_tbl)


        self.verticalLayout_28.addWidget(self.frame_review_tbl)


        self.verticalLayout_29.addWidget(self.frame_pageReview)

        self.stackedWidget.addWidget(self.pageReview)
        self.page_password = QWidget()
        self.page_password.setObjectName(u"page_password")
        self.gridLayout_2 = QGridLayout(self.page_password)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_pagePassword = QFrame(self.page_password)
        self.frame_pagePassword.setObjectName(u"frame_pagePassword")
        self.frame_pagePassword.setMinimumSize(QSize(400, 200))
        self.frame_pagePassword.setMaximumSize(QSize(400, 200))
        self.frame_pagePassword.setStyleSheet(u"#userName_txt {\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-radius: 20px;\n"
"}\n"
"#userPass_txt {\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton {\n"
"    border-style: outset;\n"
"	border: 2px solid #8f8f91;\n"
"    border-radius: 10px;\n"
"    background-color: rgba(100,100,0,100);\n"
"	font: bold 14px;\n"
"    max-width: 100px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	 background-color: rgba(255,0,0,100);\n"
"}\n"
"frame_PasswordBtn {\n"
"	padding: 10px;\n"
"}")
        self.frame_pagePassword.setFrameShape(QFrame.StyledPanel)
        self.frame_pagePassword.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_pagePassword)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_uName = QFrame(self.frame_pagePassword)
        self.frame_uName.setObjectName(u"frame_uName")
        self.frame_uName.setMinimumSize(QSize(0, 45))
        self.frame_uName.setMaximumSize(QSize(16777215, 45))
        self.frame_uName.setStyleSheet(u"")
        self.frame_uName.setFrameShape(QFrame.NoFrame)
        self.frame_uName.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_uName)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_uName)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 45))
        self.label.setMaximumSize(QSize(120, 45))
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label)

        self.userName_txt = QLineEdit(self.frame_uName)
        self.userName_txt.setObjectName(u"userName_txt")
        self.userName_txt.setMinimumSize(QSize(0, 45))
        self.userName_txt.setMaximumSize(QSize(16777215, 45))
        self.userName_txt.setFont(font2)
        self.userName_txt.setStyleSheet(u"")
        self.userName_txt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.userName_txt)


        self.verticalLayout_9.addWidget(self.frame_uName)

        self.frame_uName_2 = QFrame(self.frame_pagePassword)
        self.frame_uName_2.setObjectName(u"frame_uName_2")
        self.frame_uName_2.setMinimumSize(QSize(0, 45))
        self.frame_uName_2.setMaximumSize(QSize(16777215, 45))
        self.frame_uName_2.setStyleSheet(u"#userName_txt {\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_uName_2.setFrameShape(QFrame.NoFrame)
        self.frame_uName_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_uName_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_uName_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 45))
        self.label_2.setMaximumSize(QSize(120, 45))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_2)

        self.userPass_txt = QLineEdit(self.frame_uName_2)
        self.userPass_txt.setObjectName(u"userPass_txt")
        self.userPass_txt.setMinimumSize(QSize(0, 45))
        self.userPass_txt.setMaximumSize(QSize(16777215, 45))
        self.userPass_txt.setFont(font2)
        self.userPass_txt.setStyleSheet(u"")
        self.userPass_txt.setEchoMode(QLineEdit.Password)
        self.userPass_txt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.userPass_txt)


        self.verticalLayout_9.addWidget(self.frame_uName_2)

        self.frame_PasswordBtn = QFrame(self.frame_pagePassword)
        self.frame_PasswordBtn.setObjectName(u"frame_PasswordBtn")
        self.frame_PasswordBtn.setMinimumSize(QSize(0, 45))
        self.frame_PasswordBtn.setMaximumSize(QSize(16777215, 45))
        self.frame_PasswordBtn.setStyleSheet(u"")
        self.frame_PasswordBtn.setFrameShape(QFrame.NoFrame)
        self.frame_PasswordBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_PasswordBtn)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_PasswordBtn)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 45))
        self.label_3.setMaximumSize(QSize(120, 45))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.appExit_btn = QPushButton(self.frame_PasswordBtn)
        self.appExit_btn.setObjectName(u"appExit_btn")
        self.appExit_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.appExit_btn)

        self.userLogin_btn = QPushButton(self.frame_PasswordBtn)
        self.userLogin_btn.setObjectName(u"userLogin_btn")
        self.userLogin_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.userLogin_btn)


        self.verticalLayout_9.addWidget(self.frame_PasswordBtn)


        self.gridLayout_2.addWidget(self.frame_pagePassword, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_password)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frameStackedWidget)


        self.horizontalLayout_3.addWidget(self.frame_mainContent)


        self.verticalLayout_2.addWidget(self.frame_contentBar)

        self.frame_creditBar = QFrame(self.frame_app)
        self.frame_creditBar.setObjectName(u"frame_creditBar")
        self.frame_creditBar.setMinimumSize(QSize(0, 30))
        self.frame_creditBar.setMaximumSize(QSize(16777215, 30))
        self.frame_creditBar.setStyleSheet(u"")
        self.frame_creditBar.setFrameShape(QFrame.StyledPanel)
        self.frame_creditBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_creditBar)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_creditBar)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 10, 0)
        self.label_4 = QLabel(self.frame_36)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_44.addWidget(self.label_4)


        self.horizontalLayout_43.addWidget(self.frame_36, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_creditBar)


        self.gridLayout_3.addWidget(self.frame_app, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.widget_app)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_appLogo.setText("")
        self.label_appTitle.setText(QCoreApplication.translate("MainWindow", u"Inventory Management System", None))
        self.btn_minimizeApp.setText("")
        self.btn_maximizeApp.setText("")
        self.btn_closeApp.setText("")
        self.btn_toggleMenu.setText("")
        self.btn_LMenuToggleText.setText(QCoreApplication.translate("MainWindow", u"Index", None))
        self.btn_stockMenuText.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.btn_receiveMenu.setText("")
        self.btn_receiveMenuText.setText(QCoreApplication.translate("MainWindow", u"Receive", None))
        self.btn_reviewMenu.setText("")
        self.btn_reviewMenuText.setText(QCoreApplication.translate("MainWindow", u"Review", None))
        self.btn_exitMenuText.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.btn_stockConsolidate.setText(QCoreApplication.translate("MainWindow", u"Consolidate", None))
        self.btn_stockExpand.setText(QCoreApplication.translate("MainWindow", u"View All", None))
        self.btn_stock_report.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.groupBox_4.setTitle("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"User Name :", None))
        self.outUserName_txt.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Usage Date :", None))
        self.outInfo_lbl.setText(QCoreApplication.translate("MainWindow", u"Comment :", None))
        self.outInfo_txt.setText("")
        self.outUsage_lbl.setText(QCoreApplication.translate("MainWindow", u"Usage Qty :", None))
        self.outUsage_txt.setText("")
        self.btn_itemOut.setText(QCoreApplication.translate("MainWindow", u"     Deduct from Stock", None))
        self.groupBox_5.setTitle("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Type :", None))
        self.outType_txt.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Code/Name :", None))
        self.outCode_txt.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Batch/SN :", None))
        self.outBatch_txt.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Rig Stock :", None))
        self.outStock_txt.setText("")
        self.outUnit_txt.setText("")
        self.label_30.setText("")
        self.btn_toStandby.setText("")
        self.btn_toStock.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Standby :", None))
        self.outStandby_txt.setText("")
        self.outUnit_txt_2.setText("")
        self.groupBox_7.setTitle("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Type :", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Code/Name :", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Batch/SN :", None))
        self.outInfo_lbl_2.setText(QCoreApplication.translate("MainWindow", u"Description :", None))
        self.inDescription_txt.setText("")
        self.outInfo_lbl_3.setText(QCoreApplication.translate("MainWindow", u"Comment :", None))
        self.inComment_txt.setText("")
        self.groupBox_6.setTitle("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"User Name :", None))
        self.inUserName_txt.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Date Received :", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Received at Rig :", None))
        self.inQty_txt.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Standby :", None))
        self.inTransitQty_txt.setText("")
        self.outUsage_lbl_2.setText(QCoreApplication.translate("MainWindow", u"UOM:", None))
        self.btn_itemIn.setText(QCoreApplication.translate("MainWindow", u"Add to Stock", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Database :", None))
        self.review_db_cmb.setItemText(0, QCoreApplication.translate("MainWindow", u"Received", None))
        self.review_db_cmb.setItemText(1, QCoreApplication.translate("MainWindow", u"Usage", None))

        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Item Type :", None))
        self.review_type_cmb.setItemText(0, QCoreApplication.translate("MainWindow", u"ALL", None))

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Item Code :", None))
        self.review_code_cmb.setItemText(0, QCoreApplication.translate("MainWindow", u"ALL", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Date From :", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Date To :", None))
        self.review_keyword_lbl.setText(QCoreApplication.translate("MainWindow", u"Keywords in Comment (seperated by comma):", None))
        self.review_keyword_txt.setText("")
        self.review_search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.review_report_btn.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User Name :  ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password :  ", None))
        self.label_3.setText("")
        self.appExit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.userLogin_btn.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ver: 1.0-BETA2", None))
    # retranslateUi

