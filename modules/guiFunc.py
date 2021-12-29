from PySide6 import QtWidgets, QtCore, QtGui
import sqlite3
import datetime

# Custom import
from main import MainWindow
from modules.sideGrip import SideGrip
from modules.qssStyle import appStyle, stockViewStyle, usageStyle, receiveStyle
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
        if btn_Name == 'btn_receiveMenu':
            self.ui.stackedWidget.setCurrentWidget(self.ui.pageReceive)
            self.ui.inUserName_txt.setText(self.uName)
        elif btn_Name == 'btn_stockMenu':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_stockView)
        elif btn_Name == 'btn_reviewMenu':
            pass
            #self.ui.stackedWidget.setCurrentWidget(self.ui.pageReview)
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
        
        # Apply the stylesheet for main application frame external file
        self.ui.frame_app.setStyleSheet(appStyle)
        self.ui.frame_pageStockView.setStyleSheet(stockViewStyle)
        self.ui.frame_pageUsage.setStyleSheet(usageStyle)
        self.ui.frame_pageReceive.setStyleSheet(receiveStyle)
        
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
        self.ui.usage_tbl.verticalHeader().setVisible(False)
        self.ui.usage_tbl.horizontalHeader().setStretchLastSection(True)
        self.ui.usage_tbl.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.usage_tbl.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.usage_tbl.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.received_tbl.verticalHeader().setVisible(False)
        self.ui.received_tbl.horizontalHeader().setStretchLastSection(True)
        self.ui.received_tbl.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.received_tbl.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.received_tbl.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # Signal-socket for close. minimize, maximize button
        self.ui.btn_closeApp.clicked.connect(lambda:self.close())
        self.ui.btn_minimizeApp.clicked.connect(lambda:self.showMinimized())
        self.ui.btn_maximizeApp.clicked.connect(lambda:guiFunction.maximize(self))

        # Signal-socket for buttons on left side menu
        self.ui.btn_toggleMenu.clicked.connect(lambda:guiFunction.toggleMenu(self, True))
        self.ui.btn_LMenuToggleText.clicked.connect(lambda:guiFunction.toggleMenu(self, True))
        self.ui.btn_receiveMenu.clicked.connect(self.menuItemSelected)
        self.ui.btn_receiveMenuText.clicked.connect(self.menuItemSelected)
        self.ui.btn_reviewMenu.clicked.connect(self.menuItemSelected)
        self.ui.btn_reviewMenuText.clicked.connect(self.menuItemSelected)
        self.ui.btn_stockMenu.clicked.connect(self.menuItemSelected)
        self.ui.btn_stockMenuText.clicked.connect(self.menuItemSelected)
        self.ui.btn_exitMenu.clicked.connect(self.menuItemSelected)
        self.ui.btn_exitMenuText.clicked.connect(self.menuItemSelected)
        
        # initializing stacked-widget's password page
        self.ui.userLogin_btn.clicked.connect(lambda:appFunction.authenticate(self))
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_password)
        self.ui.userPass_txt.returnPressed.connect(lambda:appFunction.authenticate(self))
        self.ui.appExit_btn.clicked.connect(lambda:appFunction.appClose(self))

        
        # Signal-socket for stacked-widget's stock page
        self.ui.btn_stockConsolidate.clicked.connect(lambda:appFunction.consolidate(self))
        self.ui.itemList_cmb.currentTextChanged.connect(lambda:appFunction.itemTypeChanged(self))
        self.ui.itemList_cmb.activated.connect(lambda:appFunction.itemTypeChanged(self))
        self.ui.item_tbl.cellDoubleClicked.connect(lambda: appFunction.item_tbl_dblClicked(self))

        # Signal-socket for stacked-widget's usage page
        self.ui.btn_toStock.clicked.connect(lambda:appFunction.outMoveToStock_clicked(self))
        self.ui.btn_toStandby.clicked.connect(lambda:appFunction.outMoveToStandby_clicked(self))
        self.ui.btn_itemOut.clicked.connect(lambda:appFunction.outDeductButton_Clicked(self))

        # Signal-socket for stacked-widget's receive page
        self.ui.inType_cmb.currentTextChanged.connect(lambda:appFunction.inTypeCombo_Change(self))
        self.ui.inCode_cmb.currentTextChanged.connect(lambda:appFunction.inCodeCombo_Change(self))
        self.ui.inBatch_cmb.currentTextChanged.connect(lambda:appFunction.inBatchCombo_Change(self))
        self.ui.inBatch_cmb.activated.connect(lambda:appFunction.inBatchCombo_Change(self))
        self.ui.btn_itemIn.clicked.connect(lambda:appFunction.toReceivedTable(self))

        self.ui.frame_leftMenu.setMinimumWidth(0)
        self.ui.frame_leftMenu.setMaximumWidth(0)

     
class appFunction(MainWindow):
   
    def appClose(self):
        self.close()

    # data load from SQLite to pandas dataframe 
    def appInit(self):
        with sqlite3.connect('db\\invRig.db') as conn:
            sqlQuery = f"SELECT DISTINCT type FROM rigInv ORDER BY type"
            c = conn.cursor()
            c.execute(sqlQuery)
            val = c.fetchall()
            self.ui.itemList_cmb.clear()
            self.ui.itemList_cmb.insertItems(0, [i[0] for i in val])
        self.ui.outDate_dt.setDate(QtCore.QDate.currentDate())
        self.ui.inDate_dt.setDate(QtCore.QDate.currentDate())
        
        itemTypes = ['Bulk', 'Additive', 'Tool', 'Consumable', 'Equipment', 'Other']
        self.ui.inType_cmb.clear()
        self.ui.inType_cmb.insertItems(0, itemTypes)
        

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
                    self.ui.stackedWidget.setCurrentWidget(self.ui.page_stockView)
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
        iDate = str(self.ui.inDate_dt.date().toPython()).strip()
        iUnit = str(self.ui.inUnit_cmb.currentText()).strip()
        iQty = str(self.ui.inQty_txt.text()).strip()
        iStandby = str(self.ui.inTransitQty_txt.text()).strip()

        # Check if there are any empty or wrong input
        iValue = [iType, iCode, iBatch, iDesc, iComm, iDate, iUnit, iQty, iStandby, self.uName]
        checkValue = [None, '']
        if len(list(set(iValue).intersection(set(checkValue)))):
            QtWidgets.QMessageBox().critical(self, 'Input Error', 'All fields are mandatory and cannot be left empty.')
            return
        if not (appFunction.canConv(self, iQty) & appFunction.canConv(self, iStandby)):
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
            try:
                conn.commit()
            
                QtWidgets.QMessageBox().information(self,'Success','Entry added to inventory.')
                #appFunction.appInit(self) # Reset inventory table
                appFunction.itemTypeChanged(self)
                self.ui.inCode_cmb.clear()
                self.ui.inBatch_cmb.clear()
                self.ui.inDescription_txt.setText('')
                self.ui.inComment_txt.setText('')
                self.ui.inUnit_cmb.clear()
                self.ui.inQty_txt.setText('')
                self.ui.inTransitQty_txt.setText('')
                self.ui.received_tbl.setRowCount(0)
                self.ui.received_tbl.setColumnCount(0)
            except:
                QtWidgets.QMessageBox().critical(self,'Error','An error occured while attempting to add record.')


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
                self.ui.outUnit_txt.setText(x.item(cRow,5).text())
                self.ui.outUnit_txt_2.setText(x.item(cRow,5).text())
                self.ui.outUserName_txt.setText(self.uName)
                self.ui.outUsage_txt.setText('')
                self.ui.outInfo_txt.setText('')

                iCode = str(self.ui.outCode_txt.text())
                with sqlite3.connect('db\\invRig.db') as conn: 
                    qtColName = ['Date', 'Code', 'Batch', 'Usage','UOM', 'Comment', 'Used By']
                    sqlQuery = f"SELECT date, code, batch, usage, uom, "\
                        f"purpose, usedby FROM usage WHERE code='{iCode}'"
                    appFunction.fillTable_sql(self, conn, sqlQuery, self.ui.usage_tbl, qtColName)

                # self.ui.stackedWidget.setCurrentIndex(3)

    def outMoveToStock_clicked(self):
        response, status = QtWidgets.QInputDialog.getText(self, 'Enter Quantity', 'Quantity to transfer:')
        if status:
            if appFunction.canConv(self, response):
                mQty = float(response)
                oStandby = float(str(self.ui.outStandby_txt.text()).strip())
                if mQty>oStandby:
                    QtWidgets.QMessageBox().critical(self,'Error','Transfer quantity cannot be more than current standby quantity.')
                    return
                else:
                    oStock = float(str(self.ui.outStock_txt.text()).strip())
                    oType = str(self.ui.outType_txt.text()).strip()
                    oCode = str(self.ui.outCode_txt.text()).strip()
                    oBatch = str(self.ui.outBatch_txt.text()).strip()
                
                    rStock = oStock + mQty
                    rStandby = oStandby - mQty

                    with sqlite3.connect('db\\invRig.db') as conn:
                        sqlQuery = f"UPDATE rigInv SET rig_qty=?, transit_qty=? " \
                            f"WHERE type=? AND code=? AND batch=?"
                        sqlValues = [rStock, rStandby, oType, oCode, oBatch]
                        c = conn.cursor()
                        c.execute(sqlQuery, sqlValues)
                        conn.commit()
                        appFunction.appInit(self)
                        self.ui.outStock_txt.setText(str(rStock))
                        self.ui.outStandby_txt.setText(str(rStandby))
            else:
                QtWidgets.QMessageBox().critical(self,'Error','Transfer quantity must need to be a number.')
                return


    def outMoveToStandby_clicked(self):
        response, status = QtWidgets.QInputDialog.getText(self, 'Enter Quantity', 'Quantity to transfer:')
        if status:
            if appFunction.canConv(self, response):
                mQty = float(response)
                oStock = float(str(self.ui.outStock_txt.text()).strip())
                if mQty>oStock:
                    QtWidgets.QMessageBox().critical(self,'Error','Transfer quantity cannot be more than current rig quantity.')
                    return
                else:
                    oStandby = float(str(self.ui.outStandby_txt.text()).strip())
                    oType = str(self.ui.outType_txt.text()).strip()
                    oCode = str(self.ui.outCode_txt.text()).strip()
                    oBatch = str(self.ui.outBatch_txt.text()).strip()
                
                    rStock = oStock - mQty
                    rStandby = oStandby + mQty

                    with sqlite3.connect('db\\invRig.db') as conn:
                        sqlQuery = f"UPDATE rigInv SET rig_qty=?, transit_qty=? " \
                            f"WHERE type=? AND code=? AND batch=?"
                        sqlValues = [rStock, rStandby, oType, oCode, oBatch]
                        c = conn.cursor()
                        c.execute(sqlQuery, sqlValues)
                        conn.commit()
                        appFunction.appInit(self)
                        self.ui.outStock_txt.setText(str(rStock))
                        self.ui.outStandby_txt.setText(str(rStandby))
            else:
                QtWidgets.QMessageBox().critical(self,'Error','Transfer quantity must need to be a number.')
                return


    def outDeductButton_Clicked(self):
        #print (self.ui.outDate_dt.date().toPyDate()) #.strftime("%d-%m-%Y")       
        oType = str(self.ui.outType_txt.text()).strip()
        oCode = str(self.ui.outCode_txt.text()).strip()
        oBatch = str(self.ui.outBatch_txt.text()).strip()
        oDate = str(self.ui.outDate_dt.date().toPython()).strip()
        oQty = str(self.ui.outUsage_txt.text()).strip()
        oUnit = str(self.ui.outUnit_txt.text()).strip()
        oInfo = str(self.ui.outInfo_txt.text()).strip()

        if appFunction.canConv(self, oQty):
            usedQty =  float(oQty)
            stockQty = float(self.ui.outStock_txt.text())
        else:
            QtWidgets.QMessageBox().critical(self, 'Input Error!', 'Usage quantity need to be a number.')
            return

        if (usedQty>stockQty):
            QtWidgets.QMessageBox().critical(self, 'Input Error!', 'Usage cannot be more than the stock.')
            return
        elif self.ui.outInfo_txt.text()=="":
            QtWidgets.QMessageBox().critical(self, 'Input Error!', 'Provide details about usage information')
            return
        else:
            uMessage = QtWidgets.QMessageBox().question(self, ' Confirmation', \
                f"{usedQty} {oUnit} {oCode} will be removed from inventory. Are you sure?")
            if uMessage != QtWidgets.QMessageBox.Yes: return
            revisedRigQty = stockQty - usedQty
            with sqlite3.connect('db\\invRig.db') as conn:
                sqlQuery = f"UPDATE rigInv SET rig_qty=? " \
                    f"WHERE type=? AND code=? AND batch=?"
                sqlValues = [revisedRigQty, oType, oCode, oBatch]
                c = conn.cursor()
                c.execute(sqlQuery, sqlValues)
                conn.commit()
                
                sqlQuery = f"INSERT INTO usage VALUES (?,?,?,?,?,?,?,?)"
                sqlValues = [oDate, oType, oCode, oBatch, usedQty, oUnit, oInfo, self.uName]
                c.execute(sqlQuery,sqlValues)
                conn.commit()
            
                appFunction.appInit(self) 
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_stockView)


    def inTypeCombo_Change(self):
        itemType = str(self.ui.inType_cmb.currentText()) 
        if itemType != "":
            with sqlite3.connect('db\\invRig.db') as conn:
                sqlQuery = f"SELECT DISTINCT code FROM rigInv WHERE type='{itemType}'ORDER BY code"
                c = conn.cursor()
                c.execute(sqlQuery)
                val = c.fetchall()
                self.ui.inCode_cmb.clear()
                self.ui.inCode_cmb.insertItems(0, [i[0] for i in val])

                sqlQuery = f"SELECT DISTINCT uom FROM rigInv WHERE type='{itemType}'ORDER BY uom"
                c.execute(sqlQuery)
                val = c.fetchall()
                self.ui.inUnit_cmb.clear()
                self.ui.inUnit_cmb.insertItems(0, [i[0] for i in val])


    def inCodeCombo_Change(self):
        itemType = str(self.ui.inType_cmb.currentText())
        itemCode = str(self.ui.inCode_cmb.currentText())
        if ((itemType!="") | (itemCode != "")):
                with sqlite3.connect('db\\invRig.db') as conn:
                    sqlQuery = f"SELECT DISTINCT batch FROM rigInv "\
                        f"WHERE type='{itemType}' AND code='{itemCode}' ORDER BY batch"
                    c = conn.cursor()
                    c.execute(sqlQuery)
                    val = c.fetchall()
                    self.ui.inBatch_cmb.clear()
                    self.ui.inBatch_cmb.insertItems(0, [i[0] for i in val])

    def inBatchCombo_Change(self):
        iType = str(self.ui.inType_cmb.currentText())
        iCode = str(self.ui.inCode_cmb.currentText())
        iBatch = str(self.ui.inBatch_cmb.currentText())

        if (iCode == "") | (iBatch == ""): return 

        with sqlite3.connect('db\\invRig.db') as conn: 
            qtColName = ['Date', 'Code', 'Batch','Rig Quantity','Standby Qty', 'Comment', 'Received By']
            sqlQuery = f"SELECT date, code, batch, rig_qty, "\
                f"transit_qty, comment, received_by FROM received "\
                    f"WHERE type='{iType}' AND code='{iCode}'"
            appFunction.fillTable_sql(self, conn, sqlQuery, self.ui.received_tbl, qtColName)

    # Match comma seperated word-list in a SQLite text-data column and return all matched rows 
    def keyword_match(keyWord, dbData, cData):
        matchedList =[]
        keyWord = list(set((val.lower()).strip() for val in keyWord.split(',')))
        
        for sIndex,sValue in enumerate(cData):
            for j in (sValue.lower()).split(' '):
                for b in keyWord:
                    if (b.lower()).strip() == (j.lower()).strip(): 
                        matchedList.append(dbData[sIndex])
        
        return matchedList