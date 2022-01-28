# IMPORT MAIN FILE
# /////////////////////////////

from main import *

# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions_pdf_View(QMainWindow):
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if not status:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.MaximizeAppBtn.setToolTip("Restore")
            self.ui.MaximizeAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))

        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.MaximizeAppBtn.setToolTip("Maximize")
            self.ui.MaximizeAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))


    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions_pdf_View(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions_pdf_View.maximize_restore(self))

        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        # STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # MINIMIZE
        self.ui.MinimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.MaximizeAppBtn.clicked.connect(lambda: UIFunctions_pdf_View.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.CloseAppBtn.clicked.connect(lambda: self.close())

    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS

