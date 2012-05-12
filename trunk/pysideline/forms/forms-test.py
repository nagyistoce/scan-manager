import sys
import os
from pysideline import *
from base import *
from PySide import QtGui
from PySide import QtCore
from PySide.QtCore import Qt
import resources

from pysideline.forms import Form,LineEdit,TextEdit,ComboBox,SpinBox,Slider,GroupBox,TableView,Column,DoubleSpinBox,TabbedForm,Tab,TableAction

#MyForm = Form(name='main',contents=[
MyForm = TabbedForm(name='main',documentMode=True,contents=[
	Tab(name='tab1',label='Tab 1',contents=[
		LineEdit(name='f1',label='Field 1 [f1]:',default='default_value'),
		LineEdit(name='f2',label='Field 2 (int) [f2]:',default=2,type=int),
		ComboBox(name='f3',label='Combo [f3]:',default=2,type=int,options=[(1,'test 1'),(2,'test 2'),(3,'test 3')]),
		ComboBox(name='f4',label='Combo [f4]:',default=2,type=str,depends=['options=f3.currentIndexChanged'],
				 options=lambda f:[('%d'%(f.f3.getValue() or 0),'test %d.%d'%((f.f3.getValue() or 0),i)) for i in [5,6,7,8,9]]
		),
		DoubleSpinBox(name='f4.1',label='Field 4.1 [f4.1]:',default=14.1,minimum=10.0,maximum=20.0,singleStep=0.1,decimals=2,prefix='x=',suffix='s'),
		SpinBox(name='f5',label='Field 5 [f5]:',default=4,minimum=0,maximum=100,singleStep=2,prefix='v=',suffix='%'),
		Slider(name='f6',label='Field 6 [f6]:',default=4,minimum=0,maximum=100,tickInterval=10,singleStep=5,tickPosition=QtGui.QSlider.TicksBelow,orientation=Qt.Horizontal),
		GroupBox(name='g1',title='Group 1',groupData=True,contents=[
			LineEdit(name='f7',label='Field g1.1 [f7]:',default='default_value'),
			LineEdit(name='f8',label='Field g1.2 (int) [f8]:',default=2,type=int),
			GroupBox(name='g2',title='Group 1',groupData=True,checkable=True,checked=False,contents=[
				LineEdit(name='f9',label='Field g1.g2.1 [f9]:',default='default_value'),
				LineEdit(name='f10',label='Field g1.g2.2 (int) [f10]:',default=2,type=int),
			]),
		]),
	]),
	Tab(name='tab2',label='Tab 2',contents=[
		TableView(name='t1',tableActions=TableAction.All,
			editForm=Form(name='tableEdit',contents=[
				LineEdit(name='label',label='Label:',type=unicode),
				LineEdit(name='percentage',label='Percentage:',type=int),
			]),
			columns=[
				Column(name='label',label='Label'),
				Column(name='percentage',label='Percentage'),
			],
		),
		TableView(name='t2',tableActions=TableAction.All,
			columns=[
				Column(name='label',label='Label',editable=True,editor=LineEdit(name='labelEditor')),
				Column(name='percentage',label='Percentage',editable=True,resizeMode=QtGui.QHeaderView.Stretch,editor=
					SpinBox(name='percentageEditor',default=4,minimum=0,maximum=100,singleStep=2,prefix='v=',suffix='%')
				),
			],
		),
	]),
])
class App(Application):
	
	class MainWindow(BaseWidget,QtGui.QMainWindow):
		def init(self):
			self.setWindowTitle(self.tr('pysideline.forms test application'))
			self.setCentralWidget(self.MainWidget)
			self.show()

		class MainWidget(BaseWidget,QtGui.QWidget):
			
			class Layout(BaseLayout,QtGui.QVBoxLayout):
				def init(self):
					self.setContentsMargins(0,0,0,0)
					self._up.setLayout(self)
					
			class FormWidget(BaseWidget,QtGui.QWidget):
				class Layout(BaseLayout,QtGui.QVBoxLayout):
					def init(self):
						self.setContentsMargins(0,0,0,0)
						self._up.setLayout(self)
						
				def init(self):
					self._up.Layout.addWidget(self)
					
					self.app.myForm = MyForm(None)
					self.form = self.app.myForm.create(self)
					self.Layout.addWidget(self.form)
					
			class OKButton(BaseWidget,QtGui.QPushButton):
				def init(self):
					self._up.Layout.addWidget(self)
					self.setText('OK')
				def onclicked(self):
					print self.app.myForm.getValue()._pp()
				
app = App(sys.argv)
app.exec_()


