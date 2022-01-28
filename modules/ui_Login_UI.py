# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_UI.ui'
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
    QVBoxLayout, QWidget)
from . Images_Resource_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 640)
        MainWindow.setMinimumSize(QSize(820, 640))
        MainWindow.setMaximumSize(QSize(820, 640))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMaximumSize(QSize(820, 600))
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: #333;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
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
"\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
""
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
"}\n"
"\n"
"\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid #6a7cb1;\n"
"}\n"
"\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: #6272a4;\n"
"    border-top-left-radius:10px;\n"
"    border-top-right-radius:10px;\n"
"}\n"
"#bottomBar{\n"
"	border-top: 3px solid #bd93f9;\n"
"    border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"\n"
"\n"
"}\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* Top "
                        "Buttons */\n"
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
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"\n"
"QPushButton#login_sign_btn, #Login_Input,#btn_Register{\n"
"	background-color:qlineargradient(spread:pad, x1:0.169, y1:0.136364, x2:1, y2:0.347, stop:0 rgba(106, 124, 177, 255), stop:0.751244 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
" \n"
"\n"
"}"
                        "\n"
"\n"
"QPushButton#login_sign_btn:hover,#Login_Input:hover,#btn_Register:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#login_sign_btn:pressed, #Login_Input:pressed,#btn_Register:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#btn_facebook, #btn_instagram, #btn_twitter, #btn_github,#btn_telegram\n"
"{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"font: 14pt \"Social Media Circled\";\n"
"}\n"
"\n"
"QPushButton#btn_facebook:hover, #btn_github:hover, #btn_twitter:hover, #btn_instagram:hover,#btn_telegram:hover{\n"
"	color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#btn_facebook:pressed, #btn_twitter:pressed, #btn_github:pressed, #btn_instagram:pressed,#btn_telegram:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color:rgba(91, 88, 53,"
                        " 255);\n"
"}\n"
"\n"
"\n"
"#label_description\n"
"{\n"
"\n"
"	background-color: #6272a4;\n"
"    border-radius:4px;\n"
"    padding : 20px;\n"
"}")
        self.appMargins = QHBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QVBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.bgApp)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"border-left-top-radius: 10px;\n"
"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_2.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setMaximumSize(QSize(95, 16777215))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.rightButtons.setFont(font)
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.appLayout.addWidget(self.contentTopBg)

        self.content = QFrame(self.bgApp)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(0, 0))
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.content)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ContentLeftBox = QFrame(self.content)
        self.ContentLeftBox.setObjectName(u"ContentLeftBox")
        self.ContentLeftBox.setFont(font)
        self.ContentLeftBox.setFrameShape(QFrame.NoFrame)
        self.ContentLeftBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.ContentLeftBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.label_logo = QLabel(self.ContentLeftBox)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setFrameShape(QFrame.StyledPanel)

        self.verticalLayout.addWidget(self.label_logo)


        self.horizontalLayout_5.addWidget(self.ContentLeftBox)

        self.ContentRightBox = QFrame(self.content)
        self.ContentRightBox.setObjectName(u"ContentRightBox")
        self.ContentRightBox.setMaximumSize(QSize(500, 16777215))
        self.ContentRightBox.setFrameShape(QFrame.NoFrame)
        self.ContentRightBox.setFrameShadow(QFrame.Raised)
        self.Login_Label = QLabel(self.ContentRightBox)
        self.Login_Label.setObjectName(u"Login_Label")
        self.Login_Label.setGeometry(QRect(80, 10, 100, 40))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.Login_Label.setFont(font1)
        self.Login_Label.setStyleSheet(u"color:rgba(0, 0, 0, 200);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.Register_Label = QLabel(self.ContentRightBox)
        self.Register_Label.setObjectName(u"Register_Label")
        self.Register_Label.setGeometry(QRect(190, 10, 121, 40))
        self.Register_Label.setFont(font1)
        self.Register_Label.setStyleSheet(u"color:rgba(0, 0, 0, 200);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.Email_Signup = QLineEdit(self.ContentRightBox)
        self.Email_Signup.setObjectName(u"Email_Signup")
        self.Email_Signup.setGeometry(QRect(10, 70, 190, 40))
        self.Email_Signup.setFont(font)
        self.Email_Signup.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.Email_Signup.setEchoMode(QLineEdit.Normal)
        self.Last_Name_Signup = QLineEdit(self.ContentRightBox)
        self.Last_Name_Signup.setObjectName(u"Last_Name_Signup")
        self.Last_Name_Signup.setGeometry(QRect(220, 70, 131, 41))
        self.Last_Name_Signup.setFont(font)
        self.Last_Name_Signup.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.First_Name_Signup = QLineEdit(self.ContentRightBox)
        self.First_Name_Signup.setObjectName(u"First_Name_Signup")
        self.First_Name_Signup.setGeometry(QRect(10, 130, 111, 31))
        self.First_Name_Signup.setFont(font)
        self.First_Name_Signup.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.username_input = QLineEdit(self.ContentRightBox)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(110, 200, 190, 40))
        self.username_input.setFont(font)
        self.username_input.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.Password_Signup = QLineEdit(self.ContentRightBox)
        self.Password_Signup.setObjectName(u"Password_Signup")
        self.Password_Signup.setGeometry(QRect(10, 220, 190, 40))
        self.Password_Signup.setFont(font)
        self.Password_Signup.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.Password_Signup.setEchoMode(QLineEdit.Password)
        self.Password_input = QLineEdit(self.ContentRightBox)
        self.Password_input.setObjectName(u"Password_input")
        self.Password_input.setGeometry(QRect(200, 260, 190, 40))
        self.Password_input.setFont(font)
        self.Password_input.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.Password_input.setEchoMode(QLineEdit.Password)
        self.Con_Password_Signup = QLineEdit(self.ContentRightBox)
        self.Con_Password_Signup.setObjectName(u"Con_Password_Signup")
        self.Con_Password_Signup.setGeometry(QRect(10, 290, 190, 40))
        self.Con_Password_Signup.setFont(font)
        self.Con_Password_Signup.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.Con_Password_Signup.setEchoMode(QLineEdit.Password)
        self.Login_Input = QPushButton(self.ContentRightBox)
        self.Login_Input.setObjectName(u"Login_Input")
        self.Login_Input.setGeometry(QRect(40, 360, 190, 40))
        self.Login_Input.setFont(font)
        self.btn_Register = QPushButton(self.ContentRightBox)
        self.btn_Register.setObjectName(u"btn_Register")
        self.btn_Register.setGeometry(QRect(190, 410, 190, 40))
        self.btn_Register.setFont(font)
        self.Forget_Label = QLabel(self.ContentRightBox)
        self.Forget_Label.setObjectName(u"Forget_Label")
        self.Forget_Label.setGeometry(QRect(20, 460, 301, 41))
        self.Forget_Label.setStyleSheet(u"color:rgba(0, 0, 0, 210);")
        self.layoutWidget = QWidget(self.ContentRightBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 190, 271, 34))
        self.Social_Media_Layout = QHBoxLayout(self.layoutWidget)
        self.Social_Media_Layout.setObjectName(u"Social_Media_Layout")
        self.Social_Media_Layout.setContentsMargins(0, 0, 0, 0)
        self.btn_telegram = QPushButton(self.layoutWidget)
        self.btn_telegram.setObjectName(u"btn_telegram")
        self.btn_telegram.setMinimumSize(QSize(30, 30))
        self.btn_telegram.setMaximumSize(QSize(30, 30))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_telegram.setFont(font2)
        self.btn_telegram.setStyleSheet(u"")

        self.Social_Media_Layout.addWidget(self.btn_telegram)

        self.btn_github = QPushButton(self.layoutWidget)
        self.btn_github.setObjectName(u"btn_github")
        self.btn_github.setMinimumSize(QSize(30, 30))
        self.btn_github.setMaximumSize(QSize(30, 30))

        self.Social_Media_Layout.addWidget(self.btn_github)

        self.btn_instagram = QPushButton(self.layoutWidget)
        self.btn_instagram.setObjectName(u"btn_instagram")
        self.btn_instagram.setMinimumSize(QSize(30, 30))
        self.btn_instagram.setMaximumSize(QSize(30, 30))
        self.btn_instagram.setFont(font2)

        self.Social_Media_Layout.addWidget(self.btn_instagram)

        self.btn_twitter = QPushButton(self.layoutWidget)
        self.btn_twitter.setObjectName(u"btn_twitter")
        self.btn_twitter.setMinimumSize(QSize(30, 30))
        self.btn_twitter.setMaximumSize(QSize(30, 30))
        self.btn_twitter.setFont(font2)

        self.Social_Media_Layout.addWidget(self.btn_twitter)

        self.btn_facebook = QPushButton(self.layoutWidget)
        self.btn_facebook.setObjectName(u"btn_facebook")
        self.btn_facebook.setMinimumSize(QSize(30, 30))
        self.btn_facebook.setMaximumSize(QSize(30, 30))
        self.btn_facebook.setFont(font2)
        self.btn_facebook.setStyleSheet(u"")

        self.Social_Media_Layout.addWidget(self.btn_facebook)

        self.login_sign_btn = QPushButton(self.ContentRightBox)
        self.login_sign_btn.setObjectName(u"login_sign_btn")
        self.login_sign_btn.setGeometry(QRect(0, 40, 30, 40))
        self.login_sign_btn.setFont(font)
        self.login_sign_btn.setStyleSheet(u"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.login_sign_btn.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.ContentRightBox)


        self.appLayout.addWidget(self.content)

        self.bottomBar = QFrame(self.bgApp)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_4.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")

        self.horizontalLayout_4.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_size_grip)


        self.appLayout.addWidget(self.bottomBar)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"MedTech - One Step Solution For Hospital and Patients", None))
        self.minimizeAppBtn.setText("")
        self.maximizeRestoreAppBtn.setText("")
        self.closeAppBtn.setText("")
        self.label_logo.setText("")
        self.Login_Label.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.Register_Label.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.Email_Signup.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Email Address", None))
        self.Last_Name_Signup.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Last Name", None))
        self.First_Name_Signup.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  First Name", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  User Name", None))
        self.Password_Signup.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Password", None))
        self.Password_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Password", None))
        self.Con_Password_Signup.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Confirm Password", None))
        self.Login_Input.setText(QCoreApplication.translate("MainWindow", u"L o g  I n", None))
        self.btn_Register.setText(QCoreApplication.translate("MainWindow", u"R e g i s t e r", None))
        self.Forget_Label.setText(QCoreApplication.translate("MainWindow", u"Forgot your User Name or password?", None))
        self.btn_telegram.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.btn_github.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.btn_instagram.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.btn_twitter.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.btn_facebook.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.login_sign_btn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Created By : Raj Dalsaniya", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"                                                                                                              v1.0.0(Beta)", None))
    # retranslateUi

