# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BookingZqNjCX.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
from . Images_Resource_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QSize(600, 600))
        MainWindow.setMaximumSize(QSize(600, 600))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMinimumSize(QSize(600, 600))
        self.styleSheet.setMaximumSize(QSize(600, 600))
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
"border-top-left-radius: 10px;\n"
"\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
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
"  "
                        "  color: #f8f8f2;\n"
"    border-radius:10px;\n"
"\n"
"   \n"
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
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#content  QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;"
                        "\n"
"}\n"
"#content QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#content QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"#leftBox\n"
"{\n"
"border-top-left-radius : 10px;\n"
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
"    background-color: rgba(235, 235, 235, 100);\n"
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
""
                        "	selection-color: rgb(255, 255, 255);\n"
"}\n"
"QCalendarWidget QToolButton{\n"
"    background-color:rgb(98, 114, 164);\n"
"   	selection-background-color: rgb(255, 121, 199);\n"
"	selection-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#qt_calendar_calendarview {\n"
"    outline: 0px;\n"
"    selection-background-color: rgb(195, 155, 255);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bgApp)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.bgApp)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 45))
        self.contentTopBg.setMaximumSize(QSize(16777215, 45))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setMaximumSize(QSize(16777215, 50))
        self.titleRightInfo.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(75, 0))
        self.rightButtons.setMaximumSize(QSize(75, 16777215))
        self.rightButtons.setFrameShape(QFrame.StyledPanel)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(0, 0))
        self.minimizeAppBtn.setMaximumSize(QSize(35, 35))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(0, 0))
        self.closeAppBtn.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.content = QFrame(self.bgApp)
        self.content.setObjectName(u"content")
        self.content.setMaximumSize(QSize(16777215, 16777215))
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Frame_Title = QFrame(self.content)
        self.Frame_Title.setObjectName(u"Frame_Title")
        self.Frame_Title.setFrameShape(QFrame.StyledPanel)
        self.Frame_Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Frame_Title)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Frame_Doc_Name = QFrame(self.Frame_Title)
        self.Frame_Doc_Name.setObjectName(u"Frame_Doc_Name")
        self.Frame_Doc_Name.setMinimumSize(QSize(0, 40))
        self.Frame_Doc_Name.setMaximumSize(QSize(16777215, 40))
        self.Frame_Doc_Name.setFrameShape(QFrame.NoFrame)
        self.Frame_Doc_Name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Frame_Doc_Name)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Doc_Name = QLabel(self.Frame_Doc_Name)
        self.Doc_Name.setObjectName(u"Doc_Name")
        self.Doc_Name.setMinimumSize(QSize(0, 40))
        self.Doc_Name.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.Doc_Name.setFont(font)
        self.Doc_Name.setStyleSheet(u"font: 14pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.verticalLayout_5.addWidget(self.Doc_Name)


        self.horizontalLayout_4.addWidget(self.Frame_Doc_Name)

        self.frame_Date_Selector = QFrame(self.Frame_Title)
        self.frame_Date_Selector.setObjectName(u"frame_Date_Selector")
        self.frame_Date_Selector.setMinimumSize(QSize(0, 40))
        self.frame_Date_Selector.setMaximumSize(QSize(16777215, 40))
        self.frame_Date_Selector.setFrameShape(QFrame.NoFrame)
        self.frame_Date_Selector.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_Date_Selector)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Date_Selector = QDateEdit(self.frame_Date_Selector)
        self.Date_Selector.setObjectName(u"Date_Selector")
        self.Date_Selector.setMinimumSize(QSize(0, 40))
        self.Date_Selector.setMaximumSize(QSize(16777215, 40))
        self.Date_Selector.setStyleSheet(u"QDateEdit {\n"
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

        self.verticalLayout_4.addWidget(self.Date_Selector)


        self.horizontalLayout_4.addWidget(self.frame_Date_Selector)


        self.verticalLayout_3.addWidget(self.Frame_Title)

        self.Layout_1 = QHBoxLayout()
        self.Layout_1.setObjectName(u"Layout_1")
        self.btn_slot_01 = QPushButton(self.content)
        self.btn_slot_01.setObjectName(u"btn_slot_01")
        self.btn_slot_01.setMinimumSize(QSize(0, 0))
        self.btn_slot_01.setMaximumSize(QSize(75, 50))

        self.Layout_1.addWidget(self.btn_slot_01)

        self.btn_slot_02 = QPushButton(self.content)
        self.btn_slot_02.setObjectName(u"btn_slot_02")
        self.btn_slot_02.setMaximumSize(QSize(75, 45))

        self.Layout_1.addWidget(self.btn_slot_02)

        self.btn_slot_03 = QPushButton(self.content)
        self.btn_slot_03.setObjectName(u"btn_slot_03")
        self.btn_slot_03.setMaximumSize(QSize(75, 50))

        self.Layout_1.addWidget(self.btn_slot_03)

        self.btn_slot_04 = QPushButton(self.content)
        self.btn_slot_04.setObjectName(u"btn_slot_04")
        self.btn_slot_04.setMaximumSize(QSize(75, 50))

        self.Layout_1.addWidget(self.btn_slot_04)

        self.btn_slot_05 = QPushButton(self.content)
        self.btn_slot_05.setObjectName(u"btn_slot_05")
        self.btn_slot_05.setMaximumSize(QSize(75, 50))

        self.Layout_1.addWidget(self.btn_slot_05)

        self.btn_slot_06 = QPushButton(self.content)
        self.btn_slot_06.setObjectName(u"btn_slot_06")
        self.btn_slot_06.setMaximumSize(QSize(75, 50))

        self.Layout_1.addWidget(self.btn_slot_06)


        self.verticalLayout_3.addLayout(self.Layout_1)

        self.Layout_2 = QHBoxLayout()
        self.Layout_2.setObjectName(u"Layout_2")
        self.btn_slot_07 = QPushButton(self.content)
        self.btn_slot_07.setObjectName(u"btn_slot_07")
        self.btn_slot_07.setMaximumSize(QSize(75, 50))

        self.Layout_2.addWidget(self.btn_slot_07)

        self.btn_slot_08 = QPushButton(self.content)
        self.btn_slot_08.setObjectName(u"btn_slot_08")
        self.btn_slot_08.setMaximumSize(QSize(75, 45))

        self.Layout_2.addWidget(self.btn_slot_08)

        self.btn_slot_09 = QPushButton(self.content)
        self.btn_slot_09.setObjectName(u"btn_slot_09")
        self.btn_slot_09.setMaximumSize(QSize(75, 50))

        self.Layout_2.addWidget(self.btn_slot_09)

        self.btn_slot_10 = QPushButton(self.content)
        self.btn_slot_10.setObjectName(u"btn_slot_10")
        self.btn_slot_10.setMaximumSize(QSize(75, 50))

        self.Layout_2.addWidget(self.btn_slot_10)

        self.btn_slot_11 = QPushButton(self.content)
        self.btn_slot_11.setObjectName(u"btn_slot_11")
        self.btn_slot_11.setMaximumSize(QSize(75, 50))

        self.Layout_2.addWidget(self.btn_slot_11)

        self.btn_slot_12 = QPushButton(self.content)
        self.btn_slot_12.setObjectName(u"btn_slot_12")
        self.btn_slot_12.setMaximumSize(QSize(75, 50))

        self.Layout_2.addWidget(self.btn_slot_12)


        self.verticalLayout_3.addLayout(self.Layout_2)

        self.information_text = QTextEdit(self.content)
        self.information_text.setObjectName(u"information_text")
        self.information_text.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_3.addWidget(self.information_text)


        self.verticalLayout_2.addWidget(self.content)

        self.bottomBar = QFrame(self.bgApp)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMaximumSize(QSize(16777215, 20))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(485, 16777215))

        self.horizontalLayout_7.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_7.addWidget(self.version)


        self.verticalLayout_2.addWidget(self.bottomBar)


        self.verticalLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"MedTech - Slot Booking", None))
        self.minimizeAppBtn.setText("")
        self.closeAppBtn.setText("")
        self.Doc_Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_slot_01.setText(QCoreApplication.translate("MainWindow", u"9:00-9:30", None))
        self.btn_slot_02.setText(QCoreApplication.translate("MainWindow", u"9:30-10:00", None))
        self.btn_slot_03.setText(QCoreApplication.translate("MainWindow", u"10:30-11:00", None))
        self.btn_slot_04.setText(QCoreApplication.translate("MainWindow", u"10:10-10:30", None))
        self.btn_slot_05.setText(QCoreApplication.translate("MainWindow", u"11:00-11:30", None))
        self.btn_slot_06.setText(QCoreApplication.translate("MainWindow", u"11:30-12:30", None))
        self.btn_slot_07.setText(QCoreApplication.translate("MainWindow", u"12:30-13:30", None))
        self.btn_slot_08.setText(QCoreApplication.translate("MainWindow", u"13:30-14:30", None))
        self.btn_slot_09.setText(QCoreApplication.translate("MainWindow", u"17:30-18:30", None))
        self.btn_slot_10.setText(QCoreApplication.translate("MainWindow", u"18:30-19:30", None))
        self.btn_slot_11.setText(QCoreApplication.translate("MainWindow", u"19:30-20:30", None))
        self.btn_slot_12.setText(QCoreApplication.translate("MainWindow", u"20:30-21:25", None))
        self.information_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">There are multiple slots avilable for each doctors. Each slot timings have 10 appointment available. if all appointment is booked then slot label color is changed which indicate no appointment are available.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">If there are any difficulties then please let us know over this mail id : </span><a href=\"rajdalsaniya1995@gmail.com\"><span style=\" font-size:16pt; text-decoration: underline; color:#0000ff;\">rajdalsaniya1995@gmail.com</span></a></p></body></html>", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Created By: Raj Dalsaniya", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v. 1.0.0(Beta)", None))
    # retranslateUi

