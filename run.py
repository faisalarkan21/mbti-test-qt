__author__ = 'faisal21'

import sys
from PyQt4 import QtGui
from PyQt4.QtCore import *
from onebyone1 import  Ui_MainWindow



class run1(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)






if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window1 = run1()
    window1.show()
    sys.exit(app.exec_())

