from PyQt4 import QtGui
import calculator_ui
import sys
from math import *


class window(calculator_ui.Ui_MainWindow,QtGui.QMainWindow):
	def __init__(self):
		super(window,self).__init__()
		self.setupUi(self)
		self.btn0.clicked.connect(lambda:self.screenvalue('0'))
		self.btn1.clicked.connect(lambda:self.screenvalue('1'))
		self.btn2.clicked.connect(lambda:self.screenvalue('2'))
		self.btn3.clicked.connect(lambda:self.screenvalue('3'))
		self.btn4.clicked.connect(lambda:self.screenvalue('4'))
		self.btn5.clicked.connect(lambda:self.screenvalue('5'))
		self.btn6.clicked.connect(lambda:self.screenvalue('6'))
		self.btn7.clicked.connect(lambda:self.screenvalue('7'))
		self.btn8.clicked.connect(lambda:self.screenvalue('8'))
		self.btn9.clicked.connect(lambda:self.screenvalue('9'))
		self.btndot.clicked.connect(lambda:self.screenvalue('.'))
		self.sin.clicked.connect(lambda:self.screenvalue('sin('))
		self.cos.clicked.connect(lambda:self.screenvalue('cos('))
		self.tan.clicked.connect(lambda:self.screenvalue('tan('))
		self.sin_.clicked.connect(lambda:self.screenvalue('asin('))
		self.cos_.clicked.connect(lambda:self.screenvalue('acos('))
		self.tan_.clicked.connect(lambda:self.screenvalue('atan('))
		self.power.clicked.connect(lambda:self.screenvalue('**'))
		self.power_square.clicked.connect(lambda:self.screenvalue('**2'))
		self.bracket_opened.clicked.connect(lambda:self.screenvalue('('))
		self.bracket_closed.clicked.connect(lambda:self.screenvalue(')'))
		self.square_root.clicked.connect(lambda:self.screenvalue('sqrt('))
		self.add.clicked.connect(lambda:self.screenvalue('+'))
		self.subtract.clicked.connect(lambda:self.screenvalue('-'))
		self.multiply.clicked.connect(lambda:self.screenvalue('*'))
		self.divide.clicked.connect(lambda:self.screenvalue('/'))
		self.btnpi.clicked.connect(lambda:self.screenvalue('3.14'))
		self.equals.clicked.connect(self.calculations)
		self.ac.clicked.connect(self.lineEdit.clear)
		self.backspace.clicked.connect(self.lineEdit.backspace)

		


	def screenvalue(self,value):
		self.lineEdit.insert(value)



	def calculations(self):
		answer=self.lineEdit.text()	
		try:
			new_answer=eval(answer)
			new_answer1=str(new_answer)
			self.lineEdit.setText(new_answer1)

		except Exception as e: 
			self.lineEdit.setText('SYNTAX ERROR')
app=QtGui.QApplication(sys.argv)
myapplication=window()
myapplication.show()
sys.exit(app.exec_())
