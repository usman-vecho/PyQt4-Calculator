# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_calculator_new.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(679, 536)
        MainWindow.setMaximumSize(QtCore.QSize(679, 536))
        MainWindow.setStyleSheet(_fromUtf8("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 641, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 170, 641, 361))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.sin = QtGui.QPushButton(self.frame)
        self.sin.setGeometry(QtCore.QRect(0, 10, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.sin.setFont(font)
        self.sin.setObjectName(_fromUtf8("sin"))
        self.cos = QtGui.QPushButton(self.frame)
        self.cos.setGeometry(QtCore.QRect(130, 10, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cos.setFont(font)
        self.cos.setObjectName(_fromUtf8("cos"))
        self.tan = QtGui.QPushButton(self.frame)
        self.tan.setGeometry(QtCore.QRect(260, 10, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.tan.setFont(font)
        self.tan.setObjectName(_fromUtf8("tan"))
        self.bracket_opened = QtGui.QPushButton(self.frame)
        self.bracket_opened.setGeometry(QtCore.QRect(390, 10, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.bracket_opened.setFont(font)
        self.bracket_opened.setObjectName(_fromUtf8("bracket_opened"))
        self.tan_ = QtGui.QPushButton(self.frame)
        self.tan_.setGeometry(QtCore.QRect(260, 70, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.tan_.setFont(font)
        self.tan_.setObjectName(_fromUtf8("tan_"))
        self.backspace = QtGui.QPushButton(self.frame)
        self.backspace.setGeometry(QtCore.QRect(390, 70, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.backspace.setFont(font)
        self.backspace.setObjectName(_fromUtf8("backspace"))
        self.sin_ = QtGui.QPushButton(self.frame)
        self.sin_.setGeometry(QtCore.QRect(0, 70, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.sin_.setFont(font)
        self.sin_.setObjectName(_fromUtf8("sin_"))
        self.cos_ = QtGui.QPushButton(self.frame)
        self.cos_.setGeometry(QtCore.QRect(130, 70, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cos_.setFont(font)
        self.cos_.setObjectName(_fromUtf8("cos_"))
        self.btn9 = QtGui.QPushButton(self.frame)
        self.btn9.setGeometry(QtCore.QRect(260, 130, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn9.setFont(font)
        self.btn9.setObjectName(_fromUtf8("btn9"))
        self.add = QtGui.QPushButton(self.frame)
        self.add.setGeometry(QtCore.QRect(390, 130, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.add.setFont(font)
        self.add.setObjectName(_fromUtf8("add"))
        self.btn7 = QtGui.QPushButton(self.frame)
        self.btn7.setGeometry(QtCore.QRect(0, 130, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn7.setFont(font)
        self.btn7.setObjectName(_fromUtf8("btn7"))
        self.btn8 = QtGui.QPushButton(self.frame)
        self.btn8.setGeometry(QtCore.QRect(130, 130, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn8.setFont(font)
        self.btn8.setObjectName(_fromUtf8("btn8"))
        self.btn6 = QtGui.QPushButton(self.frame)
        self.btn6.setGeometry(QtCore.QRect(260, 190, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn6.setFont(font)
        self.btn6.setObjectName(_fromUtf8("btn6"))
        self.subtract = QtGui.QPushButton(self.frame)
        self.subtract.setGeometry(QtCore.QRect(390, 190, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.subtract.setFont(font)
        self.subtract.setObjectName(_fromUtf8("subtract"))
        self.btn4 = QtGui.QPushButton(self.frame)
        self.btn4.setGeometry(QtCore.QRect(0, 190, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn4.setFont(font)
        self.btn4.setObjectName(_fromUtf8("btn4"))
        self.btn5 = QtGui.QPushButton(self.frame)
        self.btn5.setGeometry(QtCore.QRect(130, 190, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn5.setFont(font)
        self.btn5.setObjectName(_fromUtf8("btn5"))
        self.btn3 = QtGui.QPushButton(self.frame)
        self.btn3.setGeometry(QtCore.QRect(260, 250, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn3.setFont(font)
        self.btn3.setObjectName(_fromUtf8("btn3"))
        self.multiply = QtGui.QPushButton(self.frame)
        self.multiply.setGeometry(QtCore.QRect(390, 250, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.multiply.setFont(font)
        self.multiply.setObjectName(_fromUtf8("multiply"))
        self.btn1 = QtGui.QPushButton(self.frame)
        self.btn1.setGeometry(QtCore.QRect(0, 250, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn1.setFont(font)
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.btn2 = QtGui.QPushButton(self.frame)
        self.btn2.setGeometry(QtCore.QRect(130, 250, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn2.setFont(font)
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.btnpi = QtGui.QPushButton(self.frame)
        self.btnpi.setGeometry(QtCore.QRect(260, 310, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btnpi.setFont(font)
        self.btnpi.setObjectName(_fromUtf8("btnpi"))
        self.divide = QtGui.QPushButton(self.frame)
        self.divide.setGeometry(QtCore.QRect(390, 310, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.divide.setFont(font)
        self.divide.setObjectName(_fromUtf8("divide"))
        self.btn0 = QtGui.QPushButton(self.frame)
        self.btn0.setGeometry(QtCore.QRect(0, 310, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn0.setFont(font)
        self.btn0.setObjectName(_fromUtf8("btn0"))
        self.btndot = QtGui.QPushButton(self.frame)
        self.btndot.setGeometry(QtCore.QRect(130, 310, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btndot.setFont(font)
        self.btndot.setObjectName(_fromUtf8("btndot"))
        self.bracket_closed = QtGui.QPushButton(self.frame)
        self.bracket_closed.setGeometry(QtCore.QRect(520, 10, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.bracket_closed.setFont(font)
        self.bracket_closed.setObjectName(_fromUtf8("bracket_closed"))
        self.power = QtGui.QPushButton(self.frame)
        self.power.setGeometry(QtCore.QRect(520, 70, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.power.setFont(font)
        self.power.setObjectName(_fromUtf8("power"))
        self.equals = QtGui.QPushButton(self.frame)
        self.equals.setGeometry(QtCore.QRect(520, 310, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.equals.setFont(font)
        self.equals.setObjectName(_fromUtf8("equals"))
        self.square_root = QtGui.QPushButton(self.frame)
        self.square_root.setGeometry(QtCore.QRect(520, 190, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.square_root.setFont(font)
        self.square_root.setObjectName(_fromUtf8("square_root"))
        self.power_square = QtGui.QPushButton(self.frame)
        self.power_square.setGeometry(QtCore.QRect(520, 130, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.power_square.setFont(font)
        self.power_square.setObjectName(_fromUtf8("power_square"))
        self.ac = QtGui.QPushButton(self.frame)
        self.ac.setGeometry(QtCore.QRect(520, 250, 112, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.ac.setFont(font)
        self.ac.setObjectName(_fromUtf8("ac"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.sin.setText(_translate("MainWindow", "sin", None))
        self.cos.setText(_translate("MainWindow", "cos", None))
        self.tan.setText(_translate("MainWindow", "tan", None))
        self.bracket_opened.setText(_translate("MainWindow", "(", None))
        self.tan_.setText(_translate("MainWindow", "tan-1", None))
        self.backspace.setText(_translate("MainWindow", "<--", None))
        self.sin_.setText(_translate("MainWindow", "sin-1", None))
        self.cos_.setText(_translate("MainWindow", "cos-1", None))
        self.btn9.setText(_translate("MainWindow", "9", None))
        self.add.setText(_translate("MainWindow", "+", None))
        self.btn7.setText(_translate("MainWindow", "7", None))
        self.btn8.setText(_translate("MainWindow", "8", None))
        self.btn6.setText(_translate("MainWindow", "6", None))
        self.subtract.setText(_translate("MainWindow", "-", None))
        self.btn4.setText(_translate("MainWindow", "4", None))
        self.btn5.setText(_translate("MainWindow", "5", None))
        self.btn3.setText(_translate("MainWindow", "3", None))
        self.multiply.setText(_translate("MainWindow", "x", None))
        self.btn1.setText(_translate("MainWindow", "1", None))
        self.btn2.setText(_translate("MainWindow", "2", None))
        self.btnpi.setText(_translate("MainWindow", "π", None))
        self.divide.setText(_translate("MainWindow", "÷", None))
        self.btn0.setText(_translate("MainWindow", "0", None))
        self.btndot.setText(_translate("MainWindow", ".", None))
        self.bracket_closed.setText(_translate("MainWindow", ")", None))
        self.power.setText(_translate("MainWindow", "pow", None))
        self.equals.setText(_translate("MainWindow", "=", None))
        self.square_root.setText(_translate("MainWindow", "√ ", None))
        self.power_square.setText(_translate("MainWindow", "x**2", None))
        self.ac.setText(_translate("MainWindow", "AC", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

