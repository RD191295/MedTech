# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainalnxRP.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)
from . Images_Resource_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1169, 750)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: #333;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: #333;\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"    color: #44475a;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: #6272a4;\n"
"}\n"
"#topLogo {\n"
"	background-color: #6272a4;\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-re"
                        "peat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; color: #f8f8f2; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #bd93f9; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#bottomMenu .QPushButton:"
                        "pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid #6a7cb1;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #5b6996;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: #f8f8f2;\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#toggleButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: #495474;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
""
                        "	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid #6272a4;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#e"
                        "xtraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: #6272a4;\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid #bd93f9;\n"
"}\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #bd93f9; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #ff79c6; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #495474; }\n"
"#themeSettingsTopDetail { background-color: #6272a4; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: #495474 }\n"
"#bottomBar QLabel { font-size: 11px"
                        "; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline"
                        "-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #6272a4;\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #6272a4;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"	background-color: #6272a4;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
""
                        "}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
""
                        "	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background-color: #6272a4;\n"
"    width: 8px;\n"
"    margin: 21px 0 21"
                        "px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Che"
                        "ckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"}\n"
"\n"
"/* //////////////////////////////////////////////////////////////////////////////////"
                        "///////////////\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
""
                        "    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-"
                        "color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"#pagesContainer QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"    border: 2px solid #ff79c6;\n"
"    color: #ff79c6;\n"
"}\n"
"#pagesContainer QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: #6272a4;\n"
"}\n"
"#pagesContainer QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: #586796;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #708"
                        "2b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"#qt_calendar_navigationbar {\n"
"    background-color: rgb(98, 114, 164);\n"
"    min-height: 40px;\n"
"    max-width :280px;\n"
"    border-top-left-radius:5px;\n"
"	border-top-right-radius:5px;\n"
"\n"
"}\n"
"\n"
"\n"
"#qt_calendar_prevmonth, #qt_calendar_nextmonth {\n"
"    border: none;\n"
"    color: white;\n"
"    min-width: 36px;\n"
"    max-width: 36px;\n"
"    min-height: 36px;\n"
"    max-height: 36px;\n"
"    font-weight: bold; \n"
"    qproperty-icon: none; \n"
"    background-color: transparent;\n"
"}\n"
"#qt_calendar_prevmonth {\n"
"    qproperty-text: \"<\"; \n"
"}\n"
"#qt_calendar_nextmonth {\n"
"    qproperty-text: \">\";\n"
"}\n"
"#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {\n"
"    background-color: rgba(225, 225, 225, 100);\n"
"}\n"
"#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {\n"
"    backgro"
                        "und-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"\n"
"#qt_calendar_yearbutton, #qt_calendar_monthbutton {\n"
"    color: white;\n"
"    margin: 0px;\n"
"    min-width: 80px;\n"
"}\n"
"#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {\n"
"    background-color: rgba(225, 225, 225, 100);\n"
"}\n"
"#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"#qt_calendar_yearedit {\n"
"    min-width: 80px;\n"
"    color: white;\n"
"    background: transparent;\n"
"}\n"
"#qt_calendar_yearedit::up-button { \n"
"    width: 14px;\n"
"    subcontrol-position: right\n"
"}\n"
"#qt_calendar_yearedit::down-button { \n"
"    width: 14px;\n"
"    subcontrol-position: left; \n"
"}\n"
"\n"
"QCalendarWidget  QMenu{\n"
"    background-color:rgb(98, 114, 164);\n"
"   	selection-background-color: rgb(255, 121, 199);\n"
"	selection-color: rgb(255, 255, 255);\n"
"}\n"
"QCalendarWidget QToolButton{\n"
"    background-color:rgb(98, 114, 164);\n"
""
                        "   	selection-background-color: rgb(255, 121, 199);\n"
"	selection-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#qt_calendar_calendarview {\n"
"    outline: 0px;\n"
"    selection-background-color: rgb(195, 155, 255);\n"
"}\n"
"\n"
"/*list view */\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:alternate {\n"
"    background: #EEEEEE;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FA"
                        "FBFE, stop: 1 #DCDEF1);\n"
"}\n"
"QListView {\n"
"   border-radius:10px;\n"
"    alternate-background-color: yellow;\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setStyleSheet(u"  border-top-left-radius: 10px;\n"
"  border-bottom-left-radius: 10px;")
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 40, 40))
        self.topLogo.setMinimumSize(QSize(40, 40))
        self.topLogo.setMaximumSize(QSize(40, 40))
        self.topLogo.setStyleSheet(u"background-image:url(:/images/images/images/MedTech-logos_v1.jpg)")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.topMenu)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"\n"
"background-image: url(:/icons/images/icons/icon_menu.png);")
        self.toggleButton.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.toggleButton)

        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.toggleBox = QFrame(self.topMenu)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.toggleBox)

        self.btn_profile = QPushButton(self.topMenu)
        self.btn_profile.setObjectName(u"btn_profile")
        sizePolicy.setHeightForWidth(self.btn_profile.sizePolicy().hasHeightForWidth())
        self.btn_profile.setSizePolicy(sizePolicy)
        self.btn_profile.setMinimumSize(QSize(0, 45))
        self.btn_profile.setFont(font)
        self.btn_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_profile.setLayoutDirection(Qt.LeftToRight)
        self.btn_profile.setStyleSheet(u"background-image:url(:/icons/images/icons/cli_profile.png);")

        self.verticalLayout_8.addWidget(self.btn_profile)

        self.btn_appointment = QPushButton(self.topMenu)
        self.btn_appointment.setObjectName(u"btn_appointment")
        sizePolicy.setHeightForWidth(self.btn_appointment.sizePolicy().hasHeightForWidth())
        self.btn_appointment.setSizePolicy(sizePolicy)
        self.btn_appointment.setMinimumSize(QSize(0, 45))
        self.btn_appointment.setFont(font)
        self.btn_appointment.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_appointment.setLayoutDirection(Qt.LeftToRight)
        self.btn_appointment.setStyleSheet(u"background-image: url(:/icons/images/icons/cli_doctor.png);")

        self.verticalLayout_8.addWidget(self.btn_appointment)

        self.btn_labtest = QPushButton(self.topMenu)
        self.btn_labtest.setObjectName(u"btn_labtest")
        sizePolicy.setHeightForWidth(self.btn_labtest.sizePolicy().hasHeightForWidth())
        self.btn_labtest.setSizePolicy(sizePolicy)
        self.btn_labtest.setMinimumSize(QSize(0, 45))
        self.btn_labtest.setFont(font)
        self.btn_labtest.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_labtest.setLayoutDirection(Qt.LeftToRight)
        self.btn_labtest.setStyleSheet(u"background-image: url(:/icons/images/icons/cli-lab.png);")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-medical-cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_labtest.setIcon(icon)

        self.verticalLayout_8.addWidget(self.btn_labtest)

        self.btn_medicine = QPushButton(self.topMenu)
        self.btn_medicine.setObjectName(u"btn_medicine")
        sizePolicy.setHeightForWidth(self.btn_medicine.sizePolicy().hasHeightForWidth())
        self.btn_medicine.setSizePolicy(sizePolicy)
        self.btn_medicine.setMinimumSize(QSize(0, 45))
        self.btn_medicine.setFont(font)
        self.btn_medicine.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_medicine.setLayoutDirection(Qt.LeftToRight)
        self.btn_medicine.setStyleSheet(u"background-image: url(:/icons/images/icons/cli_medicine.png);")

        self.verticalLayout_8.addWidget(self.btn_medicine)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon1)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.creditText = QTextEdit(self.extraCenter)
        self.creditText.setObjectName(u"creditText")
        self.creditText.setMinimumSize(QSize(222, 0))
        self.creditText.setMaximumSize(QSize(16777215, 206))
        self.creditText.setStyleSheet(u"background: transparent;")
        self.creditText.setFrameShape(QFrame.NoFrame)
        self.creditText.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.creditText)

        self.socialBtn = QFrame(self.extraCenter)
        self.socialBtn.setObjectName(u"socialBtn")
        self.socialBtn.setMinimumSize(QSize(0, 45))
        self.socialBtn.setMaximumSize(QSize(16777215, 45))
        self.socialBtn.setFrameShape(QFrame.StyledPanel)
        self.socialBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.socialBtn)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btn_facebook = QPushButton(self.socialBtn)
        self.btn_facebook.setObjectName(u"btn_facebook")
        self.btn_facebook.setMinimumSize(QSize(0, 45))
        self.btn_facebook.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.btn_facebook.setFont(font3)
        self.btn_facebook.setStyleSheet(u"font: 14pt \"Social Media Circled\";\n"
"border-radius: 0px;\n"
"color: rgb(255, 170, 255);")

        self.horizontalLayout_12.addWidget(self.btn_facebook)

        self.btn_telegram = QPushButton(self.socialBtn)
        self.btn_telegram.setObjectName(u"btn_telegram")
        self.btn_telegram.setMinimumSize(QSize(0, 45))
        self.btn_telegram.setMaximumSize(QSize(16777215, 45))
        self.btn_telegram.setStyleSheet(u"font: 14pt \"Social Media Circled\";\n"
"border-radius: 0px;\n"
"color: rgb(255, 170, 255);")

        self.horizontalLayout_12.addWidget(self.btn_telegram)

        self.btn_twitter = QPushButton(self.socialBtn)
        self.btn_twitter.setObjectName(u"btn_twitter")
        self.btn_twitter.setMinimumSize(QSize(0, 45))
        self.btn_twitter.setMaximumSize(QSize(16777215, 45))
        self.btn_twitter.setStyleSheet(u"font: 14pt \"Social Media Circled\";\n"
"border-radius: 0px;\n"
"color: rgb(255, 170, 255);")

        self.horizontalLayout_12.addWidget(self.btn_twitter)

        self.btn_github = QPushButton(self.socialBtn)
        self.btn_github.setObjectName(u"btn_github")
        self.btn_github.setMinimumSize(QSize(0, 45))
        self.btn_github.setMaximumSize(QSize(16777215, 45))
        self.btn_github.setStyleSheet(u"font: 14pt \"Social Media Circled\";\n"
"border-radius: 0px;\n"
"color: rgb(255, 170, 255);")

        self.horizontalLayout_12.addWidget(self.btn_github)

        self.btn_instagram = QPushButton(self.socialBtn)
        self.btn_instagram.setObjectName(u"btn_instagram")
        self.btn_instagram.setMinimumSize(QSize(0, 45))
        self.btn_instagram.setMaximumSize(QSize(16777215, 45))
        self.btn_instagram.setStyleSheet(u"font: 14pt \"Social Media Circled\";\n"
"border-radius: 0px;\n"
"color: rgb(255, 170, 255);")

        self.horizontalLayout_12.addWidget(self.btn_instagram)


        self.verticalLayout_10.addWidget(self.socialBtn)

        self.frame = QFrame(self.extraCenter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"  border-top-right-radius: 10px;")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon2)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon3)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon4)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon1)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.pagesContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Home_Page = QWidget()
        self.Home_Page.setObjectName(u"Home_Page")
        self.Home_Layout = QVBoxLayout(self.Home_Page)
        self.Home_Layout.setSpacing(0)
        self.Home_Layout.setObjectName(u"Home_Layout")
        self.Home_Layout.setContentsMargins(0, 0, 0, 0)
        self.frame_Home = QFrame(self.Home_Page)
        self.frame_Home.setObjectName(u"frame_Home")
        self.frame_Home.setFrameShape(QFrame.NoFrame)
        self.frame_Home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_Home)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 5, 0, 0)
        self.frame_Welcome_Note = QFrame(self.frame_Home)
        self.frame_Welcome_Note.setObjectName(u"frame_Welcome_Note")
        self.frame_Welcome_Note.setMinimumSize(QSize(0, 40))
        self.frame_Welcome_Note.setMaximumSize(QSize(16777215, 40))
        self.frame_Welcome_Note.setFrameShape(QFrame.NoFrame)
        self.frame_Welcome_Note.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_Welcome_Note)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Label_Welcome = QLabel(self.frame_Welcome_Note)
        self.Label_Welcome.setObjectName(u"Label_Welcome")
        self.Label_Welcome.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 24pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_9.addWidget(self.Label_Welcome)


        self.verticalLayout_20.addWidget(self.frame_Welcome_Note)

        self.frame_Promo = QFrame(self.frame_Home)
        self.frame_Promo.setObjectName(u"frame_Promo")
        self.frame_Promo.setFrameShape(QFrame.NoFrame)
        self.frame_Promo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_Promo)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.Promo_Label = QLabel(self.frame_Promo)
        self.Promo_Label.setObjectName(u"Promo_Label")
        self.Promo_Label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_26.addWidget(self.Promo_Label)


        self.verticalLayout_20.addWidget(self.frame_Promo)


        self.Home_Layout.addWidget(self.frame_Home)

        self.stackedWidget.addWidget(self.Home_Page)
        self.Profile_Page = QWidget()
        self.Profile_Page.setObjectName(u"Profile_Page")
        self.Profile_Details_Label = QLabel(self.Profile_Page)
        self.Profile_Details_Label.setObjectName(u"Profile_Details_Label")
        self.Profile_Details_Label.setGeometry(QRect(20, 20, 191, 51))
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setItalic(False)
        self.Profile_Details_Label.setFont(font5)
        self.Profile_Details_Label.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"border-radius:5px;\n"
"color: rgb(98, 114, 164);")
        self.Pic_Upload = QLabel(self.Profile_Page)
        self.Pic_Upload.setObjectName(u"Pic_Upload")
        self.Pic_Upload.setGeometry(QRect(30, 120, 151, 151))
        self.Pic_Upload.setStyleSheet(u"image: url(:/images/images/images/placeholder.png);")
        self.btn_upload = QPushButton(self.Profile_Page)
        self.btn_upload.setObjectName(u"btn_upload")
        self.btn_upload.setGeometry(QRect(210, 170, 150, 51))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-cloud-upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_upload.setIcon(icon5)
        self.Profile_Description_Label = QLabel(self.Profile_Page)
        self.Profile_Description_Label.setObjectName(u"Profile_Description_Label")
        self.Profile_Description_Label.setGeometry(QRect(20, 70, 591, 31))
        font6 = QFont()
        font6.setPointSize(17)
        font6.setBold(False)
        font6.setItalic(False)
        self.Profile_Description_Label.setFont(font6)
        self.Profile_Description_Label.setStyleSheet(u"font: 17pt \"Segoe UI\";\n"
"border-radius:5px;\n"
"color: rgb(98, 114, 164);")
        self.layoutWidget = QWidget(self.Profile_Page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(410, 280, 311, 61))
        self.LastName_Layout = QHBoxLayout(self.layoutWidget)
        self.LastName_Layout.setObjectName(u"LastName_Layout")
        self.LastName_Layout.setContentsMargins(0, 0, 0, 0)
        self.LastName_Label = QLabel(self.layoutWidget)
        self.LastName_Label.setObjectName(u"LastName_Label")
        self.LastName_Label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 12pt \"Segoe UI\";")

        self.LastName_Layout.addWidget(self.LastName_Label)

        self.LastName_Input = QLineEdit(self.layoutWidget)
        self.LastName_Input.setObjectName(u"LastName_Input")
        self.LastName_Input.setMaximumSize(QSize(16777215, 60))

        self.LastName_Layout.addWidget(self.LastName_Input)

        self.layoutWidget_2 = QWidget(self.Profile_Page)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 380, 350, 61))
        self.Email_Layout = QHBoxLayout(self.layoutWidget_2)
        self.Email_Layout.setObjectName(u"Email_Layout")
        self.Email_Layout.setContentsMargins(0, 0, 0, 0)
        self.Email_Label = QLabel(self.layoutWidget_2)
        self.Email_Label.setObjectName(u"Email_Label")
        self.Email_Label.setMinimumSize(QSize(82, 0))
        self.Email_Label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 12pt \"Segoe UI\";")

        self.Email_Layout.addWidget(self.Email_Label)

        self.Email_Input = QLineEdit(self.layoutWidget_2)
        self.Email_Input.setObjectName(u"Email_Input")
        self.Email_Input.setMinimumSize(QSize(260, 0))
        self.Email_Input.setMaximumSize(QSize(260, 60))
        self.Email_Input.setReadOnly(True)

        self.Email_Layout.addWidget(self.Email_Input)

        self.layoutWidget_3 = QWidget(self.Profile_Page)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(410, 380, 311, 61))
        self.UserName_Layout = QHBoxLayout(self.layoutWidget_3)
        self.UserName_Layout.setObjectName(u"UserName_Layout")
        self.UserName_Layout.setContentsMargins(0, 0, 0, 0)
        self.UserName_Label = QLabel(self.layoutWidget_3)
        self.UserName_Label.setObjectName(u"UserName_Label")
        self.UserName_Label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 12pt \"Segoe UI\";")

        self.UserName_Layout.addWidget(self.UserName_Label)

        self.UserName_Input = QLineEdit(self.layoutWidget_3)
        self.UserName_Input.setObjectName(u"UserName_Input")
        self.UserName_Input.setMaximumSize(QSize(16777215, 60))

        self.UserName_Layout.addWidget(self.UserName_Input)

        self.btn_details_save = QPushButton(self.Profile_Page)
        self.btn_details_save.setObjectName(u"btn_details_save")
        self.btn_details_save.setGeometry(QRect(310, 550, 231, 51))
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_details_save.setIcon(icon6)
        self.label_promo = QLabel(self.Profile_Page)
        self.label_promo.setObjectName(u"label_promo")
        self.label_promo.setGeometry(QRect(740, 20, 441, 591))
        self.layoutWidget1 = QWidget(self.Profile_Page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 280, 350, 61))
        self.FirstName_Layout = QHBoxLayout(self.layoutWidget1)
        self.FirstName_Layout.setSpacing(6)
        self.FirstName_Layout.setObjectName(u"FirstName_Layout")
        self.FirstName_Layout.setContentsMargins(0, 0, 0, 0)
        self.FirstName_Label = QLabel(self.layoutWidget1)
        self.FirstName_Label.setObjectName(u"FirstName_Label")
        self.FirstName_Label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 12pt \"Segoe UI\";")

        self.FirstName_Layout.addWidget(self.FirstName_Label)

        self.FirstName_Input = QLineEdit(self.layoutWidget1)
        self.FirstName_Input.setObjectName(u"FirstName_Input")
        self.FirstName_Input.setMinimumSize(QSize(260, 0))
        self.FirstName_Input.setMaximumSize(QSize(260, 60))

        self.FirstName_Layout.addWidget(self.FirstName_Input)

        self.layoutWidget2 = QWidget(self.Profile_Page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 480, 350, 41))
        self.Gender_Layout = QHBoxLayout(self.layoutWidget2)
        self.Gender_Layout.setObjectName(u"Gender_Layout")
        self.Gender_Layout.setContentsMargins(0, 0, 0, 0)
        self.Gender_Label = QLabel(self.layoutWidget2)
        self.Gender_Label.setObjectName(u"Gender_Label")
        self.Gender_Label.setMinimumSize(QSize(82, 0))
        self.Gender_Label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 12pt \"Segoe UI\";")

        self.Gender_Layout.addWidget(self.Gender_Label)

        self.Gender_Input = QComboBox(self.layoutWidget2)
        self.Gender_Input.addItem("")
        self.Gender_Input.addItem("")
        self.Gender_Input.addItem("")
        self.Gender_Input.setObjectName(u"Gender_Input")
        self.Gender_Input.setMinimumSize(QSize(260, 0))
        self.Gender_Input.setMaximumSize(QSize(260, 40))

        self.Gender_Layout.addWidget(self.Gender_Input)

        self.layoutWidget3 = QWidget(self.Profile_Page)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(410, 480, 311, 42))
        self.BirthDate_Layout = QHBoxLayout(self.layoutWidget3)
        self.BirthDate_Layout.setObjectName(u"BirthDate_Layout")
        self.BirthDate_Layout.setContentsMargins(0, 0, 0, 0)
        self.BirthDate_Label = QLabel(self.layoutWidget3)
        self.BirthDate_Label.setObjectName(u"BirthDate_Label")
        self.BirthDate_Label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 12pt \"Segoe UI\";")

        self.BirthDate_Layout.addWidget(self.BirthDate_Label)

        self.BirthDate_Input = QDateEdit(self.layoutWidget3)
        self.BirthDate_Input.setObjectName(u"BirthDate_Input")
        self.BirthDate_Input.setMinimumSize(QSize(224, 40))
        self.BirthDate_Input.setMaximumSize(QSize(224, 40))
        self.BirthDate_Input.setStyleSheet(u"QDateEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QDateEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QDateEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.BirthDate_Layout.addWidget(self.BirthDate_Input)

        self.stackedWidget.addWidget(self.Profile_Page)
        self.Appointment_Page = QWidget()
        self.Appointment_Page.setObjectName(u"Appointment_Page")
        self.verticalLayout_11 = QVBoxLayout(self.Appointment_Page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Appointment_frame = QFrame(self.Appointment_Page)
        self.Appointment_frame.setObjectName(u"Appointment_frame")
        self.Appointment_frame.setFrameShape(QFrame.StyledPanel)
        self.Appointment_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.Appointment_frame)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.frame_Label = QFrame(self.Appointment_frame)
        self.frame_Label.setObjectName(u"frame_Label")
        self.frame_Label.setMinimumSize(QSize(0, 30))
        self.frame_Label.setMaximumSize(QSize(16777215, 30))
        self.frame_Label.setFrameShape(QFrame.NoFrame)
        self.frame_Label.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_Label)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Title_Label = QLabel(self.frame_Label)
        self.Title_Label.setObjectName(u"Title_Label")
        self.Title_Label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.Title_Label)


        self.verticalLayout_15.addWidget(self.frame_Label)

        self.Frame_SearchBar = QFrame(self.Appointment_frame)
        self.Frame_SearchBar.setObjectName(u"Frame_SearchBar")
        self.Frame_SearchBar.setMinimumSize(QSize(0, 45))
        self.Frame_SearchBar.setMaximumSize(QSize(16777215, 45))
        self.Frame_SearchBar.setFrameShape(QFrame.NoFrame)
        self.Frame_SearchBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Frame_SearchBar)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_search = QFrame(self.Frame_SearchBar)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setMinimumSize(QSize(0, 45))
        self.frame_search.setMaximumSize(QSize(16777215, 16777215))
        self.frame_search.setFrameShape(QFrame.NoFrame)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_search)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.searchBar = QLineEdit(self.frame_search)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setMaximumSize(QSize(16777215, 45))

        self.horizontalLayout_8.addWidget(self.searchBar)


        self.horizontalLayout_7.addWidget(self.frame_search)

        self.frame_btn = QFrame(self.Frame_SearchBar)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMinimumSize(QSize(130, 45))
        self.frame_btn.setMaximumSize(QSize(130, 45))
        self.frame_btn.setFrameShape(QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_btn)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btn_search = QPushButton(self.frame_btn)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(130, 45))
        self.btn_search.setMaximumSize(QSize(130, 45))
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-find-in-page.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon7)

        self.verticalLayout_17.addWidget(self.btn_search)


        self.horizontalLayout_7.addWidget(self.frame_btn)


        self.verticalLayout_15.addWidget(self.Frame_SearchBar)

        self.frame_result = QFrame(self.Appointment_frame)
        self.frame_result.setObjectName(u"frame_result")
        self.frame_result.setFrameShape(QFrame.NoFrame)
        self.frame_result.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_result)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.result_widget = QListWidget(self.frame_result)
        self.result_widget.setObjectName(u"result_widget")
        self.result_widget.setSpacing(5)

        self.verticalLayout_16.addWidget(self.result_widget)


        self.verticalLayout_15.addWidget(self.frame_result)


        self.verticalLayout_11.addWidget(self.Appointment_frame)

        self.stackedWidget.addWidget(self.Appointment_Page)
        self.Lab_test_Booking = QWidget()
        self.Lab_test_Booking.setObjectName(u"Lab_test_Booking")
        self.verticalLayout_18 = QVBoxLayout(self.Lab_test_Booking)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.Lab_test_list = QFrame(self.Lab_test_Booking)
        self.Lab_test_list.setObjectName(u"Lab_test_list")
        self.Lab_test_list.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.Lab_test_list.setFrameShape(QFrame.StyledPanel)
        self.Lab_test_list.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.Lab_test_list)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lab_layout_3 = QHBoxLayout()
        self.lab_layout_3.setObjectName(u"lab_layout_3")
        self.btn_covid = QPushButton(self.Lab_test_list)
        self.btn_covid.setObjectName(u"btn_covid")
        self.btn_covid.setMaximumSize(QSize(170, 170))
        self.btn_covid.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image: url(:/images/images/images/Covid19.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/images/images/images/Covid19_hover.png);\n"
"}\n"
"")
        self.btn_covid.setIconSize(QSize(164, 164))

        self.lab_layout_3.addWidget(self.btn_covid)

        self.btn_cancer = QPushButton(self.Lab_test_list)
        self.btn_cancer.setObjectName(u"btn_cancer")
        self.btn_cancer.setMaximumSize(QSize(170, 170))
        self.btn_cancer.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image: url(:/images/images/images/Cancer Screening.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/images/images/images/Cancer Screening_hover.png)\n"
"}")
        self.btn_cancer.setIconSize(QSize(164, 164))

        self.lab_layout_3.addWidget(self.btn_cancer)

        self.btn_heptatitis = QPushButton(self.Lab_test_list)
        self.btn_heptatitis.setObjectName(u"btn_heptatitis")
        self.btn_heptatitis.setMaximumSize(QSize(170, 170))
        self.btn_heptatitis.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image:url(:/images/images/images/Heptatis.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/images/images/images/Heptatis_hover.png);\n"
"}")
        self.btn_heptatitis.setIconSize(QSize(164, 164))

        self.lab_layout_3.addWidget(self.btn_heptatitis)

        self.btn_B12_D3 = QPushButton(self.Lab_test_list)
        self.btn_B12_D3.setObjectName(u"btn_B12_D3")
        self.btn_B12_D3.setMaximumSize(QSize(170, 170))
        self.btn_B12_D3.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image: url(:/images/images/images/B12_D3_Test.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/images/images/images/B12_D3_Test_hover.png);\n"
"\n"
"\n"
"}")
        self.btn_B12_D3.setIconSize(QSize(164, 164))

        self.lab_layout_3.addWidget(self.btn_B12_D3)

        self.btn_Dengue = QPushButton(self.Lab_test_list)
        self.btn_Dengue.setObjectName(u"btn_Dengue")
        self.btn_Dengue.setMaximumSize(QSize(170, 170))
        self.btn_Dengue.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image: url(:/images/images/images/DengueTest.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image:  url(:/images/images/images/DengueTest_hover.png);\n"
"}")
        self.btn_Dengue.setIconSize(QSize(164, 164))

        self.lab_layout_3.addWidget(self.btn_Dengue)

        self.btn_ECG = QPushButton(self.Lab_test_list)
        self.btn_ECG.setObjectName(u"btn_ECG")
        self.btn_ECG.setMaximumSize(QSize(170, 170))
        self.btn_ECG.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image: url(:/images/images/images/ECG.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/images/images/images/ECG_hover.png);\n"
"\n"
"\n"
"}")
        self.btn_ECG.setIconSize(QSize(164, 164))

        self.lab_layout_3.addWidget(self.btn_ECG)


        self.verticalLayout_19.addLayout(self.lab_layout_3)

        self.lab_layout_1 = QHBoxLayout()
        self.lab_layout_1.setObjectName(u"lab_layout_1")
        self.btn_fullbody = QPushButton(self.Lab_test_list)
        self.btn_fullbody.setObjectName(u"btn_fullbody")
        self.btn_fullbody.setMaximumSize(QSize(170, 170))
        self.btn_fullbody.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image: url(:/images/images/images/FullBodyCheckup.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/images/images/images/FullBodyCheckup_hover.png);\n"
"}")
        self.btn_fullbody.setIconSize(QSize(164, 164))

        self.lab_layout_1.addWidget(self.btn_fullbody)

        self.btn_hormone = QPushButton(self.Lab_test_list)
        self.btn_hormone.setObjectName(u"btn_hormone")
        self.btn_hormone.setMaximumSize(QSize(170, 170))
        self.btn_hormone.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image:url(:/images/images/images/HormoneTest.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image:url(:/images/images/images/HormoneTest_hover.png);\n"
"}")
        self.btn_hormone.setIconSize(QSize(164, 164))

        self.lab_layout_1.addWidget(self.btn_hormone)

        self.btn_iron = QPushButton(self.Lab_test_list)
        self.btn_iron.setObjectName(u"btn_iron")
        self.btn_iron.setMaximumSize(QSize(170, 170))
        self.btn_iron.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image: url(:/images/images/images/IronStudies.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image:  url(:/images/images/images/IronStudies_hover.png);\n"
"\n"
"}")
        self.btn_iron.setIconSize(QSize(164, 164))

        self.lab_layout_1.addWidget(self.btn_iron)

        self.btn_kidney = QPushButton(self.Lab_test_list)
        self.btn_kidney.setObjectName(u"btn_kidney")
        self.btn_kidney.setMaximumSize(QSize(170, 170))
        self.btn_kidney.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image: url(:/images/images/images/Kidneytest.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/images/images/images/Kidneytest_hover.png);\n"
"\n"
"}")
        self.btn_kidney.setIconSize(QSize(164, 164))

        self.lab_layout_1.addWidget(self.btn_kidney)

        self.btn_liver = QPushButton(self.Lab_test_list)
        self.btn_liver.setObjectName(u"btn_liver")
        self.btn_liver.setMaximumSize(QSize(170, 170))
        self.btn_liver.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image:url(:/images/images/images/LiverTest.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/images/images/images/LiverTest_hover.png);\n"
"}")
        self.btn_liver.setIconSize(QSize(164, 164))

        self.lab_layout_1.addWidget(self.btn_liver)

        self.btn_lungs = QPushButton(self.Lab_test_list)
        self.btn_lungs.setObjectName(u"btn_lungs")
        self.btn_lungs.setMaximumSize(QSize(170, 170))
        self.btn_lungs.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image: url(:/images/images/images/Lungstest.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/images/images/images/Lungstest_hover.png);\n"
"}")
        self.btn_lungs.setIconSize(QSize(164, 164))

        self.lab_layout_1.addWidget(self.btn_lungs)


        self.verticalLayout_19.addLayout(self.lab_layout_1)

        self.lab_layout_2 = QHBoxLayout()
        self.lab_layout_2.setObjectName(u"lab_layout_2")
        self.btn_stress = QPushButton(self.Lab_test_list)
        self.btn_stress.setObjectName(u"btn_stress")
        self.btn_stress.setMaximumSize(QSize(170, 170))
        self.btn_stress.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image: url(:/images/images/images/StressMangment.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/images/images/images/StressMangment_hover.png);\n"
"}")
        self.btn_stress.setIconSize(QSize(164, 164))

        self.lab_layout_2.addWidget(self.btn_stress)

        self.btn_thyroid = QPushButton(self.Lab_test_list)
        self.btn_thyroid.setObjectName(u"btn_thyroid")
        self.btn_thyroid.setMaximumSize(QSize(170, 170))
        self.btn_thyroid.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"    color: #f8f8f2;\n"
"   background-image: url(:/images/images/images/ThyroidTest.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/images/images/images/ThyroidTest_hover.png);\n"
"\n"
"}")
        self.btn_thyroid.setIconSize(QSize(164, 164))

        self.lab_layout_2.addWidget(self.btn_thyroid)

        self.pushButton_14 = QPushButton(self.Lab_test_list)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMaximumSize(QSize(170, 170))
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: white;\n"
"    color: #f8f8f2;\n"
"}")

        self.lab_layout_2.addWidget(self.pushButton_14)

        self.pushButton_17 = QPushButton(self.Lab_test_list)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMaximumSize(QSize(170, 170))
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: white;\n"
"    color: #f8f8f2;\n"
"}")

        self.lab_layout_2.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.Lab_test_list)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMaximumSize(QSize(170, 170))
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: white;\n"
"    color: #f8f8f2;\n"
"}")

        self.lab_layout_2.addWidget(self.pushButton_18)

        self.pushButton_11 = QPushButton(self.Lab_test_list)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(170, 170))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: white;\n"
"    color: #f8f8f2;\n"
"}")

        self.lab_layout_2.addWidget(self.pushButton_11)


        self.verticalLayout_19.addLayout(self.lab_layout_2)


        self.verticalLayout_18.addWidget(self.Lab_test_list)

        self.stackedWidget.addWidget(self.Lab_test_Booking)
        self.Medicine_Order = QWidget()
        self.Medicine_Order.setObjectName(u"Medicine_Order")
        self.verticalLayout_21 = QVBoxLayout(self.Medicine_Order)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Order_Layout = QFrame(self.Medicine_Order)
        self.Order_Layout.setObjectName(u"Order_Layout")
        self.Order_Layout.setFrameShape(QFrame.NoFrame)
        self.Order_Layout.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.Order_Layout)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.Order_Label = QFrame(self.Order_Layout)
        self.Order_Label.setObjectName(u"Order_Label")
        self.Order_Label.setMinimumSize(QSize(0, 30))
        self.Order_Label.setMaximumSize(QSize(16777215, 30))
        self.Order_Label.setFrameShape(QFrame.StyledPanel)
        self.Order_Label.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.Order_Label)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Title_Order = QLabel(self.Order_Label)
        self.Title_Order.setObjectName(u"Title_Order")
        self.Title_Order.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_10.addWidget(self.Title_Order)


        self.verticalLayout_22.addWidget(self.Order_Label)

        self.Order_Search = QFrame(self.Order_Layout)
        self.Order_Search.setObjectName(u"Order_Search")
        self.Order_Search.setMinimumSize(QSize(0, 45))
        self.Order_Search.setMaximumSize(QSize(16777215, 45))
        self.Order_Search.setFrameShape(QFrame.NoFrame)
        self.Order_Search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.Order_Search)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_search_text = QFrame(self.Order_Search)
        self.frame_search_text.setObjectName(u"frame_search_text")
        self.frame_search_text.setMinimumSize(QSize(0, 45))
        self.frame_search_text.setMaximumSize(QSize(16777215, 45))
        self.frame_search_text.setFrameShape(QFrame.NoFrame)
        self.frame_search_text.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_search_text)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.medicine_search = QLineEdit(self.frame_search_text)
        self.medicine_search.setObjectName(u"medicine_search")
        self.medicine_search.setMinimumSize(QSize(0, 45))
        self.medicine_search.setMaximumSize(QSize(16777215, 45))

        self.horizontalLayout_13.addWidget(self.medicine_search)


        self.horizontalLayout_11.addWidget(self.frame_search_text)

        self.frame_search_btn = QFrame(self.Order_Search)
        self.frame_search_btn.setObjectName(u"frame_search_btn")
        self.frame_search_btn.setMinimumSize(QSize(130, 45))
        self.frame_search_btn.setMaximumSize(QSize(130, 45))
        self.frame_search_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_search_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_search_btn)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_search_Medicine = QPushButton(self.frame_search_btn)
        self.btn_search_Medicine.setObjectName(u"btn_search_Medicine")
        self.btn_search_Medicine.setMinimumSize(QSize(0, 45))
        self.btn_search_Medicine.setMaximumSize(QSize(16777215, 45))
        self.btn_search_Medicine.setIcon(icon7)

        self.horizontalLayout_14.addWidget(self.btn_search_Medicine)


        self.horizontalLayout_11.addWidget(self.frame_search_btn)


        self.verticalLayout_22.addWidget(self.Order_Search)

        self.Order_Display = QFrame(self.Order_Layout)
        self.Order_Display.setObjectName(u"Order_Display")
        self.Order_Display.setFrameShape(QFrame.NoFrame)
        self.Order_Display.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.Order_Display)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.frame_Medicie_Search = QFrame(self.Order_Display)
        self.frame_Medicie_Search.setObjectName(u"frame_Medicie_Search")
        self.frame_Medicie_Search.setFrameShape(QFrame.NoFrame)
        self.frame_Medicie_Search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_Medicie_Search)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.SearchMedicine = QListWidget(self.frame_Medicie_Search)
        self.SearchMedicine.setObjectName(u"SearchMedicine")

        self.verticalLayout_25.addWidget(self.SearchMedicine)


        self.horizontalLayout_15.addWidget(self.frame_Medicie_Search)

        self.frame_Ordered_Medicine = QFrame(self.Order_Display)
        self.frame_Ordered_Medicine.setObjectName(u"frame_Ordered_Medicine")
        self.frame_Ordered_Medicine.setFrameShape(QFrame.StyledPanel)
        self.frame_Ordered_Medicine.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_Ordered_Medicine)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_Ordered_Medicine)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 30))
        self.frame_title.setMaximumSize(QSize(16777215, 30))
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(self.frame_title)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 114, 164);\n"
"font: 700 14pt \"Segoe UI\";\n"
"border-radius : 5px;")
        self.title_label.setMargin(0)

        self.horizontalLayout_16.addWidget(self.title_label)


        self.verticalLayout_23.addWidget(self.frame_title)

        self.frame_ordered_Med = QFrame(self.frame_Ordered_Medicine)
        self.frame_ordered_Med.setObjectName(u"frame_ordered_Med")
        self.frame_ordered_Med.setFrameShape(QFrame.StyledPanel)
        self.frame_ordered_Med.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_ordered_Med)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.ordered_List = QListWidget(self.frame_ordered_Med)
        self.ordered_List.setObjectName(u"ordered_List")

        self.verticalLayout_24.addWidget(self.ordered_List)


        self.verticalLayout_23.addWidget(self.frame_ordered_Med)

        self.frame_btn_oirder = QFrame(self.frame_Ordered_Medicine)
        self.frame_btn_oirder.setObjectName(u"frame_btn_oirder")
        self.frame_btn_oirder.setMinimumSize(QSize(0, 45))
        self.frame_btn_oirder.setMaximumSize(QSize(16777215, 45))
        self.frame_btn_oirder.setFrameShape(QFrame.NoFrame)
        self.frame_btn_oirder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_btn_oirder)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 5, 0)
        self.Total_Amount_Label = QLabel(self.frame_btn_oirder)
        self.Total_Amount_Label.setObjectName(u"Total_Amount_Label")
        self.Total_Amount_Label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_17.addWidget(self.Total_Amount_Label)

        self.Total_Amount_Input = QLineEdit(self.frame_btn_oirder)
        self.Total_Amount_Input.setObjectName(u"Total_Amount_Input")
        self.Total_Amount_Input.setMinimumSize(QSize(0, 45))
        self.Total_Amount_Input.setMaximumSize(QSize(16777215, 45))

        self.horizontalLayout_17.addWidget(self.Total_Amount_Input)

        self.btn_order = QPushButton(self.frame_btn_oirder)
        self.btn_order.setObjectName(u"btn_order")
        self.btn_order.setMinimumSize(QSize(130, 45))
        self.btn_order.setMaximumSize(QSize(130, 45))
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_order.setIcon(icon8)

        self.horizontalLayout_17.addWidget(self.btn_order)


        self.verticalLayout_23.addWidget(self.frame_btn_oirder)


        self.horizontalLayout_15.addWidget(self.frame_Ordered_Medicine)


        self.verticalLayout_22.addWidget(self.Order_Display)


        self.verticalLayout_21.addWidget(self.Order_Layout)

        self.stackedWidget.addWidget(self.Medicine_Order)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(250, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"  border-bottom-right-radius: 10px;")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font7 = QFont()
        font7.setBold(False)
        font7.setItalic(False)
        self.creditsLabel.setFont(font7)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"MedTech", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Your Health, Our Priority", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_profile.setText(QCoreApplication.translate("MainWindow", u"Your Account", None))
        self.btn_appointment.setText(QCoreApplication.translate("MainWindow", u"Doctor Appointment", None))
        self.btn_labtest.setText(QCoreApplication.translate("MainWindow", u"Book LabTest", None))
        self.btn_medicine.setText(QCoreApplication.translate("MainWindow", u"Order Medicine", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Info Credit", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.creditText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">MedTech</span>      </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.IT License</span>      </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Raj Dalsaniya</span>      </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Version : 1.0.0 (Beta)</span>      </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"rajdalsaniya1995@gmail.com\"><span style=\" font-weight:700; text-decoration: underline; color:#aaaaff;\">Follow Me on Social Media:</span></a></p></body></html>", None))
        self.btn_facebook.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.btn_telegram.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.btn_twitter.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.btn_github.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.btn_instagram.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"MedTech - One Step Solution For Hospital and Patients", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.Label_Welcome.setText(QCoreApplication.translate("MainWindow", u"Dear Piyush , Welcome to MedTech", None))
        self.Promo_Label.setText("")
        self.Profile_Details_Label.setText(QCoreApplication.translate("MainWindow", u"Profile Details", None))
        self.Pic_Upload.setText("")
        self.btn_upload.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.Profile_Description_Label.setText(QCoreApplication.translate("MainWindow", u"Welcome To MedTech. Please Fill All Details in  Profile", None))
        self.LastName_Label.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.LastName_Input.setText("")
        self.Email_Label.setText(QCoreApplication.translate("MainWindow", u"Email         ", None))
        self.Email_Input.setText("")
        self.UserName_Label.setText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.UserName_Input.setText("")
        self.btn_details_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_promo.setText("")
        self.FirstName_Label.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.FirstName_Input.setText("")
        self.Gender_Label.setText(QCoreApplication.translate("MainWindow", u"Gender  ", None))
        self.Gender_Input.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Gender", None))
        self.Gender_Input.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.Gender_Input.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.BirthDate_Label.setText(QCoreApplication.translate("MainWindow", u"Birth Date", None))
        self.Title_Label.setText(QCoreApplication.translate("MainWindow", u" Search Doctor And Book Appoinment", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_covid.setText("")
        self.btn_cancer.setText("")
        self.btn_heptatitis.setText("")
        self.btn_B12_D3.setText("")
        self.btn_Dengue.setText("")
        self.btn_ECG.setText("")
        self.btn_fullbody.setText("")
        self.btn_hormone.setText("")
        self.btn_iron.setText("")
        self.btn_kidney.setText("")
        self.btn_liver.setText("")
        self.btn_lungs.setText("")
        self.btn_stress.setText("")
        self.btn_thyroid.setText("")
        self.pushButton_14.setText("")
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
        self.pushButton_11.setText("")
        self.Title_Order.setText(QCoreApplication.translate("MainWindow", u" Search Medicine And Order", None))
        self.btn_search_Medicine.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Your Cart <img src=\":/icons/images/icons/cil-cart.png\"/></p></body></html>", None))
        self.Total_Amount_Label.setText(QCoreApplication.translate("MainWindow", u"Total Amount :", None))
        self.btn_order.setText(QCoreApplication.translate("MainWindow", u"Order ", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Raj Dalsaniya", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0.1(Beta)", None))
    # retranslateUi

