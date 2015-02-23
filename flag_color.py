#!/usr/local/bin/python3

from PyQt4 import QtCore, QtGui
import sys
from random import randrange

class FlagColor(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Flag Color')
        self.initUI()
    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)

        # White background
        paint.setBrush(QtCore.Qt.white)
        paint.drawRect(event.rect())
        
        paint.end()
        
    def initUI(self):

        
        self.col = QtGui.QColor(0, 0, 0)  
        
        
        combo = QtGui.QComboBox(self)
        
        infile = open("countries_list.txt","r")
        for i in infile:
            combo.addItem(i)
        combo.move(100,50)
        combo.activated[str].connect(self.setColor) 
        
        
        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150, 100, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        
        self.show()
        
    def setColor(self, pressed):
        source = self.sender()
        
        
        val, val1, val2 = randrange(0,255), randrange(0,255), randrange(0,255)
        
                        
        
        self.col.setRed(val)
        self.col.setBlue(val1)
        self.col.setGreen(val2)
            
        self.square.setStyleSheet("QFrame { background-color: %s }" %
                    self.col.name())
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    flag = FlagColor()
    
    app.exec_()
