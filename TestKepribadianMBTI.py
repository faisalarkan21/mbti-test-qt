__author__ = 'faisal21'

import sys
from PyQt4 import QtGui
from PyQt4.QtCore import *
from menuUtama import  Ui_Dialog

from menuUtama1 import Ui_Dialog
from coba1 import *


class tesMbti(QtGui.QMainWindow):
    def __init__(self,parent =None):
        QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.clicked.connect(self.mulaiTest)
        self.ui.pushButton_2.clicked.connect(self.check)
        self.ui.pushButton_3.clicked.connect(self.keluar)
        self.ui.label_3.raise_()
        self.ui.label_4.lower()
        self.ui.pushButton_3.raise_()
        self.setWindowTitle("Program Tes Kepribadian MBTI")
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        self.ui.pushButton_2.setEnabled(False)



    def check(self):
        MyDialog5.jumlah = 0
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(False)


    def mulaiTest (self):

        self.window2 = soal1JP1(self)
        self.window2.exec_()
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)

    def keluar (self):
        self.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window1 = tesMbti()
    window1.show()


    sys.exit(app.exec_())

