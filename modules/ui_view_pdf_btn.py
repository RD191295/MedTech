# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_pdf_btn.ui'
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
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from . Images_Resource_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(640, 268)
        MainWindow.setMaximumSize(QSize(640, 268))
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
"	bac"
                        "kground-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"")
        self.StyleLayout = QVBoxLayout(self.stylesheet)
        self.StyleLayout.setSpacing(0)
        self.StyleLayout.setObjectName(u"StyleLayout")
        self.StyleLayout.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.stylesheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShape(QFrame.StyledPanel)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.bgApp)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.bgApp)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMaximumSize(QSize(16777215, 40))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.btntopLayout = QHBoxLayout(self.contentTopBg)
        self.btntopLayout.setSpacing(0)
        self.btntopLayout.setObjectName(u"btntopLayout")
        self.btntopLayout.setContentsMargins(0, 0, 0, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.leftBoxLayout = QHBoxLayout(self.leftBox)
        self.leftBoxLayout.setSpacing(0)
        self.leftBoxLayout.setObjectName(u"leftBoxLayout")
        self.leftBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")

        self.leftBoxLayout.addWidget(self.titleRightInfo)


        self.btntopLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMaximumSize(QSize(100, 16777215))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.btnLayout = QHBoxLayout(self.rightButtons)
        self.btnLayout.setSpacing(0)
        self.btnLayout.setObjectName(u"btnLayout")
        self.btnLayout.setContentsMargins(0, 0, 0, 0)
        self.MinimizeAppBtn = QPushButton(self.rightButtons)
        self.MinimizeAppBtn.setObjectName(u"MinimizeAppBtn")
        self.MinimizeAppBtn.setMinimumSize(QSize(35, 35))
        self.MinimizeAppBtn.setMaximumSize(QSize(35, 35))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MinimizeAppBtn.setIcon(icon)

        self.btnLayout.addWidget(self.MinimizeAppBtn)

        self.CloseAppBtn = QPushButton(self.rightButtons)
        self.CloseAppBtn.setObjectName(u"CloseAppBtn")
        self.CloseAppBtn.setMinimumSize(QSize(35, 35))
        self.CloseAppBtn.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseAppBtn.setIcon(icon1)

        self.btnLayout.addWidget(self.CloseAppBtn)


        self.btntopLayout.addWidget(self.rightButtons)


        self.verticalLayout.addWidget(self.contentTopBg)

        self.bgcontentFrame = QFrame(self.bgApp)
        self.bgcontentFrame.setObjectName(u"bgcontentFrame")
        self.bgcontentFrame.setMaximumSize(QSize(16777215, 16777215))
        self.bgcontentFrame.setFrameShape(QFrame.NoFrame)
        self.bgcontentFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bgcontentFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 2)
        self.instruction = QPlainTextEdit(self.bgcontentFrame)
        self.instruction.setObjectName(u"instruction")
        self.instruction.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"	font: 700 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}")

        self.horizontalLayout.addWidget(self.instruction)


        self.verticalLayout.addWidget(self.bgcontentFrame)

        self.pagesContainer = QFrame(self.bgApp)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setMinimumSize(QSize(0, 45))
        self.pagesContainer.setMaximumSize(QSize(16777215, 45))
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.bgbtnLayout = QHBoxLayout(self.pagesContainer)
        self.bgbtnLayout.setSpacing(3)
        self.bgbtnLayout.setObjectName(u"bgbtnLayout")
        self.bgbtnLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_book_other = QPushButton(self.pagesContainer)
        self.btn_book_other.setObjectName(u"btn_book_other")
        self.btn_book_other.setMinimumSize(QSize(0, 40))
        self.btn_book_other.setMaximumSize(QSize(16777215, 40))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-action-redo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_book_other.setIcon(icon2)

        self.bgbtnLayout.addWidget(self.btn_book_other)

        self.btn_view = QPushButton(self.pagesContainer)
        self.btn_view.setObjectName(u"btn_view")
        self.btn_view.setMinimumSize(QSize(0, 40))
        self.btn_view.setMaximumSize(QSize(16777215, 40))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-view-module.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_view.setIcon(icon3)

        self.bgbtnLayout.addWidget(self.btn_view)

        self.btn_cancel = QPushButton(self.pagesContainer)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 40))
        self.btn_cancel.setMaximumSize(QSize(16777215, 40))
        self.btn_cancel.setIcon(icon1)

        self.bgbtnLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addWidget(self.pagesContainer)

        self.bottomBar = QFrame(self.bgApp)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.bgcreditLayout = QHBoxLayout(self.bottomBar)
        self.bgcreditLayout.setSpacing(0)
        self.bgcreditLayout.setObjectName(u"bgcreditLayout")
        self.bgcreditLayout.setContentsMargins(0, 3, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")

        self.bgcreditLayout.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setMaximumSize(QSize(81, 16777215))

        self.bgcreditLayout.addWidget(self.version)


        self.verticalLayout.addWidget(self.bottomBar)


        self.StyleLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"MedTech ", None))
        self.MinimizeAppBtn.setText("")
        self.CloseAppBtn.setText("")
        self.instruction.setPlainText("")
        self.btn_book_other.setText(QCoreApplication.translate("MainWindow", u"Book Other Test", None))
        self.btn_view.setText(QCoreApplication.translate("MainWindow", u"View Invoice", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Created By : Raj Dalsaniya", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v 1.0.0(Beta)", None))
    # retranslateUi

