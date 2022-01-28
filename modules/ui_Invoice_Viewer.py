# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Invoice_Viewer.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from .Images_Resource_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 880)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setMinimumSize(QSize(0, 0))
        self.stylesheet.setMaximumSize(QSize(16777215, 16777215))
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: #6272a4;\n"
"   border-top-left-radius:10px;\n"
"	border-top-right-radius:10px;\n"
"}\n"
"#contentBottom{\n"
"	border-to"
                        "p: 3px solid #bd93f9;\n"
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
"/* Bottom Bar */\n"
"#bottomBar { background-color: #495474; border-bottom-left-radius:10px;border-bottom-right-radius:10px; }\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"\n"
"\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"")
        self.styleLayout = QVBoxLayout(self.stylesheet)
        self.styleLayout.setSpacing(0)
        self.styleLayout.setObjectName(u"styleLayout")
        self.styleLayout.setContentsMargins(10, 10, 10, 10)
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
        self.contentTopBg.setMaximumSize(QSize(16777215, 40))
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
        self.title_layout = QHBoxLayout(self.leftBox)
        self.title_layout.setSpacing(0)
        self.title_layout.setObjectName(u"title_layout")
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")

        self.title_layout.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMaximumSize(QSize(150, 16777215))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.btn_Layout = QHBoxLayout(self.rightButtons)
        self.btn_Layout.setSpacing(6)
        self.btn_Layout.setObjectName(u"btn_Layout")
        self.btn_Layout.setContentsMargins(0, 0, 0, 0)
        self.MinimizeAppBtn = QPushButton(self.rightButtons)
        self.MinimizeAppBtn.setObjectName(u"MinimizeAppBtn")
        self.MinimizeAppBtn.setMinimumSize(QSize(35, 35))
        self.MinimizeAppBtn.setMaximumSize(QSize(35, 35))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MinimizeAppBtn.setIcon(icon)

        self.btn_Layout.addWidget(self.MinimizeAppBtn)

        self.MaximizeAppBtn = QPushButton(self.rightButtons)
        self.MaximizeAppBtn.setObjectName(u"MaximizeAppBtn")
        self.MaximizeAppBtn.setMinimumSize(QSize(35, 35))
        self.MaximizeAppBtn.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MaximizeAppBtn.setIcon(icon1)

        self.btn_Layout.addWidget(self.MaximizeAppBtn)

        self.CloseAppBtn = QPushButton(self.rightButtons)
        self.CloseAppBtn.setObjectName(u"CloseAppBtn")
        self.CloseAppBtn.setMinimumSize(QSize(35, 35))
        self.CloseAppBtn.setMaximumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseAppBtn.setIcon(icon2)
        self.CloseAppBtn.setCheckable(False)

        self.btn_Layout.addWidget(self.CloseAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.bgLayout.addWidget(self.contentTopBg)

        self.content_frame = QFrame(self.bgApp)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMinimumSize(QSize(0, 0))
        self.content_frame.setMaximumSize(QSize(16777215, 16777215))
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)

        self.bgLayout.addWidget(self.content_frame)

        self.bottomBar = QFrame(self.bgApp)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.credit_Layout = QHBoxLayout(self.bottomBar)
        self.credit_Layout.setSpacing(0)
        self.credit_Layout.setObjectName(u"credit_Layout")
        self.credit_Layout.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")

        self.credit_Layout.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setMaximumSize(QSize(83, 16777215))

        self.credit_Layout.addWidget(self.version)


        self.bgLayout.addWidget(self.bottomBar)


        self.styleLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u" Medtech --- View Invoice", None))
        self.MinimizeAppBtn.setText("")
        self.MaximizeAppBtn.setText("")
        self.CloseAppBtn.setText("")
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Created By : Raj A. Dalsaniya", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"V 1.0.0(Beta)", None))
    # retranslateUi

