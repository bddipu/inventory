from PySide6 import QtWidgets, QtCore, QtGui
import sqlite3
import datetime

# Custom import
from main import MainWindow
from modules.sideGrip import SideGrip
from modules.qssStyle import appStyle, stockViewStyle, usageStyle
import modules.images

# Glaobal variable
isMaximized = False


class inputHandler(MainWindow):
    # Detect and respond to special key press from keyboard
    def keyCombination(self):
        modifier = QtWidgets.QApplication.keyboardModifiers()
        if modifier == QtCore.Qt.ShiftModifier:
            pass
        
class guiFunction(MainWindow):
    
    def maximize(self):
        global isMaximized
        if not isMaximized:
            self.showMaximized()
            isMaximized = True
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            self.showNormal()
            isMaximized = False
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    def toggleMenu(self, enable):
        width = self.ui.frame_leftMenu.width()
        maxExtend = 200
        standard = 50

        if width == 50:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        self.animation = QtCore.QPropertyAnimation(self.ui.frame_leftMenu, b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def decorateLeftMenu(self, btn):
        btn_Name = btn.objectName()
        frame_Name = btn.parent().objectName()
        if (btn_Name[-4:] == 'Text'):
            btn_Name = btn_Name[:len(btn_Name)-4]

        dormant_btnStyle = """
            QPushButton{
                border-left: 3px solid transparent;
            }
        """
        selected_btnStyle = ' #' + btn_Name + '{border-left: 3px solid red;}'
        selected_frameStyle = ' #' + frame_Name + '{background-color: rgba(0,255,0,100);}'
        reset_menuStyle = dormant_btnStyle + selected_btnStyle + selected_frameStyle
        self.ui.frame_LMenuMdl.setStyleSheet(reset_menuStyle)

        # Show respecti
        if btn_Name == 'btn_userMenu':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_password)
        elif btn_Name == 'btn_stockMenu':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_stockView)
        elif btn_Name == 'btn_exitMenu':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_password)
            self.ui.frame_leftMenu.setMinimumWidth(0)
            self.ui.frame_leftMenu.setMaximumWidth(0)
            self.ui.userName_txt.setText("")
            self.ui.userPass_txt.setText("")
            self.uName = None        

    def updateGrips(self):
        global isMaximized
        if isMaximized: isMaximized = False
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)
    
    # returns names of widgetType objects inside parent widget
    def getWidgetName(self, widgetType, parentWidget):
        for w in parentWidget.findChildren(widgetType):
            widgetName = [name for name in w.objectNme()]
        print (widgetName)

    # Initialization of app during first load
    def uiInit(self):
        # Make window frameless
        self.setWindowFlags(QtCore.Qt.WindowType.WindowSystemMenuHint.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Apply the stylesheet for mai application frame externa file
        self.ui.frame_app.setStyleSheet(appStyle)
        self.ui.frame_pageStockView.setStyleSheet(stockViewStyle)
        self.ui.frame_pageUsage.setStyleSheet(usageStyle)
        
        # Move the window with top bar
        def moveWindow(event):
            global isMaximized
            if isMaximized: return
            if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()
        self.ui.frame_titleBar.mouseMoveEvent = moveWindow
        
        # Maximize window by double clicking top bar
        def doubleClickMaximize(event):
            QtCore.QTimer.singleShot(250, lambda: guiFunction.maximize(self))
        self.ui.frame_titleBar.mouseDoubleClickEvent = doubleClickMaximize


        # Define the custom grips. Diagonal grips incorporated in top and bottom
        self.left_grip = SideGrip(self, QtCore.Qt.LeftEdge)
        self.right_grip = SideGrip(self, QtCore.Qt.RightEdge)
        self.top_grip = SideGrip(self, QtCore.Qt.TopEdge)
        self.bottom_grip = SideGrip(self, QtCore.Qt.BottomEdge)

        # Modify QTableViews
        # self.ui.item_tbl.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.item_tbl.verticalHeader().setVisible(False)
        self.ui.item_tbl.horizontalHeader().setStretchLastSection(True)
        self.ui.item_tbl.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.item_tbl.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.item_tbl.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # Signal-socket for close. minimize, maximize button
        self.ui.btn_closeApp.clicked.connect(lambda:self.close())
        self.ui.btn_minimizeApp.clicked.connect(lambda:self.showMinimized())
        self.ui.btn_maximizeApp.clicked.connect(lambda:guiFunction.maximize(self))

        # Signal-socket for buttons on left side menu
        self.ui.btn_toggleMenu.clicked.connect(lambda:guiFunction.toggleMenu(self, True))
        self.ui.btn_LMenuToggleText.clicked.connect(lambda:guiFunction.toggleMenu(self, True))
        self.ui.btn_userMenu.clicked.connect(self.menuItemSelected)
        self.ui.btn_userMenuText.clicked.connect(self.menuItemSelected)
        self.ui.btn_stockMenu.clicked.connect(self.menuItemSelected)
        self.ui.btn_stockMenuText.clicked.connect(self.menuItemSelected)
        self.ui.btn_exitMenu.clicked.connect(self.menuItemSelected)
        self.ui.btn_exitMenuText.clicked.connect(self.menuItemSelected)
        
        # initializing stacked-widget's password page
        self.ui.userLogin_btn.clicked.connect(lambda:appFunction.authenticate(self))
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_password)
        
        # Signal-socket for stacked-widget's stock page
        self.ui.btn_stockConsolidate.clicked.connect(lambda:appFunction.consolidate(self))
        self.ui.itemList_cmb.currentTextChanged.connect(lambda:appFunction.itemTypeChanged(self))
        self.ui.itemList_cmb.activated.connect(lambda:appFunction.itemTypeChanged(self))
        self.ui.item_tbl.cellDoubleClicked.connect(lambda: appFunction.item_tbl_dblClicked(self))

        self.ui.frame_leftMenu.setMinimumWidth(0)
        self.ui.frame_leftMenu.setMaximumWidth(0)

     
class appFunction(MainWindow):
   
    # data load from SQLite to pandas dataframe 
    def appInit(self):
        with sqlite3.connect('db\\invRig.db') as conn:
            sqlQuery = f"SELECT DISTINCT type FROM rigInv ORDER BY type"
            c = conn.cursor()
            c.execute(sqlQuery)
            val = c.fetchall()
            self.ui.itemList_cmb.clear()
            self.ui.itemList_cmb.insertItems(0, [i[0] for i in val])
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_stockView)
        # self.ui.outDate_dt.setDate(QtCore.QDate.currentDate())
        # self.ui.inDate_dt.setDate(QtCore.QDate.currentDate())

    # Authenticate user or add user or change password
    def authenticate(self):       
        uName=str(self.ui.userName_txt.text()).strip()
        uPass=str(self.ui.userPass_txt.text()).strip()
        # Do not continue if username ot password left empty
        if (uName in ['',None,'Nan']) | (uPass in ['',None,'Nan']) : return
        # Get username from database
        with sqlite3.connect('db\\invRig.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM appuser")
            uData = c.fetchall()
        
        for x in [datetime.datetime.now()]:
            mPass = str((x.year*x.month*x.day*1979))[-6:]

        for uRows in uData:
            if uName == uRows[0]:
                if (uPass == uRows[1]) | (uPass == str(mPass)):
                    self.uName = uName
                    appFunction.appInit(self)
                    guiFunction.toggleMenu(self, True)
                    return
                else:
                    uMessage = QtWidgets.QMessageBox().question(self, ' Password error', "Wrong password. Do you want to reset the " \
                        + "password with provided one?")
                    if uMessage == QtWidgets.QMessageBox.Yes:
                        response, status = QtWidgets.QInputDialog.getText(self, 'Admin Authentication', 'Enter Admin Password:')
                        if status:
                            if str(response).strip() != mPass: 
                                QtWidgets.QMessageBox().critical(self, 'Password Error', 'Wrong admin password. Password not changed.')
                                return
                            else:                        
                                sqlQuery = f"UPDATE appuser SET upass='{uPass}' WHERE uname='{uName}'"
                                with sqlite3.connect('db\\invRig.db') as conn:
                                    c = conn.cursor()
                                    c.execute(sqlQuery)
                                    conn.commit()
                                return
                        else: return
                    else: return
        else:
            # If user doesn't exist, offer to add one
            uMessage = QtWidgets.QMessageBox().question(self, ' Invalid User', "User doesn't exist. Do you want to add a new user?")
            if uMessage == QtWidgets.QMessageBox.Yes:
                response, status = QtWidgets.QInputDialog.getText(self, 'Admin Authentication', 'Enter Admin Password:')
                if status:
                    if str(response).strip() != mPass: 
                        QtWidgets.QMessageBox().critical(self, 'Password Error', 'Wrong admin password. User not added.')
                        return
                    else:
                        sqlQuery = f"INSERT INTO appuser VALUES ('{uName}', '{uPass}')"
                        with sqlite3.connect('db\\invRig.db') as conn:
                            c = conn.cursor()
                            c.execute(sqlQuery)
                            conn.commit()
                        return
                else: return
            else: return
    
    # slot of signal from 'itemList' combo box
    def itemTypeChanged(self):
        itemType = str(self.ui.itemList_cmb.currentText())
        with sqlite3.connect('db\\invRig.db') as conn:
            qtColName = ['Code','Description','Batch','Rig Quantity','Standby Qty','UOM', 'Comment']
            sqlQuery = f"SELECT code, description, batch, rig_qty, transit_qty, uom, comment " \
                f"FROM rigInv WHERE type='{itemType}' AND ((rig_qty !=0) OR (transit_qty != 0)) ORDER BY code"
            appFunction.fillTable_sql(self, conn, sqlQuery, self.ui.item_tbl, qtColName)

    def fillTable_sql(self, sqlConn, sqlQuery, qtTable, qtColName):
        c = sqlConn.cursor()
        c.execute(sqlQuery)
        allData = c.fetchall() 
        # Counts no of rows, columns n dataset
        if allData: 
            noOfColumns = len(list(allData[0]))
        else:
            qtTable.clear()
            qtTable.setColumnCount(0)
            qtTable.setRowCount(0)
            return   
        noOfRows = len(allData)

        for x in [qtTable]:
            x.clear()
            x.setColumnCount(noOfColumns)
            x.setRowCount(noOfRows)
            x.setHorizontalHeaderLabels(qtColName)
            x.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
            for i in range(noOfRows):
                for j in range(noOfColumns):
                    x.setItem(i,j,QtWidgets.QTableWidgetItem(str(allData[i][j])))
            x.resizeColumnsToContents()
            x.verticalHeader().setDefaultSectionSize(x.rowHeight(15))

    # Check if a string can be converted to integer
    def canConv(self,a):
        try:
            int(float(a))
            return True
        except ValueError:
            return False 
    # Get user input and write incoming invetory details to database
    def toReceivedTable(self):
        iType = str(self.ui.inType_cmb.currentText()).strip()
        iCode = str(self.ui.inCode_cmb.currentText()).strip()
        iBatch = str(self.ui.inBatch_cmb.currentText()).strip()
        iDesc = str(self.ui.inDescription_txt.text()).strip()
        iComm = str(self.ui.inComment_txt.text()).strip()
        iDate = str(self.ui.inDate_dt.date().toPyDate()).strip()
        iUnit = str(self.ui.inUnit_cmb.currentText()).strip()
        iQty = str(self.ui.inQty_txt.text()).strip()
        iStandby = str(self.ui.inTransitQty_txt.text()).strip()

        # Check if there are any empty or wrong input
        iValue = [iType, iCode, iBatch, iDesc, iComm, iDate, iUnit, iQty, iStandby, self.uName]
        checkValue = [None, '']
        if len(list(set(iValue).intersection(set(checkValue)))):
            QtWidgets.QMessageBox().critical(self, 'Input Error', 'All fields are mandatory and cannot be left empty.')
            return
        if not (self.canConv(iQty) & self.canConv(iStandby)):
            QtWidgets.QMessageBox().critical(self, 'Input Error', 'Quantities must need to be number.')
            return
        
        # update rigInv table and received table
        with sqlite3.connect('db\\invRig.db') as conn:
            # Check for same batch at the rig
            sqlQuery = f"SELECT batch, rig_qty, transit_qty FROM rigInv WHERE "\
                f"type='{iType}' AND code='{iCode}' AND batch='{iBatch}' "\
                    f"AND ((rig_qty !=0) OR (transit_qty != 0)) "
            c = conn.cursor()
            c.execute(sqlQuery)
            sqlData = c.fetchall()

            if (sqlData):
                # if qty from same batch exists at rig or standby vessel
                totalRigQty = float(sqlData[0][1]) + float(iQty)
                totalStandbyQty = float(sqlData[0][2]) + float(iStandby)
                sqlQuery = f"UPDATE rigInv SET rig_qty=?, transit_qty=? " \
                    f"WHERE type=? AND code=? AND batch=?"
                sqlValues = [totalRigQty, totalStandbyQty, iType, iCode, iBatch]
            else:
                # if the received batch is a new bacth at rig
                totalRigQty = float(iQty)
                totalStandbyQty = float(iStandby)
                sqlQuery = f"INSERT INTO rigInv VALUES (?,?,?,?,?,?,?,?)"
                sqlValues = [iType, iCode, iDesc, iBatch, iQty, iStandby, iUnit, iComm]          
            
            c.execute(sqlQuery,sqlValues)
            conn.commit()
            
            sqlQuery = f"INSERT INTO received VALUES (?,?,?,?,?,?,?,?,?,?)"
            sqlValues = [iDate, iType, iCode, iBatch, iDesc, iComm, iUnit, iQty, iStandby, self.uName]
            c.execute(sqlQuery,sqlValues)
            conn.commit()
        
        self.initializeForm() # Reset inventory table
        self.inCancelButton_Clicked() # Reset inventoryIn page

    # slot for signal from 'consolidate' button
    def consolidate(self):
        itemType = str(self.ui.itemList_cmb.currentText())
        with sqlite3.connect('db\\invRig.db') as conn:
            qtColName = ['Code','Rig Qty','Standby']
            sqlQuery = f"SELECT code, SUM(rig_qty), SUM(transit_qty)" \
                f"FROM rigInv WHERE type='{itemType}' AND ((rig_qty !=0) OR (transit_qty != 0)) " \
                    f"GROUP BY code"       
            appFunction.fillTable_sql(self, conn, sqlQuery, self.ui.item_tbl, qtColName)


    # Update option for NON-KEY data in stock view table
    def item_tbl_dblClicked(self):
        cRow = self.ui.item_tbl.currentRow()
        cColumn = self.ui.item_tbl.currentColumn()
        if ((self.ui.item_tbl.columnCount() != 7) & (cRow >= 0)): return
        cValue = self.ui.item_tbl.item(cRow,cColumn).text()
        if cColumn in [1,5,6]:
            response, status = QtWidgets.QInputDialog.getText(self, 'Update', 'Enter new value:', 
                QtWidgets.QLineEdit.Normal,cValue)
            if status:
                if response in ['',cValue,None]: 
                    return
                else:
                    dataPair = {1:'description', 5:'uom', 6:'comment'}
                    dType = self.ui.itemList_cmb.currentText()
                    dCode = self.ui.item_tbl.item(cRow,0).text()
                    dBatch = self.ui.item_tbl.item(cRow,2).text()
                    with sqlite3.connect('db\\invRig.db') as conn:
                        sqlQuery = f"UPDATE rigInv SET {dataPair[cColumn]}=? " \
                            f"WHERE type=? AND code=? AND batch=?"
                        sqlValues = [response, dType, dCode, dBatch]
                        c = conn.cursor()
                        c.execute(sqlQuery, sqlValues)
                        conn.commit()
                        self.ui.item_tbl.item(cRow,cColumn).setText(response)
                        # appFunction.appInit(self)
            else: return
        else:
            appFunction.itemOutButton_Clicked(self)
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_usage)

    

    def itemOutButton_Clicked(self):
        dfTable = self.ui.item_tbl
        cRow = dfTable.currentRow()
        if ((self.ui.item_tbl.columnCount() != 6) & (cRow >= 0)): # execure below only if data are not in consolidated form
            for x in [dfTable]:
                self.ui.outType_txt.setText(self.ui.itemList_cmb.currentText())
                self.ui.outCode_txt.setText(x.item(cRow,0).text())
                self.ui.outBatch_txt.setText(x.item(cRow,2).text())
                self.ui.outStock_txt.setText(x.item(cRow,3).text())
                self.ui.outStandby_txt.setText(x.item(cRow,4).text())
                # self.ui.outUnit_txt.setText(x.item(cRow,5).text())
                self.ui.outUserName_txt.setText(self.uName)

                iCode = str(self.ui.outCode_txt.text())
                with sqlite3.connect('db\\invRig.db') as conn: 
                    qtColName = ['Date', 'Code', 'Batch', 'Usage','UOM', 'Purpose', 'Received By']
                    sqlQuery = f"SELECT date, code, batch, usage, uom, "\
                        f"purpose, usedby FROM usage WHERE code='{iCode}'"
                    # self.fillTable_sql(conn, sqlQuery, self.ui.usage_tbl, qtColName)

                # self.ui.stackedWidget.setCurrentIndex(3)