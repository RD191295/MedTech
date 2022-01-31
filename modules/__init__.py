# ///////////////////////////////////////////////////////////////
#
# BY: RAJ DALSANIYA
# PROJECT MADE WITH: Qt Designer and PySide6
# PROJECT NAME: DOCTOR APPOINTMENT AND LAB TEST BOOKING SYSTEM
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# PYSIDE MODULE
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWebEngineCore import *


# IMPORT UI FILES
from . ui_main import *
from . ui_Login_UI import *
from . ui_Splash_screen import *
from . ui_Booking import *
from . ui_LabTestBook import *
from . ui_process_bar import *
from . ui_view_pdf_btn import *
from . ui_Invoice_Viewer import *
from . ui_Booking_Info import *
from . ui_Medicine_order_Info import *

# CUSTOM WIDGET FOR LIST WIDGET
from . Doctor_Details_Widget import *
from . Medicine_Details_Widget import *
from . cart_Details_Widget import *

# UI FUNCTION FILES
from . ui_Login_function import *
from . ui_main_functions import *
from . ui_ViewPdf_function import *
from . ui_ViewPdf_btn_function import *

# APP SETTINGS FOR TOGGLE MENU,COLOR ETC
from . app_settings import Settings
