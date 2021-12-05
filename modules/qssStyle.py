appStyle ="""
	/* This is the root frame inside borderless windows. 
	All other widget/elements are child of this frame*/
	#frame_app {
		border-radius: 0px;
	}
	/* Below section is for app title bar*/
	#frame_titleBar {
		background-color: rgba(98,114,164,255);
		border-top-left-radius: 0px;
		border-top-right-radius: 0px;
	}
	#frame_creditBar {
		background-color: rgba(98,114,164,255);
		border-bottom-left-radius: 0px;
		border-bottom-right-radius: 0px;
	}
	#btn_appLogo {
		border: None;
		qproperty-icon: url(:/images/images/icon.ico);
		qproperty-iconSize: 24px;
	}
	#label_appTitle {
		color: rgba(255, 255, 255,200);
	}
	#btn_closeApp {
		border: None;
	}
	#btn_closeApp:hover {
		background-color: rgba(0,255,0,100);
	}
	#btn_maximizeApp {
		border: None;
	}
	#btn_maximizeApp:hover {
		background-color: rgba(0,255,0,100);
	}
	#btn_minimizeApp {
		border: None;
	}
	#btn_minimizeApp:hover {
		background-color: rgba(0,255,0,100);
	}

	#frame_contentBar {
		background-color: rgba(255,255,255,255);
	}

	#frame_leftMenu {
		background-color: rgba(98,114,164,255);
	}
	#btn_toggleMenu {
		border: None;
		qproperty-iconSize: 24px;
	}
	#btn_userMenu {
		border: None;
		border-left: 3px solid transparent;
		qproperty-iconSize: 24px;
	}
	#btn_userMenuText {
		border: None;
		border-left: 3px solid transparent;
		text-align: left;
		padding-left: 12px;
		color: rgba(255,255,255,255);
	}
	#btn_stockMenu {
		border: None;
		border-left: 3px solid transparent;
		qproperty-iconSize: 24px;
	}
	#btn_stockMenuText {
		border: None;
		border-left: 3px solid transparent;
		text-align: left;
		padding-left: 12px;
		color: rgba(255,255,255,255);
	}
	#btn_exitMenu{
		border: none;
		border-left: 3px solid transparent;
		qproperty-icon: url(:/images/images/cil-exit-to-app.png);
		qproperty-iconSize: 24px;
	}
	#btn_exitMenuText {
		border: None;
		border-left: 3px solid transparent;
		text-align: left;
		padding-left: 12px;
		color: rgba(255,255,255,255);
	}
	#btn_LMenuToggleText {
		border: None;
		text-align: left;
		padding-left: 15px;
		color: rgba(255,255,255,255);
	}
	#frame_toggleInner:hover {
		background-color: rgba(0,255,0,100);
	}
	#frame_user:hover {
		background-color: rgba(0,255,0,100);
	}
	#frame_stockMenu:hover {
		background-color: rgba(0,255,0,100);
	}
	#frame_exitMenu:hover {
		background-color: rgba(0,255,0,100);
	}
"""


stockViewStyle="""
	QTableWidget {	
		background-color: transparent;
		padding: 10px;
		border-radius: 5px;
		gridline-color: #9faeda;
	    outline: none;
	    font: 12pt "Segoe UI";
	}
	QTableWidget::item{
		border-color: #9faeda;
		padding-left: 5px;
		padding-right: 5px;
		gridline-color: #9faeda;
	}
	QTableWidget::item:selected{
		background-color: rgb(189, 147, 249);
	    color: #f8f8f2;
	}
	QHeaderView::section{
		background-color: #6272a4;
		/*max-width: 30px;*/
		border: none;
		border-style: none;
	}
	QTableWidget::horizontalHeader {	
		background-color: #6272a4;
	    font: 14pt "Segoe UI";
	}
	QHeaderView::section:horizontal
	{
	    border: 1px solid #6272a4;
		background-color: #6272a4;
		padding-top:5px;
	    padding-bottom: 3px;
		padding-left: 10px;
	    padding-right: 10px;
		border-top-left-radius: 7px;
	    border-top-right-radius: 7px;
	    color: #f8f8f2;
	    font: 12pt "Segoe UI";
	}
	QTableWidget::verticalHeader {	
		background-color: #6272a4;
	}
	QHeaderView::section:vertical
	{
	    border: 1px solid #6272a4;
		background-color: #6272a4;
		padding-top: 3px;
	    padding-bottom: 3px;
		padding-left: 10px;
	    padding-right: 3px;
		color: #f8f8f2;
	    font: 12pt "Segoe UI";
	}

	#frame_btnStock{
		padding-left: 10px;
		padding-right: 10px;
	}

	QComboBox{
		background-color: #6272a4;
		border-radius: 5px;
		border: 2px solid #6272a4;
		padding: 5px;
		padding-left: 10px;
	    color: #f8f8f2;
	}
	QComboBox:hover{
		border: 2px solid #7284b9;
	}
	QComboBox::drop-down {
		subcontrol-origin: padding;
		subcontrol-position: top right;
		width: 25px; 
		border-left-width: 3px;
		border-left-color: #f8f8f2;
		border-left-style: solid;
		border-top-right-radius: 3px;
		border-bottom-right-radius: 3px;	
	 }
	/*QComboBox QAbstractItemView {
		color: rgb(255, 255, 255);	
		background-color: #6272a4;
		padding: 10px;
		selection-background-color: #6272a4;
	}*/

	/* /////////////////////////////////////////////////////////////////////////////////////////////////
	Button */
	QPushButton {
		border: 2px solid #6272a4;
		border-radius: 5px;	
		background-color: #6272a4;
	    color: #f8f8f2;
	    font: 12pt "Segoe UI";
	    padding: 3px;
	}
	QPushButton:hover {
		background-color: #7082b6;
		border: 2px solid #7082b6;
	}
	QPushButton:pressed {	
		background-color: #546391;
		border: 2px solid #ff79c6;
	}

"""