# PYSIDE MODULE
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MyCustomWidget(QWidget):
    """
    Show Doctor's Information after searching particular doctor
    information from database:
    1. Doctor's Name
    2. Doctor's Specialization
    3. Hospital Name
    4. charge of doctor
    5. Doctor's Photo
    6. Year of experience
    7. there is one button for booking appointment
    """

    def __init__(self, parent=None):
        super(MyCustomWidget, self).__init__(parent)

        self.bg_horizontal = QHBoxLayout()
        self.bg_horizontal.setObjectName(u"bg_horizontal")
        self.bg_horizontal.setContentsMargins(0, 0, 0, 0)
        self.Doctor_Pic = QLabel()
        self.Doctor_Pic.setObjectName(u"Doctor_Pic")
        self.Doctor_Pic.setMinimumSize(QSize(150, 150))
        self.Doctor_Pic.setMaximumSize(QSize(150, 150))

        self.bg_horizontal.addWidget(self.Doctor_Pic)

        self.bg_part_1 = QVBoxLayout()
        self.bg_part_1.setObjectName(u"bg_part_1")
        self.Doctor_Name_Layout = QHBoxLayout()
        self.Doctor_Name_Layout.setObjectName(u"Doctor_Name_Layout")
        self.Doctor_Name_label = QLabel()
        self.Doctor_Name_label.setObjectName(u"Doctor_Name_label")
        self.Doctor_Name_label.setMinimumSize(QSize(140, 45))
        self.Doctor_Name_label.setMaximumSize(QSize(140, 45))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.Doctor_Name_label.setFont(font)

        self.Doctor_Name_Layout.addWidget(self.Doctor_Name_label)

        self.Doctor_Name_Input = QLineEdit()
        self.Doctor_Name_Input.setObjectName(u"Doctor_Name_Input")
        self.Doctor_Name_Input.setMinimumSize(QSize(180, 45))
        self.Doctor_Name_Input.setMaximumSize(QSize(180, 45))

        self.Doctor_Name_Layout.addWidget(self.Doctor_Name_Input)

        self.bg_part_1.addLayout(self.Doctor_Name_Layout)

        self.Speciality_Layout = QHBoxLayout()
        self.Speciality_Layout.setObjectName(u"Speciality_Layout")
        self.Speciality_Label = QLabel()
        self.Speciality_Label.setObjectName(u"Speciality_Label")
        self.Speciality_Label.setMinimumSize(QSize(140, 45))
        self.Speciality_Label.setMaximumSize(QSize(140, 45))
        self.Speciality_Label.setFont(font)

        self.Speciality_Layout.addWidget(self.Speciality_Label)

        self.Speciality_Input = QLineEdit()
        self.Speciality_Input.setObjectName(u"Speciality_Input")
        self.Speciality_Input.setMinimumSize(QSize(180, 45))
        self.Speciality_Input.setMaximumSize(QSize(180, 45))

        self.Speciality_Layout.addWidget(self.Speciality_Input)

        self.bg_part_1.addLayout(self.Speciality_Layout)

        self.Hospital_Name_Layout = QHBoxLayout()
        self.Hospital_Name_Layout.setObjectName(u"Hospital_Name_Layout")
        self.Hospital_Name_Label = QLabel()
        self.Hospital_Name_Label.setObjectName(u"Hospital_Name_Label")
        self.Hospital_Name_Label.setMinimumSize(QSize(140, 45))
        self.Hospital_Name_Label.setMaximumSize(QSize(140, 45))
        self.Hospital_Name_Label.setFont(font)

        self.Hospital_Name_Layout.addWidget(self.Hospital_Name_Label)

        self.Hospital_Name_Input = QLineEdit()
        self.Hospital_Name_Input.setObjectName(u"Hospital_Name_Input")
        self.Hospital_Name_Input.setMinimumSize(QSize(180, 45))
        self.Hospital_Name_Input.setMaximumSize(QSize(180, 45))

        self.Hospital_Name_Layout.addWidget(self.Hospital_Name_Input)

        self.bg_part_1.addLayout(self.Hospital_Name_Layout)

        self.bg_horizontal.addLayout(self.bg_part_1)

        self.bg_part_2 = QVBoxLayout()
        self.bg_part_2.setObjectName(u"bg_part_2")
        self.YOE_Layout = QHBoxLayout()
        self.YOE_Layout.setObjectName(u"YOE_Layout")
        self.Experience_Label = QLabel()
        self.Experience_Label.setObjectName(u"Experience_Label")
        self.Experience_Label.setMinimumSize(QSize(190, 45))
        self.Experience_Label.setMaximumSize(QSize(190, 45))
        self.Experience_Label.setFont(font)

        self.YOE_Layout.addWidget(self.Experience_Label)

        self.Experience_Input = QLineEdit()
        self.Experience_Input.setObjectName(u"Experience_Input")
        self.Experience_Input.setMinimumSize(QSize(190, 45))
        self.Experience_Input.setMaximumSize(QSize(190, 45))

        self.YOE_Layout.addWidget(self.Experience_Input)

        self.bg_part_2.addLayout(self.YOE_Layout)

        self.charge_Layout = QHBoxLayout()
        self.charge_Layout.setObjectName(u"charge_Layout")
        self.Charge_Label = QLabel()
        self.Charge_Label.setObjectName(u"Charge_Label")
        self.Charge_Label.setMinimumSize(QSize(190, 45))
        self.Charge_Label.setMaximumSize(QSize(190, 45))
        self.Charge_Label.setFont(font)

        self.charge_Layout.addWidget(self.Charge_Label)

        self.Charge_Input = QLineEdit()
        self.Charge_Input.setObjectName(u"Charge_Input")
        self.Charge_Input.setMinimumSize(QSize(190, 45))
        self.Charge_Input.setMaximumSize(QSize(190, 45))

        self.charge_Layout.addWidget(self.Charge_Input)

        self.bg_part_2.addLayout(self.charge_Layout)

        self.btn_layout = QHBoxLayout()
        self.btn_layout.setObjectName(u"btn_layout")
        self.btn_space = QSpacerItem(230, 45, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.btn_layout.addItem(self.btn_space)

        self.btn_book = QPushButton()
        self.btn_book.setObjectName(u"btn_book")
        self.btn_book.setMinimumSize(QSize(150, 45))
        self.btn_book.setMaximumSize(QSize(150, 45))

        self.btn_layout.addWidget(self.btn_book)

        self.bg_part_2.addLayout(self.btn_layout)

        self.bg_horizontal.addLayout(self.bg_part_2)

        self.setLayout(self.bg_horizontal)

        # SET LABEL TEXT
        self.Doctor_Pic.setText("")
        self.Doctor_Name_label.setText(u"Doctor Name :")
        self.Speciality_Label.setText(u"Speciality :")
        self.Hospital_Name_Label.setText(u"Hospital Name:")
        self.Experience_Label.setText(u"Total Experience :")
        self.Charge_Label.setText(u"consultation Charge :")
        self.btn_book.setText(u"Book")

