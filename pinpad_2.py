import sys
from PyQt4.QtGui import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout,QLabel,QSpacerItem
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import pyqtSlot,QSize
from PyQt4 import QtGui, QtCore
_encoding = QtGui.QApplication.UnicodeUTF8
#Defines for "special" buttons
SAV = 10
ZERO = 11
DEL = 12

class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Pinpad example'
        self.left = 10
        self.top = 10
        self.width = 1280
        self.height = 720
        self.pin = ""
        self.pincaption = "Pin: "
        self.initUI()
        self.loadCSS()

    def loadCSS(self):
        stylesheet = \
            ".QPushButton {\n" \
            + "border: 1px solid black;\n" \
            + "border-radius: 0px;\n" \
            + "color: #000;\n"\
            + "background-color: #fff;\n" \
            + "}" 
        self.setStyleSheet(stylesheet)

    def redBtnCSS(self, btn):
        stylesheet = \
            ".QPushButton {\n" \
            + "background-color: #f00;\n" \
            + "}" 
        btn.setStyleSheet(stylesheet)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        windowLayout = QVBoxLayout()
        self.createHorizontalBtns(windowLayout)
        self.setLayout(windowLayout)
        
        self.show()
    
    def createHorizontalBtns(self,winlay):
        hspacer = QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        vlayout = QVBoxLayout()
        lablay = QHBoxLayout()
        self.pinlab = QLabel(self.pincaption)
        lablay.addWidget(self.pinlab)
        vlayout.addItem(hspacer)
        vlayout.addLayout(lablay)
        h1layout = QHBoxLayout()
        
        for i in range(1,4):
            self.addButton( i, h1layout)
        
        vlayout.addLayout(h1layout)
        h2layout = QHBoxLayout()
        
        for i in range(4,7):
            self.addButton( i, h2layout)
        
        vlayout.addLayout(h2layout)
        h3layout = QHBoxLayout()
        
        for i in range(7,10):
            self.addButton( i, h3layout)
        
        vlayout.addLayout(h3layout)
        h4layout = QHBoxLayout()
        for i in range(10,13):
            self.addButton( i, h4layout)
        
        vlayout.addLayout(h4layout)
        winlay.addLayout(vlayout)

    def addButton(self, digit, lay):
        if digit > 9:
            #Add exceptions for Save, DEL & 0 buttons
            self.addSpecialButton(digit,lay)
        else:
            btn = QPushButton(str(digit), self)
            btn.clicked.connect(lambda: self.onClick(digit))
            lay.addWidget(btn)
            btn.setSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
            btn.setMinimumSize(QSize(100,80))

    def addSpecialButton(self, digit,lay):
        if digit == SAV:
            btn = QPushButton("Save", self)
            btn.clicked.connect(lambda: self.onClick(digit))
            lay.addWidget(btn)
        elif digit == ZERO:
            btn = QPushButton('0', self)
            btn.clicked.connect(lambda: self.onClick(0))
            lay.addWidget(btn)
        elif digit == DEL:
            btn = QPushButton("DEL", self)
            btn.clicked.connect(lambda: self.onClick(digit))
            lay.addWidget(btn)
            self.redBtnCSS(btn)
        btn.setSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        btn.setMinimumSize(QSize(100,100))
    
    @pyqtSlot()
    def onClick(self,val):
        if val == DEL:
            disp = self.pinlab.text()
            if len(disp)> len(self.pincaption):
                self.pinlab.setText(disp[:-1])
                self.pin = self.pin[:-1]
        elif val == SAV:
            self.pinlab.setText(self.pin)
        else:
            self.pinlab.setText(self.pinlab.text() + '*')
            self.pin = self.pin + str(val)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
