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

# IMPORT MAIN FILE
# /////////////////////////////

from main import *

# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions_pdf_View_btn(QMainWindow):

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions_pdf_View_btn(self):

        # STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.titleRightInfo.mouseMoveEvent = moveWindow

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # MINIMIZE
        self.ui.MinimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # CLOSE APPLICATION
        self.ui.CloseAppBtn.clicked.connect(lambda: self.close())

    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS

