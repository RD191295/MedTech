# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'process_bar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QSizePolicy, QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 135px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.container)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 40, 231, 191))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelCredits = QLabel(self.layoutWidget)
        self.labelCredits.setObjectName(u"labelCredits")
        font = QFont()
        font.setPointSize(9)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet(u"background-color: none;\n"
"color: rgb(155, 155, 255);")
        self.labelCredits.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCredits, 4, 0, 1, 1)

        self.labelTitle = QLabel(self.layoutWidget)
        self.labelTitle.setObjectName(u"labelTitle")
        font1 = QFont()
        font1.setPointSize(12)
        self.labelTitle.setFont(font1)
        self.labelTitle.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.labelLoadingInfo = QLabel(self.layoutWidget)
        self.labelLoadingInfo.setObjectName(u"labelLoadingInfo")
        self.labelLoadingInfo.setMinimumSize(QSize(0, 20))
        self.labelLoadingInfo.setMaximumSize(QSize(16777215, 20))
        self.labelLoadingInfo.setFont(font)
        self.labelLoadingInfo.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(93, 93, 154);\n"
"	color: #FFFFFF;\n"
"	margin-left: 40px;\n"
"	margin-right: 40px;\n"
"}")
        self.labelLoadingInfo.setFrameShape(QFrame.NoFrame)
        self.labelLoadingInfo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoadingInfo, 3, 0, 1, 1)

        self.labelPercentage = QLabel(self.layoutWidget)
        self.labelPercentage.setObjectName(u"labelPercentage")
        font2 = QFont()
        font2.setPointSize(68)
        self.labelPercentage.setFont(font2)
        self.labelPercentage.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage, 2, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.labelCredits.setText(QCoreApplication.translate("SplashScreen", u"by: Raj A. Dalsaniya", None))
        self.labelTitle.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600; color:#9b9bff;\">MedTech</span> India Pvt Ltd</p></body></html>", None))
        self.labelLoadingInfo.setText(QCoreApplication.translate("SplashScreen", u"Please Wait while Booking....", None))
        self.labelPercentage.setText(QCoreApplication.translate("SplashScreen", u"<p><span style=\" font-size:68pt;\">0</span><span style=\" font-size:58pt; vertical-align:super;\">%</span></p>", None))
    # retranslateUi

