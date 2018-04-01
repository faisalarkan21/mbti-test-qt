__author__ = 'faisal21'

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from soal1backupjadi import  Ui_MainWindow
from Tkinter import *

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




    def backIntusi(self):
        self.intuisi = 0
        self.subIntuisi1= 0
        self.subIntuisi2 = 0
        self.subIntuisi3 = 0
    def backSense(self):
        self.sense = 0
        self.subSense1 = 0
        self.subSense2 = 0
        self.subSense3 = 0
    def backExstro(self):
        self.Exstro = 0
        self.subExstro1 = 0
        self.subExstro2 = 0
        self.subExstro3 = 0
    def backIntro(self):
        self.Intro = 0
        self.subIntro1 = 0
        self.subIntro2 = 0
        self.subIntro3 = 0
        self.subIntro4 = 0
    def backJudg(self):
        self.Judg = 0
        self.subJudg1 = 0
        self.subJudg2 = 0
        self.subJudg2 = 0
    def backPercep(self):
        self.Percep =0
        self.subPercep1 = 0
        self.subPercep2 = 0
        self.subPercep3 = 0
    def backThink(self):
        self.Think = 0
        self.subThink1 = 0
        self.subThink2 = 0
        self.subThink3 = 0
    def backFeel(self):
        self.Feel = 0
        self.subFeel1 = 0
        self.subFeel2 = 0
        self.subFeel3 = 0


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

