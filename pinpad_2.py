import sys
from PyQt4.QtGui import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import pyqtSlot,QSize
from PyQt4 import QtGui

#Defines for "special" buttons
SAV = 10
ZERO = 11
DEL = 12

class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createHorizontalBtns()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        
        self.show()
    
    def createHorizontalBtns(self):
        self.horizontalGroupBox = QGroupBox("Pinpad")
        vlayout = QVBoxLayout()
        h1layout = QHBoxLayout()
        
        for i in range(1,4):
            self.button_add( i, h1layout)
        
        vlayout.addLayout(h1layout)
        h2layout = QHBoxLayout()
        
        for i in range(4,7):
            self.button_add( i, h2layout)
        
        vlayout.addLayout(h2layout)
        h3layout = QHBoxLayout()
        
        for i in range(7,10):
            self.button_add( i, h3layout)
        
        vlayout.addLayout(h3layout)
        h4layout = QHBoxLayout()
        for i in range(10,13):
            self.button_add( i, h4layout)
        #btn1 = QPushButton('Save', self)
        #btn1.clicked.connect(lambda: self.on_click('SAV'))
        #h4layout.addWidget(btn1)
        #
        #btn2 = QPushButton('0', self)
        #btn2.clicked.connect(lambda: self.on_click(0))
        #h4layout.addWidget(btn2)
        #
        #btn3 = QPushButton('DEL', self)
        #btn3.clicked.connect(lambda: self.on_click('DEL'))
        #h4layout.addWidget(btn3)
        
        vlayout.addLayout(h4layout)
        self.horizontalGroupBox.setLayout(vlayout)

    def button_add(self, digit, lay):
        if digit > 9:
            #Add exceptions for Save, DEL & 0 buttons
            self.special_btn_add(digit,lay)
        else:
            btn = QPushButton(str(digit), self)
            btn.clicked.connect(lambda: self.on_click(digit))
            lay.addWidget(btn)
            btn.setSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
            btn.setMinimumSize(QSize(30,30))

    def special_btn_add(self, digit,lay):
        if digit == SAV:
            btn = QPushButton("Save", self)
            btn.clicked.connect(lambda: self.on_click(digit))
            lay.addWidget(btn)
        elif digit == ZERO:
            btn = QPushButton('0', self)
            btn.clicked.connect(lambda: self.on_click(0))
            lay.addWidget(btn)
        elif digit == DEL:
            btn = QPushButton("DEL", self)
            btn.clicked.connect(lambda: self.on_click(digit))
            lay.addWidget(btn)
        btn.setSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
        btn.setMinimumSize(QSize(30,30))
    
    @pyqtSlot()
    def on_click(self,val):
        print(val)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
