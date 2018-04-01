__author__ = 'faisal21'

import sys
import random
from PyQt4 import QtGui
from PyQt4.QtCore import *
from onebyone1 import Ui_MainWindow




class run1(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.a = 1
        self.ui.pushButton.clicked.connect(self.next)
        self.word = ['saya', 'kamu', 'dia']

    def next(self):
        while (self.a<100):
            try:
                print self.a
                rnd = random.choice(self.word)
                self.ui.label.setText(rnd)
                self.word.remove(rnd)
                print rnd
                return
            except IndexError:
                print "selesai"
                return










if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window1 = run1()
    window1.show()
    sys.exit(app.exec_())

