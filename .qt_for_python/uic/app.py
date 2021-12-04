# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 501)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(900, 500))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_app = QFrame(self.centralwidget)
        self.frame_app.setObjectName(u"frame_app")
        self.frame_app.setStyleSheet(u"")
        self.frame_app.setFrameShape(QFrame.StyledPanel)
        self.frame_app.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_app)
        self.verticalLayout_2.setSpacing(0)
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
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_appLogo = QFrame(self.frame_titleBar)
        self.frame_appLogo.setObjectName(u"frame_appLogo")
        self.frame_appLogo.setMinimumSize(QSize(50, 40))
        self.frame_appLogo.setMaximumSize(QSize(50, 40))
        self.frame_appLogo.setFrameShape(QFrame.NoFrame)
        self.frame_appLogo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_appLogo)
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
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_appTitle = QLabel(self.frame_appTitle)
        self.label_appTitle.setObjectName(u"label_appTitle")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_appTitle.setFont(font1)
        self.label_appTitle.setStyleSheet(u"#label_appTitle {\n"
"	color: rgba(255, 255, 255,200);\n"
"}")

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
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.btn_minimizeApp = QPushButton(self.frame_appTitleBtn)
        self.btn_minimizeApp.setObjectName(u"btn_minimizeApp")
        self.btn_minimizeApp.setMinimumSize(QSize(25, 25))
        self.btn_minimizeApp.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizeApp.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_minimizeApp)

        self.btn_maximizeApp = QPushButton(self.frame_appTitleBtn)
        self.btn_maximizeApp.setObjectName(u"btn_maximizeApp")
        self.btn_maximizeApp.setMinimumSize(QSize(25, 25))
        self.btn_maximizeApp.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximizeApp.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_maximizeApp)

        self.btn_closeApp = QPushButton(self.frame_appTitleBtn)
        self.btn_closeApp.setObjectName(u"btn_closeApp")
        self.btn_closeApp.setMinimumSize(QSize(25, 25))
        self.btn_closeApp.setMaximumSize(QSize(25, 25))
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
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_leftMenu = QFrame(self.frame_contentBar)
        self.frame_leftMenu.setObjectName(u"frame_leftMenu")
        self.frame_leftMenu.setMinimumSize(QSize(0, 0))
        self.frame_leftMenu.setMaximumSize(QSize(0, 16777215))
        self.frame_leftMenu.setFrameShape(QFrame.NoFrame)
        self.frame_leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_leftMenu)
        self.verticalLayout_4.setSpacing(0)
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

        self.label_toggleMenu = QLabel(self.frame_toggleInner)
        self.label_toggleMenu.setObjectName(u"label_toggleMenu")
        self.label_toggleMenu.setMinimumSize(QSize(150, 45))
        self.label_toggleMenu.setMaximumSize(QSize(150, 45))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_toggleMenu.setFont(font2)
        self.label_toggleMenu.setIndent(15)

        self.horizontalLayout_5.addWidget(self.label_toggleMenu)


        self.verticalLayout_5.addWidget(self.frame_toggleInner)


        self.verticalLayout_4.addWidget(self.frame_toggle)

        self.frame_LMenuMdl = QFrame(self.frame_leftMenu)
        self.frame_LMenuMdl.setObjectName(u"frame_LMenuMdl")
        self.frame_LMenuMdl.setMinimumSize(QSize(200, 0))
        self.frame_LMenuMdl.setMaximumSize(QSize(200, 16777215))
        self.frame_LMenuMdl.setFrameShape(QFrame.NoFrame)
        self.frame_LMenuMdl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_LMenuMdl)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_user = QFrame(self.frame_LMenuMdl)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setMinimumSize(QSize(200, 45))
        self.frame_user.setMaximumSize(QSize(200, 45))
        self.frame_user.setBaseSize(QSize(0, 45))
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_userMenu = QPushButton(self.frame_user)
        self.btn_userMenu.setObjectName(u"btn_userMenu")
        self.btn_userMenu.setEnabled(True)
        self.btn_userMenu.setMinimumSize(QSize(50, 45))
        self.btn_userMenu.setMaximumSize(QSize(50, 45))
        self.btn_userMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_userMenu.setFocusPolicy(Qt.TabFocus)
        self.btn_userMenu.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_userMenu.setIcon(icon4)
        self.btn_userMenu.setFlat(False)

        self.horizontalLayout_4.addWidget(self.btn_userMenu)

        self.label_userMenu = QLabel(self.frame_user)
        self.label_userMenu.setObjectName(u"label_userMenu")
        self.label_userMenu.setMinimumSize(QSize(150, 45))
        self.label_userMenu.setMaximumSize(QSize(150, 45))
        self.label_userMenu.setFont(font2)
        self.label_userMenu.setIndent(15)

        self.horizontalLayout_4.addWidget(self.label_userMenu)


        self.verticalLayout_6.addWidget(self.frame_user)

        self.frame_stockMenu = QFrame(self.frame_LMenuMdl)
        self.frame_stockMenu.setObjectName(u"frame_stockMenu")
        self.frame_stockMenu.setMinimumSize(QSize(200, 45))
        self.frame_stockMenu.setMaximumSize(QSize(200, 45))
        self.frame_stockMenu.setBaseSize(QSize(0, 45))
        self.frame_stockMenu.setFrameShape(QFrame.NoFrame)
        self.frame_stockMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_stockMenu)
        self.horizontalLayout_6.setSpacing(0)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-view-column.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stockMenu.setIcon(icon5)
        self.btn_stockMenu.setFlat(False)

        self.horizontalLayout_6.addWidget(self.btn_stockMenu)

        self.label_stockMenu = QLabel(self.frame_stockMenu)
        self.label_stockMenu.setObjectName(u"label_stockMenu")
        self.label_stockMenu.setMinimumSize(QSize(150, 45))
        self.label_stockMenu.setMaximumSize(QSize(150, 45))
        self.label_stockMenu.setFont(font2)
        self.label_stockMenu.setIndent(15)

        self.horizontalLayout_6.addWidget(self.label_stockMenu)


        self.verticalLayout_6.addWidget(self.frame_stockMenu)

        self.frame_LMenuExit = QFrame(self.frame_LMenuMdl)
        self.frame_LMenuExit.setObjectName(u"frame_LMenuExit")
        self.frame_LMenuExit.setMinimumSize(QSize(200, 45))
        self.frame_LMenuExit.setMaximumSize(QSize(200, 45))
        self.frame_LMenuExit.setBaseSize(QSize(0, 45))
        self.frame_LMenuExit.setFrameShape(QFrame.NoFrame)
        self.frame_LMenuExit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_LMenuExit)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_LMenuExit = QPushButton(self.frame_LMenuExit)
        self.btn_LMenuExit.setObjectName(u"btn_LMenuExit")
        self.btn_LMenuExit.setEnabled(True)
        self.btn_LMenuExit.setMinimumSize(QSize(50, 45))
        self.btn_LMenuExit.setMaximumSize(QSize(50, 45))
        self.btn_LMenuExit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_LMenuExit.setFocusPolicy(Qt.TabFocus)
        self.btn_LMenuExit.setStyleSheet(u"")
        self.btn_LMenuExit.setText(u"")
        self.btn_LMenuExit.setIcon(icon5)
        self.btn_LMenuExit.setFlat(False)

        self.horizontalLayout_13.addWidget(self.btn_LMenuExit)

        self.label_LMenuExit = QLabel(self.frame_LMenuExit)
        self.label_LMenuExit.setObjectName(u"label_LMenuExit")
        self.label_LMenuExit.setMinimumSize(QSize(150, 45))
        self.label_LMenuExit.setMaximumSize(QSize(150, 45))
        self.label_LMenuExit.setFont(font2)
        self.label_LMenuExit.setIndent(15)

        self.horizontalLayout_13.addWidget(self.label_LMenuExit)


        self.verticalLayout_6.addWidget(self.frame_LMenuExit)


        self.verticalLayout_4.addWidget(self.frame_LMenuMdl, 0, Qt.AlignTop)

        self.frame_LMenuBtm = QFrame(self.frame_leftMenu)
        self.frame_LMenuBtm.setObjectName(u"frame_LMenuBtm")
        self.frame_LMenuBtm.setFrameShape(QFrame.NoFrame)
        self.frame_LMenuBtm.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_LMenuBtm)


        self.horizontalLayout_3.addWidget(self.frame_leftMenu)

        self.frame_mainContent = QFrame(self.frame_contentBar)
        self.frame_mainContent.setObjectName(u"frame_mainContent")
        self.frame_mainContent.setFrameShape(QFrame.NoFrame)
        self.frame_mainContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_mainContent)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frameStackedWidget = QFrame(self.frame_mainContent)
        self.frameStackedWidget.setObjectName(u"frameStackedWidget")
        self.frameStackedWidget.setFrameShape(QFrame.NoFrame)
        self.frameStackedWidget.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frameStackedWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frameStackedWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_stockView = QWidget()
        self.page_stockView.setObjectName(u"page_stockView")
        self.verticalLayout_11 = QVBoxLayout(self.page_stockView)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_pageStockView = QFrame(self.page_stockView)
        self.frame_pageStockView.setObjectName(u"frame_pageStockView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_pageStockView.sizePolicy().hasHeightForWidth())
        self.frame_pageStockView.setSizePolicy(sizePolicy)
        self.frame_pageStockView.setFrameShape(QFrame.StyledPanel)
        self.frame_pageStockView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_pageStockView)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_tableStock = QFrame(self.frame_pageStockView)
        self.frame_tableStock.setObjectName(u"frame_tableStock")
        self.frame_tableStock.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #6272a4;\n"
"	/*max-width: 30px;*/\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #6272a4;\n"
"    font: 14pt \"Segoe UI\";\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"	background-color: #6272a4;\n"
"	padding-top:5px;\n"
"    padding-bottom: 10px;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #f8f8f2;\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
""
                        "QTableWidget::verticalHeader {	\n"
"	background-color: #6272a4;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"	background-color: #6272a4;\n"
"	padding-top: 3px;\n"
"    padding-bottom: 3px;\n"
"	padding-left: 10px;\n"
"    padding-right: 3px;\n"
"	color: #f8f8f2;\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"")
        self.frame_tableStock.setFrameShape(QFrame.StyledPanel)
        self.frame_tableStock.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_tableStock)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.item_tbl = QTableWidget(self.frame_tableStock)
        if (self.item_tbl.columnCount() < 7):
            self.item_tbl.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.item_tbl.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.item_tbl.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.item_tbl.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.item_tbl.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.item_tbl.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.item_tbl.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.item_tbl.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.item_tbl.rowCount() < 9):
            self.item_tbl.setRowCount(9)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.item_tbl.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.item_tbl.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.item_tbl.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.item_tbl.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.item_tbl.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.item_tbl.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.item_tbl.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.item_tbl.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.item_tbl.setVerticalHeaderItem(8, __qtablewidgetitem15)
        self.item_tbl.setObjectName(u"item_tbl")

        self.verticalLayout_7.addWidget(self.item_tbl)


        self.verticalLayout_12.addWidget(self.frame_tableStock)

        self.frame_btnStock = QFrame(self.frame_pageStockView)
        self.frame_btnStock.setObjectName(u"frame_btnStock")
        self.frame_btnStock.setMinimumSize(QSize(0, 50))
        self.frame_btnStock.setMaximumSize(QSize(16777215, 50))
        self.frame_btnStock.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: #6272a4;\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////"
                        "////////////////////////////////////\n"
"Button */\n"
"QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"    font: 12pt \"Segoe UI\";\n"
"    padding: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"")
        self.frame_btnStock.setFrameShape(QFrame.NoFrame)
        self.frame_btnStock.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_btnStock)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_btnStock)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.itemList_cmb = QComboBox(self.frame_2)
        self.itemList_cmb.setObjectName(u"itemList_cmb")

        self.verticalLayout_10.addWidget(self.itemList_cmb)


        self.horizontalLayout_7.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_btnStock)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_11.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_11.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_11.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_11.addWidget(self.pushButton_3)


        self.horizontalLayout_7.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_btnStock)


        self.verticalLayout_11.addWidget(self.frame_pageStockView)

        self.stackedWidget.addWidget(self.page_stockView)
        self.page_password = QWidget()
        self.page_password.setObjectName(u"page_password")
        self.gridLayout_2 = QGridLayout(self.page_password)
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
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_uName)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 45))
        self.label.setMaximumSize(QSize(120, 45))
        font3 = QFont()
        font3.setPointSize(14)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label)

        self.userName_txt = QLineEdit(self.frame_uName)
        self.userName_txt.setObjectName(u"userName_txt")
        self.userName_txt.setMinimumSize(QSize(0, 45))
        self.userName_txt.setMaximumSize(QSize(16777215, 45))
        self.userName_txt.setFont(font3)
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
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_uName_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 45))
        self.label_2.setMaximumSize(QSize(120, 45))
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_2)

        self.userPass_txt = QLineEdit(self.frame_uName_2)
        self.userPass_txt.setObjectName(u"userPass_txt")
        self.userPass_txt.setMinimumSize(QSize(0, 45))
        self.userPass_txt.setMaximumSize(QSize(16777215, 45))
        self.userPass_txt.setFont(font3)
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
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_PasswordBtn)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.pushButton_5)

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

        self.verticalLayout_2.addWidget(self.frame_creditBar)


        self.verticalLayout.addWidget(self.frame_app)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


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
        self.label_toggleMenu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_userMenu.setText("")
        self.label_userMenu.setText(QCoreApplication.translate("MainWindow", u"User Login", None))
        self.label_stockMenu.setText(QCoreApplication.translate("MainWindow", u"Stock View", None))
        self.label_LMenuExit.setText(QCoreApplication.translate("MainWindow", u"Stock View", None))
        ___qtablewidgetitem = self.item_tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem1 = self.item_tbl.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem2 = self.item_tbl.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Batch", None));
        ___qtablewidgetitem3 = self.item_tbl.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Rig Qty", None));
        ___qtablewidgetitem4 = self.item_tbl.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Standby Qty", None));
        ___qtablewidgetitem5 = self.item_tbl.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"UOM", None));
        ___qtablewidgetitem6 = self.item_tbl.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Comment", None));
        ___qtablewidgetitem7 = self.item_tbl.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Row 1", None));
        ___qtablewidgetitem8 = self.item_tbl.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Row 2", None));
        ___qtablewidgetitem9 = self.item_tbl.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Row 3", None));
        ___qtablewidgetitem10 = self.item_tbl.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Row 4", None));
        ___qtablewidgetitem11 = self.item_tbl.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Row 5", None));
        ___qtablewidgetitem12 = self.item_tbl.verticalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Row 6", None));
        ___qtablewidgetitem13 = self.item_tbl.verticalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Row 7", None));
        ___qtablewidgetitem14 = self.item_tbl.verticalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Row 8", None));
        ___qtablewidgetitem15 = self.item_tbl.verticalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Row 9", None));
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Consolidate", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Receive", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User Name :  ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password :  ", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.userLogin_btn.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
    # retranslateUi

