# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_calculator_new_blacktheme.ui'
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
        MainWindow.setStyleSheet(_fromUtf8("/*\n"
"    Copyright 2013 Emanuel Claesson\n"
"\n"
"    Licensed under the Apache License, Version 2.0 (the \"License\");\n"
"    you may not use this file except in compliance with the License.\n"
"    You may obtain a copy of the License at\n"
"\n"
"        http://www.apache.org/licenses/LICENSE-2.0\n"
"\n"
"    Unless required by applicable law or agreed to in writing, software\n"
"    distributed under the License is distributed on an \"AS IS\" BASIS,\n"
"    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n"
"    See the License for the specific language governing permissions and\n"
"    limitations under the License.\n"
"*/\n"
"\n"
"/*\n"
"    COLOR_DARK     = #191919\n"
"    COLOR_MEDIUM   = #353535\n"
"    COLOR_MEDLIGHT = #5A5A5A\n"
"    COLOR_LIGHT    = #DDDDDD\n"
"    COLOR_ACCENT   = #3D7848\n"
"*/\n"
"\n"
"* {\n"
"    background: #191919;\n"
"    color: #DDDDDD;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator, QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked, QCheckBox::indicator::unchecked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked, QCheckBox::indicator::checked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"    background: #DDDDDD;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    margin-top: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -7px;\n"
"    left: 7px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #191919;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 15px;\n"
"    margin: 0px 0px 0px 32px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 15px;\n"
"    margin: 32px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #353535;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    border-width: 0px 1px 0px 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border-width: 1px 0px 1px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background:#353535;\n"
"    border: 1px solid #5A5A5A;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    position: absolute;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    left: 15px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    top: 15px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: top left;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"}\n"
"\n"
"QScrollBar:left-arrow, QScrollBar::right-arrow, QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QAbstractButton:pressed {\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    show-decoration-selected: 1;\n"
"    selection-background-color: #3D7848;\n"
"    selection-color: #DDDDDD;\n"
"    alternate-background-color: #353535;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #191919;\n"
"    border: 1px solid #5A5A5A;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QHeaderView::section:selected, QHeaderView::section::checked {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QTableView {\n"
"    gridline-color: #5A5A5A;\n"
"}\n"
"\n"
"QTabBar {\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-radius: 0px;\n"
"    padding: 4px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QSlider {\n"
"    border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    margin: 4px 0px 4px 0px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    margin: 0px 4px 0px 4px;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 15px;\n"
"    margin: -4px 0px -4px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 15px;\n"
"    margin: 0px -4px 0px -4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical, QSlider::sub-page:horizontal {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical, QSlider::add-page:horizontal {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 1px;\n"
"    background-color: #3D7848;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    background: #353535;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 641, 81))
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
        self.sin.setFont(font)
        self.sin.setObjectName(_fromUtf8("sin"))
        self.cos = QtGui.QPushButton(self.frame)
        self.cos.setGeometry(QtCore.QRect(130, 10, 112, 41))
        font = QtGui.QFont()
        self.cos.setFont(font)
        self.cos.setObjectName(_fromUtf8("cos"))
        self.tan = QtGui.QPushButton(self.frame)
        self.tan.setGeometry(QtCore.QRect(260, 10, 112, 41))
        font = QtGui.QFont()
        self.tan.setFont(font)
        self.tan.setObjectName(_fromUtf8("tan"))
        self.bracket_opened = QtGui.QPushButton(self.frame)
        self.bracket_opened.setGeometry(QtCore.QRect(390, 10, 112, 41))
        font = QtGui.QFont()
        self.bracket_opened.setFont(font)
        self.bracket_opened.setObjectName(_fromUtf8("bracket_opened"))
        self.tan_ = QtGui.QPushButton(self.frame)
        self.tan_.setGeometry(QtCore.QRect(260, 70, 112, 41))
        font = QtGui.QFont()
        self.tan_.setFont(font)
        self.tan_.setObjectName(_fromUtf8("tan_"))
        self.backspace = QtGui.QPushButton(self.frame)
        self.backspace.setGeometry(QtCore.QRect(390, 70, 112, 41))
        font = QtGui.QFont()
        self.backspace.setFont(font)
        self.backspace.setObjectName(_fromUtf8("backspace"))
        self.sin_ = QtGui.QPushButton(self.frame)
        self.sin_.setGeometry(QtCore.QRect(0, 70, 112, 41))
        font = QtGui.QFont()
        self.sin_.setFont(font)
        self.sin_.setObjectName(_fromUtf8("sin_"))
        self.cos_ = QtGui.QPushButton(self.frame)
        self.cos_.setGeometry(QtCore.QRect(130, 70, 112, 41))
        font = QtGui.QFont()
        self.cos_.setFont(font)
        self.cos_.setObjectName(_fromUtf8("cos_"))
        self.btn9 = QtGui.QPushButton(self.frame)
        self.btn9.setGeometry(QtCore.QRect(260, 130, 112, 41))
        font = QtGui.QFont()
        self.btn9.setFont(font)
        self.btn9.setObjectName(_fromUtf8("btn9"))
        self.add = QtGui.QPushButton(self.frame)
        self.add.setGeometry(QtCore.QRect(390, 130, 112, 41))
        font = QtGui.QFont()
        self.add.setFont(font)
        self.add.setObjectName(_fromUtf8("add"))
        self.btn7 = QtGui.QPushButton(self.frame)
        self.btn7.setGeometry(QtCore.QRect(0, 130, 112, 41))
        font = QtGui.QFont()
        self.btn7.setFont(font)
        self.btn7.setObjectName(_fromUtf8("btn7"))
        self.btn8 = QtGui.QPushButton(self.frame)
        self.btn8.setGeometry(QtCore.QRect(130, 130, 112, 41))
        font = QtGui.QFont()
        self.btn8.setFont(font)
        self.btn8.setObjectName(_fromUtf8("btn8"))
        self.btn6 = QtGui.QPushButton(self.frame)
        self.btn6.setGeometry(QtCore.QRect(260, 190, 112, 41))
        font = QtGui.QFont()
        self.btn6.setFont(font)
        self.btn6.setObjectName(_fromUtf8("btn6"))
        self.subtract = QtGui.QPushButton(self.frame)
        self.subtract.setGeometry(QtCore.QRect(390, 190, 112, 41))
        font = QtGui.QFont()
        self.subtract.setFont(font)
        self.subtract.setObjectName(_fromUtf8("subtract"))
        self.btn4 = QtGui.QPushButton(self.frame)
        self.btn4.setGeometry(QtCore.QRect(0, 190, 112, 41))
        font = QtGui.QFont()
        self.btn4.setFont(font)
        self.btn4.setObjectName(_fromUtf8("btn4"))
        self.btn5 = QtGui.QPushButton(self.frame)
        self.btn5.setGeometry(QtCore.QRect(130, 190, 112, 41))
        font = QtGui.QFont()
        self.btn5.setFont(font)
        self.btn5.setObjectName(_fromUtf8("btn5"))
        self.btn3 = QtGui.QPushButton(self.frame)
        self.btn3.setGeometry(QtCore.QRect(260, 250, 112, 41))
        font = QtGui.QFont()
        self.btn3.setFont(font)
        self.btn3.setObjectName(_fromUtf8("btn3"))
        self.multiply = QtGui.QPushButton(self.frame)
        self.multiply.setGeometry(QtCore.QRect(390, 250, 112, 41))
        font = QtGui.QFont()
        self.multiply.setFont(font)
        self.multiply.setObjectName(_fromUtf8("multiply"))
        self.btn1 = QtGui.QPushButton(self.frame)
        self.btn1.setGeometry(QtCore.QRect(0, 250, 112, 41))
        font = QtGui.QFont()
        self.btn1.setFont(font)
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.btn2 = QtGui.QPushButton(self.frame)
        self.btn2.setGeometry(QtCore.QRect(130, 250, 112, 41))
        font = QtGui.QFont()
        self.btn2.setFont(font)
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.btnpi = QtGui.QPushButton(self.frame)
        self.btnpi.setGeometry(QtCore.QRect(260, 310, 112, 41))
        font = QtGui.QFont()
        self.btnpi.setFont(font)
        self.btnpi.setObjectName(_fromUtf8("btnpi"))
        self.divide = QtGui.QPushButton(self.frame)
        self.divide.setGeometry(QtCore.QRect(390, 310, 112, 41))
        font = QtGui.QFont()
        self.divide.setFont(font)
        self.divide.setObjectName(_fromUtf8("divide"))
        self.btn0 = QtGui.QPushButton(self.frame)
        self.btn0.setGeometry(QtCore.QRect(0, 310, 112, 41))
        font = QtGui.QFont()
        self.btn0.setFont(font)
        self.btn0.setObjectName(_fromUtf8("btn0"))
        self.btndot = QtGui.QPushButton(self.frame)
        self.btndot.setGeometry(QtCore.QRect(130, 310, 112, 41))
        font = QtGui.QFont()
        self.btndot.setFont(font)
        self.btndot.setObjectName(_fromUtf8("btndot"))
        self.bracket_closed = QtGui.QPushButton(self.frame)
        self.bracket_closed.setGeometry(QtCore.QRect(520, 10, 112, 41))
        font = QtGui.QFont()
        self.bracket_closed.setFont(font)
        self.bracket_closed.setObjectName(_fromUtf8("bracket_closed"))
        self.power = QtGui.QPushButton(self.frame)
        self.power.setGeometry(QtCore.QRect(520, 70, 112, 41))
        font = QtGui.QFont()
        self.power.setFont(font)
        self.power.setObjectName(_fromUtf8("power"))
        self.equals = QtGui.QPushButton(self.frame)
        self.equals.setGeometry(QtCore.QRect(520, 310, 112, 41))
        font = QtGui.QFont()
        self.equals.setFont(font)
        self.equals.setObjectName(_fromUtf8("equals"))
        self.square_root = QtGui.QPushButton(self.frame)
        self.square_root.setGeometry(QtCore.QRect(520, 190, 112, 41))
        font = QtGui.QFont()
        self.square_root.setFont(font)
        self.square_root.setObjectName(_fromUtf8("square_root"))
        self.power_square = QtGui.QPushButton(self.frame)
        self.power_square.setGeometry(QtCore.QRect(520, 130, 112, 41))
        font = QtGui.QFont()
        self.power_square.setFont(font)
        self.power_square.setObjectName(_fromUtf8("power_square"))
        self.ac = QtGui.QPushButton(self.frame)
        self.ac.setGeometry(QtCore.QRect(520, 250, 112, 41))
        font = QtGui.QFont()
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

