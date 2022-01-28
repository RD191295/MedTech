# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Booking_InfoQHqyEr.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
from . Images_Resource_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"QWidget{\n"
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
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: #6272a4;\n"
"}\n"
"#contentBot"
                        "tom{\n"
"	border-top: 3px solid #bd93f9;\n"
"}\n"
"\n"
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
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#frame_btn QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-"
                        "color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"#frame_btn QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#frame_btn QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.stylesheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.stylesheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.bgLayout = QVBoxLayout(self.bgApp)
        self.bgLayout.setSpacing(0)
        self.bgLayout.setObjectName(u"bgLayout")
        self.bgLayout.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.bgApp)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        self.leftBox.setStyleSheet(u"")
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMaximumSize(QSize(100, 16777215))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMaximumSize(QSize(45, 45))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMaximumSize(QSize(45, 45))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.bgLayout.addWidget(self.contentTopBg)

        self.content = QFrame(self.bgApp)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.frame_title = QFrame(self.content)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMaximumSize(QSize(16777215, 45))
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(0, 45))
        self.label_title.setMaximumSize(QSize(16777215, 45))
        self.label_title.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLabel {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QLabel:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLabel:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_title)


        self.verticalLayout_2.addWidget(self.frame_title)

        self.frame_content = QFrame(self.content)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_content)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_details = QFrame(self.frame_content)
        self.frame_details.setObjectName(u"frame_details")
        self.frame_details.setMaximumSize(QSize(400, 16777215))
        self.frame_details.setFrameShape(QFrame.NoFrame)
        self.frame_details.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_details)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.name_layout = QHBoxLayout()
        self.name_layout.setObjectName(u"name_layout")
        self.name_label = QLabel(self.frame_details)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setMinimumSize(QSize(105, 45))
        self.name_label.setMaximumSize(QSize(105, 45))
        self.name_label.setStyleSheet(u"QLabel {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"}\n"
"QLabel:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLabel:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.name_layout.addWidget(self.name_label)

        self.name_input = QLineEdit(self.frame_details)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMaximumSize(QSize(16777215, 45))
        self.name_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.name_layout.addWidget(self.name_input)


        self.verticalLayout_4.addLayout(self.name_layout)

        self.lastname_layout = QHBoxLayout()
        self.lastname_layout.setObjectName(u"lastname_layout")
        self.lastname_label = QLabel(self.frame_details)
        self.lastname_label.setObjectName(u"lastname_label")
        self.lastname_label.setMinimumSize(QSize(105, 45))
        self.lastname_label.setMaximumSize(QSize(105, 45))
        self.lastname_label.setStyleSheet(u"QLabel {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"\n"
"}\n"
"QLabel:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLabel:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.lastname_layout.addWidget(self.lastname_label)

        self.lastname_input = QLineEdit(self.frame_details)
        self.lastname_input.setObjectName(u"lastname_input")
        self.lastname_input.setMaximumSize(QSize(16777215, 45))
        self.lastname_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.lastname_layout.addWidget(self.lastname_input)


        self.verticalLayout_4.addLayout(self.lastname_layout)

        self.mobileno_layout = QHBoxLayout()
        self.mobileno_layout.setObjectName(u"mobileno_layout")
        self.mobile_label = QLabel(self.frame_details)
        self.mobile_label.setObjectName(u"mobile_label")
        self.mobile_label.setMinimumSize(QSize(105, 45))
        self.mobile_label.setMaximumSize(QSize(105, 45))
        self.mobile_label.setStyleSheet(u"QLabel {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"        border-radius:5px;\n"
"\n"
"}\n"
"QLabel:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLabel:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.mobileno_layout.addWidget(self.mobile_label)

        self.mobile_input = QLineEdit(self.frame_details)
        self.mobile_input.setObjectName(u"mobile_input")
        self.mobile_input.setMaximumSize(QSize(16777215, 45))
        self.mobile_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.mobileno_layout.addWidget(self.mobile_input)


        self.verticalLayout_4.addLayout(self.mobileno_layout)

        self.city_layout = QHBoxLayout()
        self.city_layout.setObjectName(u"city_layout")
        self.city_label = QLabel(self.frame_details)
        self.city_label.setObjectName(u"city_label")
        self.city_label.setMinimumSize(QSize(105, 45))
        self.city_label.setMaximumSize(QSize(105, 45))
        self.city_label.setStyleSheet(u"QLabel {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"\n"
"}\n"
"QLabel:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLabel:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.city_layout.addWidget(self.city_label)

        self.city_input = QLineEdit(self.frame_details)
        self.city_input.setObjectName(u"city_input")
        self.city_input.setMaximumSize(QSize(16777215, 45))
        self.city_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.city_layout.addWidget(self.city_input)


        self.verticalLayout_4.addLayout(self.city_layout)

        self.address_layout = QHBoxLayout()
        self.address_layout.setObjectName(u"address_layout")
        self.address_label = QLabel(self.frame_details)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setMinimumSize(QSize(105, 0))
        self.address_label.setMaximumSize(QSize(105, 90))
        self.address_label.setStyleSheet(u"QLabel {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"\n"
"}\n"
"QLabel:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLabel:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.address_layout.addWidget(self.address_label)

        self.address_input = QLineEdit(self.frame_details)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setMinimumSize(QSize(0, 90))
        self.address_input.setMaximumSize(QSize(16777215, 90))
        self.address_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.address_layout.addWidget(self.address_input)


        self.verticalLayout_4.addLayout(self.address_layout)


        self.horizontalLayout_7.addWidget(self.frame_details)

        self.frame__demo = QFrame(self.frame_content)
        self.frame__demo.setObjectName(u"frame__demo")
        self.frame__demo.setFrameShape(QFrame.NoFrame)
        self.frame__demo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame__demo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.charge_Label = QLabel(self.frame__demo)
        self.charge_Label.setObjectName(u"charge_Label")
        self.charge_Label.setMinimumSize(QSize(130, 45))
        self.charge_Label.setMaximumSize(QSize(130, 45))
        self.charge_Label.setStyleSheet(u"QLabel {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"}\n"
"QLabel:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLabel:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.horizontalLayout_8.addWidget(self.charge_Label)

        self.charge_Input = QLineEdit(self.frame__demo)
        self.charge_Input.setObjectName(u"charge_Input")
        self.charge_Input.setMinimumSize(QSize(0, 45))
        self.charge_Input.setMaximumSize(QSize(16777215, 45))
        self.charge_Input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.horizontalLayout_8.addWidget(self.charge_Input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.Info_Text = QTextEdit(self.frame__demo)
        self.Info_Text.setObjectName(u"Info_Text")
        self.Info_Text.setStyleSheet(u"QTextEdit {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid #6272a4;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"    border-radius:5px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.verticalLayout_3.addWidget(self.Info_Text)


        self.horizontalLayout_7.addWidget(self.frame__demo)


        self.verticalLayout_2.addWidget(self.frame_content)

        self.frame_btn = QFrame(self.content)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMinimumSize(QSize(0, 45))
        self.frame_btn.setMaximumSize(QSize(16777215, 45))
        self.frame_btn.setFrameShape(QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_pay = QPushButton(self.frame_btn)
        self.btn_pay.setObjectName(u"btn_pay")
        self.btn_pay.setMaximumSize(QSize(16777215, 45))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icons8-online-payment-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pay.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.btn_pay)

        self.btn_payLater = QPushButton(self.frame_btn)
        self.btn_payLater.setObjectName(u"btn_payLater")
        self.btn_payLater.setMaximumSize(QSize(16777215, 45))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icons8-pay-date-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_payLater.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.btn_payLater)

        self.btn_cancel = QPushButton(self.frame_btn)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 45))
        self.btn_cancel.setMaximumSize(QSize(16777215, 45))
        self.btn_cancel.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.btn_cancel)


        self.verticalLayout_2.addWidget(self.frame_btn)


        self.bgLayout.addWidget(self.content)

        self.bottomBar = QFrame(self.bgApp)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(790, 16777215))

        self.horizontalLayout_4.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_4.addWidget(self.version)


        self.bgLayout.addWidget(self.bottomBar)


        self.verticalLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Book Appointment", None))
        self.minimizeAppBtn.setText("")
        self.closeAppBtn.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Dear Raj ,  You are Booking <strong>Hormone Test</strong> With us.", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"First Name :", None))
        self.lastname_label.setText(QCoreApplication.translate("MainWindow", u"Last Name :", None))
        self.mobile_label.setText(QCoreApplication.translate("MainWindow", u"Mobile Number :", None))
        self.city_label.setText(QCoreApplication.translate("MainWindow", u"City :", None))
        self.address_label.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.address_input.setText("")
        self.charge_Label.setText(QCoreApplication.translate("MainWindow", u"Consultation Charge", None))
        self.Info_Text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Please Fill All Information Ask Here. There is Two Mode for Booking :</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">   1. Pay Later And Book</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">   2.  Pay And Book</s"
                        "pan></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">If you Choose Pay Later And Book , you can pay Consultation charge at Hospital Reception</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">If you choose Pay and Book then you can Pay through Online.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-le"
                        "ft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">If you have any issue while Booking you can contact us Here: </span><a href=\"rajdalsaniya1995@gmail.com\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">rajdalsaniya1995@gmail.com</span></a></p></body></html>", None))
        self.btn_pay.setText(QCoreApplication.translate("MainWindow", u"Pay And Book", None))
        self.btn_payLater.setText(QCoreApplication.translate("MainWindow", u"Pay Later And Book", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Created By: Raj A. Dalsaniya", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v. 1.0.0(Beta)", None))
    # retranslateUi

