# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Splash_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(56, 58, 89);\n"
"color:rgb(220, 220, 220);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.app_title = QLabel(self.drop_shadow_frame)
        self.app_title.setObjectName(u"app_title")
        self.app_title.setGeometry(QRect(0, 90, 661, 61))
        self.app_title.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"font: 40pt \"Segoe UI\";")
        self.app_title.setAlignment(Qt.AlignCenter)
        self.app_tagline = QLabel(self.drop_shadow_frame)
        self.app_tagline.setObjectName(u"app_tagline")
        self.app_tagline.setGeometry(QRect(190, 150, 271, 31))
        self.app_tagline.setStyleSheet(u"color: rgb(98, 114, 164);\n"
"font: 17pt \"Segoe UI\";")
        self.app_progress = QProgressBar(self.drop_shadow_frame)
        self.app_progress.setObjectName(u"app_progress")
        self.app_progress.setGeometry(QRect(40, 240, 591, 31))
        self.app_progress.setStyleSheet(u"QProgressBar\n"
"{\n"
"background-color: rgb(98, 114, 164);\n"
"color: rgb(200, 200, 200);\n"
"border-style:none;\n"
"border-radius:10px;\n"
"text-align :center\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255)  , stop:1  rgba(170, 85, 255, 255));\n"
"}")
        self.app_progress.setValue(24)
        self.label_loading = QLabel(self.drop_shadow_frame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(140, 280, 401, 31))
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);\n"
"font: 17pt \"Segoe UI\";")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credit = QLabel(self.drop_shadow_frame)
        self.label_credit.setObjectName(u"label_credit")
        self.label_credit.setGeometry(QRect(480, 350, 171, 20))
        self.label_credit.setStyleSheet(u"color: rgb(98, 114, 164);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">MedTech - v1.0.0 (Beta)</span></p></body></html>", None))
        self.app_tagline.setText(QCoreApplication.translate("MainWindow", u"<strong>Your Health </strong> ,Our Priority", None))
        self.label_loading.setText(QCoreApplication.translate("MainWindow", u"loading.........................", None))
        self.label_credit.setText(QCoreApplication.translate("MainWindow", u"Created By : Raj Dalsaniya", None))
    # retranslateUi

