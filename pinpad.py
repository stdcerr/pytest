import sys
from PyQt4.QtGui import QPushButton, QMainWindow, QApplication
################################################################
def main():
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())

################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #create stuff
        self.btn = QPushButton()


        
################################################################

if __name__ == "__main__":

    main()
