# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cart_layoutLHiprM.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import Images_Resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1434, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 671, 208))
        self.BgLayout = QVBoxLayout(self.layoutWidget)
        self.BgLayout.setObjectName(u"BgLayout")
        self.BgLayout.setContentsMargins(0, 0, 0, 0)
        self.DetailsLayout = QHBoxLayout()
        self.DetailsLayout.setObjectName(u"DetailsLayout")
        self.pic_label = QLabel(self.layoutWidget)
        self.pic_label.setObjectName(u"pic_label")
        self.pic_label.setMinimumSize(QSize(209, 0))
        self.pic_label.setMaximumSize(QSize(209, 16777215))

        self.DetailsLayout.addWidget(self.pic_label)

        self.Medicine_Details_Layout = QVBoxLayout()
        self.Medicine_Details_Layout.setObjectName(u"Medicine_Details_Layout")

        self.DetailsLayout.addLayout(self.Medicine_Details_Layout)

        self.Price_Composition_Layout = QVBoxLayout()
        self.Price_Composition_Layout.setObjectName(u"Price_Composition_Layout")
        self.Medicine_Name = QLabel(self.layoutWidget)
        self.Medicine_Name.setObjectName(u"Medicine_Name")
        self.Medicine_Name.setMinimumSize(QSize(0, 30))
        self.Medicine_Name.setMaximumSize(QSize(16777215, 30))
        self.Medicine_Name.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")

        self.Price_Composition_Layout.addWidget(self.Medicine_Name)

        self.Price_Per_Unit_Label = QLabel(self.layoutWidget)
        self.Price_Per_Unit_Label.setObjectName(u"Price_Per_Unit_Label")
        self.Price_Per_Unit_Label.setMinimumSize(QSize(0, 52))
        self.Price_Per_Unit_Label.setMaximumSize(QSize(16777215, 45))
        self.Price_Per_Unit_Label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")

        self.Price_Composition_Layout.addWidget(self.Price_Per_Unit_Label)

        self.Price_Per_Unit_Input = QLineEdit(self.layoutWidget)
        self.Price_Per_Unit_Input.setObjectName(u"Price_Per_Unit_Input")
        self.Price_Per_Unit_Input.setMinimumSize(QSize(0, 35))
        self.Price_Per_Unit_Input.setMaximumSize(QSize(16777215, 35))
        self.Price_Per_Unit_Input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"")

        self.Price_Composition_Layout.addWidget(self.Price_Per_Unit_Input)

        self.Total_Price_Label = QLabel(self.layoutWidget)
        self.Total_Price_Label.setObjectName(u"Total_Price_Label")
        self.Total_Price_Label.setMaximumSize(QSize(16777215, 30))
        self.Total_Price_Label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")

        self.Price_Composition_Layout.addWidget(self.Total_Price_Label)

        self.Total_Price_Input = QLineEdit(self.layoutWidget)
        self.Total_Price_Input.setObjectName(u"Total_Price_Input")
        self.Total_Price_Input.setMinimumSize(QSize(0, 35))
        self.Total_Price_Input.setMaximumSize(QSize(16777215, 35))
        self.Total_Price_Input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"")

        self.Price_Composition_Layout.addWidget(self.Total_Price_Input)


        self.DetailsLayout.addLayout(self.Price_Composition_Layout)

        self.Qunatity__btn_order_Layout = QVBoxLayout()
        self.Qunatity__btn_order_Layout.setObjectName(u"Qunatity__btn_order_Layout")
        self.Quanty_order_Label = QLabel(self.layoutWidget)
        self.Quanty_order_Label.setObjectName(u"Quanty_order_Label")
        self.Quanty_order_Label.setMinimumSize(QSize(0, 40))
        self.Quanty_order_Label.setMaximumSize(QSize(16777215, 40))
        self.Quanty_order_Label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(98, 114, 164);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")

        self.Qunatity__btn_order_Layout.addWidget(self.Quanty_order_Label)

        self.Quantity_Layout = QHBoxLayout()
        self.Quantity_Layout.setObjectName(u"Quantity_Layout")
        self.btn_low = QPushButton(self.layoutWidget)
        self.btn_low.setObjectName(u"btn_low")
        self.btn_low.setMinimumSize(QSize(45, 45))
        self.btn_low.setMaximumSize(QSize(45, 45))
        self.btn_low.setStyleSheet(u"QPushButton {\n"
"	font: 700 18pt \"Segoe UI\";\n"
"    color: #FFF;\n"
"    border: 2px solid #6272a4;\n"
"    border-radius: 20px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #6272a4\n"
"        );\n"
"    padding: 5px;\n"
"	text-align: center   \n"
" }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #7082b6\n"
"        );\n"
"	border: 2px solid #7082b6;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #546391\n"
"        );\n"
"	border: 2px solid #ff79c6;\n"
"\n"
"    }")

        self.Quantity_Layout.addWidget(self.btn_low)

        self.Quantity_Order_Input = QLabel(self.layoutWidget)
        self.Quantity_Order_Input.setObjectName(u"Quantity_Order_Input")
        self.Quantity_Order_Input.setMinimumSize(QSize(45, 45))
        self.Quantity_Order_Input.setMaximumSize(QSize(45, 45))
        self.Quantity_Order_Input.setStyleSheet(u"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"	font: 700 18pt \"Segoe UI\";\n"
"}\n"
"QLabel:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"QLabel:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}")
        self.Quantity_Order_Input.setAlignment(Qt.AlignCenter)

        self.Quantity_Layout.addWidget(self.Quantity_Order_Input)

        self.btn_high = QPushButton(self.layoutWidget)
        self.btn_high.setObjectName(u"btn_high")
        self.btn_high.setMinimumSize(QSize(45, 45))
        self.btn_high.setMaximumSize(QSize(45, 45))
        self.btn_high.setStyleSheet(u"QPushButton {\n"
"	font: 700 18pt \"Segoe UI\";\n"
"    color: #FFF;\n"
"    border: 2px solid #6272a4;\n"
"    border-radius: 20px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #6272a4\n"
"        );\n"
"    padding: 5px;\n"
"	text-align: center   \n"
" }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #7082b6\n"
"        );\n"
"	border: 2px solid #7082b6;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #546391\n"
"        );\n"
"	border: 2px solid #ff79c6;\n"
"\n"
"    }")

        self.Quantity_Layout.addWidget(self.btn_high)


        self.Qunatity__btn_order_Layout.addLayout(self.Quantity_Layout)

        self.btn_cart = QPushButton(self.layoutWidget)
        self.btn_cart.setObjectName(u"btn_cart")
        self.btn_cart.setMinimumSize(QSize(0, 45))
        self.btn_cart.setMaximumSize(QSize(16777215, 45))
        self.btn_cart.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cart.setIcon(icon)

        self.Qunatity__btn_order_Layout.addWidget(self.btn_cart)


        self.DetailsLayout.addLayout(self.Qunatity__btn_order_Layout)


        self.BgLayout.addLayout(self.DetailsLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pic_label.setText("")
        self.Medicine_Name.setText(QCoreApplication.translate("MainWindow", u"Viroshield Mouth Spray, 30 ml", None))
        self.Price_Per_Unit_Label.setText(QCoreApplication.translate("MainWindow", u"Price Per Unit", None))
        self.Total_Price_Label.setText(QCoreApplication.translate("MainWindow", u"Total Price", None))
        self.Quanty_order_Label.setText(QCoreApplication.translate("MainWindow", u"Quantiy Order", None))
        self.btn_low.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Quantity_Order_Input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_high.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_cart.setText(QCoreApplication.translate("MainWindow", u"Remove All", None))
    # retranslateUi

