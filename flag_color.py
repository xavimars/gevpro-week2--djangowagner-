import sys
from PyQt4 import QtGui
from random import randrange

class FlagColor(QtGui.QWidget):
    
    def __init__(self):
        super(FlagColor, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Super mooi")
        
        self.col = QtGui.QColor(0, 0, 0)  
        
        self.col.setRed(100) 
        self.col.setBlue(50)
        self.col.setGreen(150)
        
        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
        self.col.name())
        
        self.show
    
def main():
    app = QtGui.QApplication(sys.argv)
    flag = FlagColor()
    app.exec_()
    
if __name__ == "__main__":
    main()
    