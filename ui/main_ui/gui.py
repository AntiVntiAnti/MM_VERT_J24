# Form implementation generated from reading ui file 'MMVERT2.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(158, 288)
        MainWindow.setStyleSheet("QWidget {\n"
"    font: 11pt \"Poppins\";\n"
"    background:#121212;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"\n"
"#wellbeing_spinbox {color:rgb(156,123,189); background:transparent; }\n"
"#wellbeing_spinbox:hover {color: rgb(216,183,249); }\n"
"#wellbeing_spinbox:focus {color: rgb(186,153,219); }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////\n"
"QTextEdit\n"
"///////////////////////////////////////////////////////////////////////////// */\n"
"QTextEdit {\n"
"    border:none;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////\n"
"QToolTip\n"
"///////////////////////////////////////////////////////////////////////////// */\n"
"QToolTip {\n"
"    background: rgba(12, 12, 12,50);\n"
"    border: 1px solid  rgb(129, 179, 234);\n"
"    border-radius: 5px;\n"
"    padding:4px;\n"
"    text-align: left;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////\n"
"QTimeEdit, QDoubleSpinBox, QSpinBox\n"
"///////////////////////////////////////////////////////////////////////////// */\n"
"QDoubleSpinBox,\n"
"QSpinBox {\n"
"    border:none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////\n"
"QLabel\n"
"///////////////////////////////////////////////////////////////////////////// */\n"
"QLabel {\n"
"    background:transparent;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////\n"
"QComboBox\n"
"///////////////////////////////////////////////////////////////////////////// */\n"
"QComboBox {\n"
"    background-color: transparent; border:1px inset rgb(28,32,23); border-radius:2px; padding: 3px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////\n"
"QLineEdit\n"
"///////////////////////////////////////////////////////////////////////////// */\n"
"    QLineEdit {\n"
"    border:none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////\n"
"QCheckBox\n"
"///////////////////////////////////////////////////////////////////////////// */\n"
"QCheckBox::indicator {\n"
"    font-weight:bold;\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(255,255,255);\n"
"    border-radius: 6px;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    margin-left:8px;\n"
"    margin-right:8px;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: rgb(255,255,255);\n"
"    border: 2px solid rgb(255,255,255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////\n"
"QSlider\n"
"///////////////////////////////////////////////////////////////////////////// */\n"
"QSlider:horizontal { \n"
"    background:transparent;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 14px;\n"
"    margin: 0px;\n"
"    background:transparent;\n"
"    }\n"
"\n"
"QSlider::groove:horizontal:hover {\n"
"    background: rgb(38, 38, 38);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(255, 255, 255);\n"
"    height: 17px;\n"
"    width: 15px;\n"
"    margin: 0px;\n"
"    border-radius:7px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background:transparent;\n"
"    border-radius: 10px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: white;\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color:white;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////\n"
"Time/DateEdit\n"
"///////////////////////////////////////////////////////////////////////////// */\n"
"QTimeEdit,\n"
"QDateEdit {\n"
"    background-color: transparent;\n"
"    border:None;\n"
"}\n"
"\n"
"/* //////////////////////////////////////////////////////////////////////////////\n"
"QTableView\n"
"////////////////////////////////////////////////////////////////////////////// */\n"
"QTableView {\n"
"    background-color: transparent;\n"
"    alternate-background-color: rgb(101, 147, 128);\n"
"    selection-background-color: #7e57c2;\n"
"    gridline-color: rgb(90, 90, 90);color:rgb(245,245,245);\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 1px;\n"
"    background:rgb(216,79,79);\n"
"}\n"
"QTableView::item:selected {\n"
"    color: #fff;\n"
"    background:rgb(23, 23, 23);\n"
"}\n"
"\n"
"\n"
"/*\n"
"VERTICAL\n"
"///////////////////////////////////////////////////////////////////////////// */\n"
"QSlider::groove:vertical {\n"
"    border-radius: 11px;\n"
"    width: 22px;\n"
"    margin: 0px;\n"
"    background-color: rgba(33,33,33,100);\n"
"}\n"
"\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgba(44,44,44,100);    \n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(255, 88, 71);\n"
"    border: none;\n"
"    height: 22px;\n"
"    width: 22px;\n"
"    margin: 0px;\n"
"    border-radius: 11px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* ////////////////////////////////////////////////////////////////////////////////////////////////\n"
"                                    QScrollBar\n"
"//////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background:transparent;\n"
"    height: 12px;\n"
"    margin: 0px 10px 0px 10px;\n"
"    border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(22,22,22);\n"
"    min-width:24px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 20px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, \n"
"QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color:transparent;\n"
"    width: 12px;\n"
"    margin: 10px 0px 10px 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(22,22,22);\n"
"    min-height: 12px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, \n"
"QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.minderStacks = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.minderStacks.setStyleSheet("QTabWidget {\n"
"    background-color: #121212;\n"
"    border: none;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;    background-color: #121212;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #121212;\n"
"    border: none;\n"
"    min-height:30px;\n"
"    max-height:30px;\n"
"    min-width:40px;\n"
"    max-width:40px;\n"
"    padding:4px 8px 4px 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #121212;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:hover {\n"
"     background-color: #121212;\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    padding: 2px;    background-color: #121212;\n"
"}\n"
"")
        self.minderStacks.setObjectName("minderStacks")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.page)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.mood_slider = QtWidgets.QSlider(parent=self.frame)
        self.mood_slider.setMinimumSize(QtCore.QSize(35, 0))
        self.mood_slider.setStyleSheet("\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QToolTip\n"
"/////////////////////////////////////////////////////////////// */\n"
"QToolTip {\n"
"    background: rgba(23,23,23, 150);\n"
"    border: 1px solid rgb(104,174,102);\n"
"    border-radius: 5px; \n"
"    padding:4px; \n"
"    text-align: left;\n"
"    color: rgb(104,174,102);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QSlider Colors\n"
"/////////////////////////////////////////////////////////////// */\n"
"\n"
"QSlider::handle:vertical {background:rgb(96,175,107);}\n"
"QSlider::handle:vertical:hover {background:rgb(126,205,137);}\n"
"QSlider::handle:vertical:pressed {background:rgb(76,155,87);}\n"
"QSlider::add-page:vertical {background:rgb(96,175,107);}\n"
"QSlider::groove:vertical:hover {background:rgba(96,175,107,0.35);}\n"
"QSlider::groove:vertical {background:rgba(96,175,107,0.15);}\n"
"")
        self.mood_slider.setMaximum(10)
        self.mood_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.mood_slider.setObjectName("mood_slider")
        self.gridLayout.addWidget(self.mood_slider, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mania = QtWidgets.QSpinBox(parent=self.frame)
        self.mania.setStyleSheet("\n"
"    /* ///////////////////////////////////////////////////////////////\n"
"    QToolTip\n"
"    /////////////////////////////////////////////////////////////// */\n"
"    QToolTip {\n"
"        background: rgba(23,23,23, 150);\n"
"        border: 1px solid rgb(220,180,74);\n"
"        border-radius: 5px;\n"
"        padding:4px;\n"
"        text-align: left;\n"
"        color: rgb(220,180,74);\n"
"    }\n"
"    \n"
"\n"
"\n"
"    /* ///////////////////////////////////////////////////////////////\n"
"    QSpinBox\n"
"    /////////////////////////////////////////////////////////////// */\n"
"    QSpinBox {color:rgb(220,180,74);}\n"
"    QSpinBox:hover {color: rgb(255,240,134);}\n"
"    QSpinBox:focus {color: rgb(250,210,104);}\n"
"    ")
        self.mania.setFrame(False)
        self.mania.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.mania.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.mania.setMaximum(10)
        self.mania.setObjectName("mania")
        self.gridLayout.addWidget(self.mania, 1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mixed_risk_slider = QtWidgets.QSlider(parent=self.frame)
        self.mixed_risk_slider.setMinimumSize(QtCore.QSize(35, 0))
        self.mixed_risk_slider.setStyleSheet("\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QToolTip\n"
"/////////////////////////////////////////////////////////////// */\n"
"QToolTip {\n"
"    background: rgba(23,23,23, 150);\n"
"    border: 1px solid rgb(220,99,108);\n"
"    border-radius: 5px; \n"
"    padding:4px; \n"
"    text-align: left;\n"
"    color: rgb(220,99,108);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QSlider Colors\n"
"/////////////////////////////////////////////////////////////// */\n"
"\n"
"QSlider::handle:vertical {background:rgb(222,100,109);}\n"
"QSlider::handle:vertical:hover {background:rgb(252,130,139);}\n"
"QSlider::handle:vertical:pressed {background:rgb(202,80,89);}\n"
"QSlider::add-page:vertical{background:rgb(222,100,109);}\n"
"QSlider::groove:vertical:hover {background:rgba(222,100,109,0.35);}\n"
"QSlider::groove:vertical {background:rgba(222,100,109,0.15);}")
        self.mixed_risk_slider.setMaximum(10)
        self.mixed_risk_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.mixed_risk_slider.setObjectName("mixed_risk_slider")
        self.gridLayout.addWidget(self.mixed_risk_slider, 0, 3, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.depression_slider = QtWidgets.QSlider(parent=self.frame)
        self.depression_slider.setMinimumSize(QtCore.QSize(35, 0))
        self.depression_slider.setStyleSheet("\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QToolTip\n"
"/////////////////////////////////////////////////////////////// */\n"
"QToolTip {\n"
"    background: rgba(23,23,23, 150);\n"
"    border: 1px solid rgb(93,112,219);\n"
"    border-radius: 5px; \n"
"    padding:4px; \n"
"    text-align: left;\n"
"    color: rgb(93,112,219);\n"
"}\n"
"/* ////////////////////////////////////////////////////////////////////////\n"
"depression slider\n"
"//////////////////////////////////////////////////////////////////////// */\n"
"QSlider::handle:vertical {background:rgb(87,111,215);}\n"
"QSlider::handle:vertical:hover {background:rgb(117,141,245);}\n"
"QSlider::handle:vertical:pressed {background:rgb(67,91,195);}\n"
"QSlider::add-page:vertical {background:rgb(87,111,215);}\n"
"QSlider::groove:vertical:hover{background:rgba(87,111,215,0.35);}\n"
"\n"
"QSlider::groove:vertical {background:rgba(87,111,215,0.15);}")
        self.depression_slider.setMaximum(10)
        self.depression_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.depression_slider.setObjectName("depression_slider")
        self.gridLayout.addWidget(self.depression_slider, 0, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mania_slider = QtWidgets.QSlider(parent=self.frame)
        self.mania_slider.setMinimumSize(QtCore.QSize(35, 0))
        self.mania_slider.setStyleSheet("\n"
"    /* ///////////////////////////////////////////////////////////////\n"
"    QToolTip\n"
"    /////////////////////////////////////////////////////////////// */\n"
"    QToolTip {\n"
"        background: rgba(23,23,23, 150);\n"
"        border: 1px solid rgb(220,180,74);\n"
"        border-radius: 5px;\n"
"        padding:4px;\n"
"        text-align: left;\n"
"        color: rgb(220,180,74);\n"
"    }\n"
"    \n"
"/* ///////////////////////////////////////////////////////////////\n"
"QSlider Colors\n"
"/////////////////////////////////////////////////////////////// */\n"
"\n"
"\n"
"    /* ///////////////////////////////////////////////////////////////\n"
"    QSlider Colors\n"
"    /////////////////////////////////////////////////////////////// */\n"
"    \n"
"QSlider::handle:vertical {background:rgb(220,180,74);}\n"
"QSlider::handle:vertical:hover {background:rgb(250,210,104);}\n"
"QSlider::handle:vertical:pressed {background:rgb(200,160,54);}\n"
"QSlider::add-page:vertical {background:rgb(220,180,74);}\n"
"QSlider::groove:vertical:hover {background:rgba(220,180,74,0.35);}\n"
"QSlider::groove:vertical {background:rgba(220,180,74,0.15);}\n"
"    ")
        self.mania_slider.setMaximum(10)
        self.mania_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.mania_slider.setObjectName("mania_slider")
        self.gridLayout.addWidget(self.mania_slider, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mood = QtWidgets.QSpinBox(parent=self.frame)
        self.mood.setStyleSheet("\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QToolTip\n"
"/////////////////////////////////////////////////////////////// */\n"
"QToolTip {\n"
"    background: rgba(23,23,23, 150);\n"
"    border: 1px solid rgb(104,174,102);\n"
"    border-radius: 5px; \n"
"    padding:4px; \n"
"    text-align: left;\n"
"    color: rgb(104,174,102);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QSpinBox\n"
"/////////////////////////////////////////////////////////////// */\n"
"QSpinBox {background:transparent;color:rgb(96,175,107);}\n"
"QSpinBox:hover {color: rgb(156,235,167);}\n"
"QSpinBox:focus {color: rgb(126,205,137);}\n"
"")
        self.mood.setFrame(False)
        self.mood.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mood.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.mood.setMaximum(10)
        self.mood.setObjectName("mood")
        self.gridLayout.addWidget(self.mood, 1, 0, 1, 1)
        self.mixed_risk = QtWidgets.QSpinBox(parent=self.frame)
        self.mixed_risk.setStyleSheet("\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QToolTip\n"
"/////////////////////////////////////////////////////////////// */\n"
"QToolTip {\n"
"    background: rgba(23,23,23, 150);\n"
"    border: 1px solid rgb(220,99,108);\n"
"    border-radius: 5px; \n"
"    padding:4px; \n"
"    text-align: left;\n"
"    color: rgb(220,99,108);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QSpinBox\n"
"/////////////////////////////////////////////////////////////// */\n"
"QSpinBox {color:rgb(222,100,109);}\n"
"QSpinBox:hover {color: rgb(255,160,169);}\n"
"QSpinBox:focus {color: rgb(252,130,139);}\n"
"")
        self.mixed_risk.setFrame(False)
        self.mixed_risk.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.mixed_risk.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.mixed_risk.setMaximum(10)
        self.mixed_risk.setObjectName("mixed_risk")
        self.gridLayout.addWidget(self.mixed_risk, 1, 3, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.depression = QtWidgets.QSpinBox(parent=self.frame)
        self.depression.setStyleSheet("\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QToolTip\n"
"/////////////////////////////////////////////////////////////// */\n"
"QToolTip {\n"
"    background: rgba(23,23,23, 150);\n"
"    border: 1px solid rgb(93,112,219);\n"
"    border-radius: 5px; \n"
"    padding:4px; \n"
"    text-align: left;\n"
"    color: rgb(93,112,219);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////\n"
"QSpinBox\n"
"/////////////////////////////////////////////////////////////// */\n"
"QSpinBox {color:rgb(87,111,215);background:transparent;}\n"
"QSpinBox:hover {color: rgb(147,171,255);}\n"
"QSpinBox:focus {color: rgb(117,141,245);}\n"
"")
        self.depression.setFrame(False)
        self.depression.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.depression.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.depression.setMaximum(10)
        self.depression.setObjectName("depression")
        self.gridLayout.addWidget(self.depression, 1, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout.addWidget(self.frame)
        self.minderStacks.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mental_mental_table = QtWidgets.QTableView(parent=self.page_4)
        self.mental_mental_table.setStyleSheet("\n"
"QTableView {\n"
"background-color: transparent;\n"
"selection-background-color: #7e57c2;\n"
"gridline-color:transparent;\n"
"color: rgb(77, 15, 26);\n"
"}\n"
"QTableView::item {\n"
"padding: 1px;color: rgb(77, 15, 26);\n"
"background:rgb(229,100,111);\n"
"}\n"
"QTableView::item:selected {\n"
"    color: rgb(255, 255, 255);\n"
"background:rgb(23, 23, 23);\n"
"}\n"
"    ")
        self.mental_mental_table.setSortingEnabled(True)
        self.mental_mental_table.setObjectName("mental_mental_table")
        self.mental_mental_table.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.mental_mental_table, 0, 0, 1, 1)
        self.minderStacks.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.mental_mental_time = QtWidgets.QTimeEdit(parent=self.page_5)
        self.mental_mental_time.setObjectName("mental_mental_time")
        self.gridLayout_15.addWidget(self.mental_mental_time, 1, 0, 1, 1)
        self.mental_mental_date = QtWidgets.QDateEdit(parent=self.page_5)
        self.mental_mental_date.setObjectName("mental_mental_date")
        self.gridLayout_15.addWidget(self.mental_mental_date, 0, 0, 1, 1)
        self.minderStacks.addWidget(self.page_5)
        self.gridLayout_2.addWidget(self.minderStacks, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 158, 18))
        self.menubar.setObjectName("menubar")
        self.menuMM = QtWidgets.QMenu(parent=self.menubar)
        self.menuMM.setObjectName("menuMM")
        self.menuData = QtWidgets.QMenu(parent=self.menubar)
        self.menuData.setObjectName("menuData")
        MainWindow.setMenuBar(self.menubar)
        self.actionMinimize = QtGui.QAction(parent=MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionMaximize = QtGui.QAction(parent=MainWindow)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionInput = QtGui.QAction(parent=MainWindow)
        self.actionInput.setObjectName("actionInput")
        self.actionTableview = QtGui.QAction(parent=MainWindow)
        self.actionTableview.setObjectName("actionTableview")
        self.actionCommit = QtGui.QAction(parent=MainWindow)
        self.actionCommit.setObjectName("actionCommit")
        self.actionDelete = QtGui.QAction(parent=MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.menuMM.addAction(self.actionMinimize)
        self.menuMM.addAction(self.actionMaximize)
        self.menuData.addAction(self.actionInput)
        self.menuData.addAction(self.actionTableview)
        self.menuData.addAction(self.actionCommit)
        self.menuData.addAction(self.actionDelete)
        self.menubar.addAction(self.menuMM.menuAction())
        self.menubar.addAction(self.menuData.menuAction())

        self.retranslateUi(MainWindow)
        self.minderStacks.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mood_slider.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Mood Measure</span></p></body></html>"))
        self.mania.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Mania Measure</span></p></body></html>"))
        self.mixed_risk_slider.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mixed Risk</p></body></html>"))
        self.depression_slider.setToolTip(_translate("MainWindow", "<html><head/><body><p>Depression</p></body></html>"))
        self.mania_slider.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Mania Measure</span></p></body></html>"))
        self.mood.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Mood Measure</span></p></body></html>"))
        self.mixed_risk.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mixed Risk</p></body></html>"))
        self.depression.setToolTip(_translate("MainWindow", "<html><head/><body><p>Depression</p></body></html>"))
        self.menuMM.setTitle(_translate("MainWindow", "MM"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionMinimize.setShortcut(_translate("MainWindow", "Alt+M"))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
        self.actionMaximize.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionInput.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionTableview.setText(_translate("MainWindow", "Tableview"))
        self.actionTableview.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionCommit.setText(_translate("MainWindow", "Commit"))
        self.actionCommit.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
