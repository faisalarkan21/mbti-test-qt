__author__ = 'faisal21'

import sys
import random
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import *
from formUtama import Ui_MainWindow
from onebyone1 import Ui_MainWindow1


choice=[]


################################################################
################################################################
################################################################
################################################################
################################################################
#======================== PART 1 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################


################################################################
#################### DIFFERENT CLASS 1 ###########################
################################################################

class soal1JP1(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal1JP1, self).__init__(parent)
        self.resize(786, 346)
        font = QtGui.QFont()
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Anda adalah tipe seseorang yang ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Terencana, Terstruktur dan memiliki deadline yang jelas ")
        self.radioButton_2.setText("Spontan, Fleksibel, tidak diikat waktu ")
        self.soal1_2.setText("Hal 1")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self._want_to_close = False

    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal1JP1, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal2IntroEx1()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Judg")
              dialog2 =  soal2IntroEx1()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Percep")
             dialog2 =  soal2IntroEx1()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 1 ###########################
################################################################

class soal2IntroEx1(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal2IntroEx1, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya lebih suka memiliki hubungan yang ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Mendalam dengan hanya beberapa orang ")
        self.radioButton_2.setText("Luas dengan banyak orang yang berbeda - beda ")
        self.soal1_2.setText("Hal 2")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal2IntroEx1, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal3TF1()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal1JP1()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Intro")
              dialog3 =  soal3TF1()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Extro")
             dialog3 =  soal3TF1()
             dialog3.exec_()



################################################################
#################### DIFFERENT CLASS 1 ###########################
################################################################

class soal3TF1(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal3TF1, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Ketika kesal terhadap seseorang anda lebih suka ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Mengkritik langsung kepada orang tersebut ")
        self.radioButton_2.setText("Menyimpannya dalam hati saja dan bersabar ")
        self.soal1_2.setText("Hal 3")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal3TF1, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal4SenInt1()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal2IntroEx1()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Think")
              dialog3 =  soal4SenInt1()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Feel")
             dialog3 =  soal4SenInt1()
             dialog3.exec_()

################################################################
#################### DIFFERENT CLASS 1 ###########################
################################################################

class soal4SenInt1 (QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal4SenInt1, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya lebih suka memiliki hubungan yang ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.soal1.setText("Saat melakukan sesuatu lebih suka melakukanya dengan ?")
        self.radioButton.setText("Cara anda sendiri tanpa pengaruh dari orang lain")
        self.radioButton_2.setText("Mengikuti orang lain biasa lakukan")
        self.pushButton.setText("    Selanjutnya")
        self.soal1_2.setText("Hal 4")
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal4SenInt1, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):

        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog5 = soal5JP2()
            dialog5.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")




    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal3TF1()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Int")
              dialog5 =  soal5JP2()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Sense")
             dialog5 = soal5JP2()
             dialog5.exec_()


################################################################
################################################################
################################################################
################################################################
################################################################
#======================== PART 2 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################


################################################################
#################### DIFFERENT CLASS 2 ###########################
################################################################


class soal5JP2(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal5JP2, self).__init__(parent)
        self.resize(786, 346)
        font = QtGui.QFont()
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Membuat jadwal dalam melakukan sesuatu membuat anda  ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Jadwal terkesan sangat mengikat dan membebani ")
        self.radioButton_2.setText("Sangat berguna agar berjalan semua sesuai rencana ")
        self.soal1_2.setText("Hal 5")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal5JP2, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")
    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal6IntroEx2()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal4SenInt1()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Percep")
              dialog2 =  soal6IntroEx2()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Judg")
             dialog2 =  soal6IntroEx2()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 2 ###########################
################################################################

class soal6IntroEx2(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal6IntroEx2, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saat hari libur anda lebih suka ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Pergi dengan teman - teman ke suatu tempat")
        self.radioButton_2.setText("Beraktifitas dirumah dan menikmati ketenangan")
        self.soal1_2.setText("Hal 6")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal6IntroEx2, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")
    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal6IntroEx2()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal5JP2()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Extro")
              dialog3 =  soal7SenInt2()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Intro")
             dialog3 =  soal7SenInt2()
             dialog3.exec_()


################################################################
#################### DIFFERENT CLASS 2 ###########################
################################################################

class soal7SenInt2(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal7SenInt2, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Anda lebih suka seseorang dengan sifat ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Seseorang yang selalu berfikir realistis")
        self.radioButton_2.setText("Seseorang yang imajinatif")
        self.soal1_2.setText("Hal 7")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal7SenInt2, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")
    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal8IntroEx3()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal6IntroEx2()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Sense")
              dialog3 =  soal8IntroEx3()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Int")
             dialog3 =  soal8IntroEx3()
             dialog3.exec_()

################################################################
#################### DIFFERENT CLASS 2 ###########################
################################################################

class soal8IntroEx3(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal8IntroEx3, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Anda adalah seseorang yang ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Sosialis, terbuka dan ekspesif")
        self.radioButton_2.setText("Tertutup dan mandiri")
        self.soal1_2.setText("Hal 8")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal8IntroEx3, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")
    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal9JP3()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal7SenInt2()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Extro")
              dialog5 =  soal9JP3()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Intro")
             dialog5 =  soal9JP3()
             dialog5.exec_()


################################################################
################################################################
################################################################
################################################################
################################################################
#======================== PART 3 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################


################################################################
#################### DIFFERENT CLASS 3 ###########################
################################################################


class soal9JP3(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal9JP3, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Ketika sesuatu tidak berjalan sesuai dengan prediksi anda ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Merubah rencana untuk beradaptasi dengan keadaan ")
        self.radioButton_2.setText("Tetap fokus pada target dan mengabaikan perubahan")
        self.soal1_2.setText("Hal 9")
        self.pushButton_2.setText("Sebelumnya ")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal9JP3, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")
    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal6IntroEx2()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal8IntroEx3()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Percep")
              dialog2 =  soal10TF2()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Judg")
             dialog2 =  soal10TF2()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 3 ###########################
################################################################

class soal10TF2(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal10TF2, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Jika sesorang meminta pendapat, anda akan  ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Berbohong untuk menyenangkan hatinya ")
        self.radioButton_2.setText("Mengatakan dengan jujur tanpa memperdulikan perasaanya")
        self.soal1_2.setText("Hal 10")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal10TF2, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal9JP3()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal9JP3()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Feel")
              dialog3 =  soal11SenInt3()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Think")
             dialog3 =  soal11SenInt3()
             dialog3.exec_()


################################################################
#################### DIFFERENT CLASS 3 ###########################
################################################################

class soal11SenInt3(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal11SenInt3, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Jika anda sedang di hutan atau taman, anda akan ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Lebih mudah mendapatkan inspirasi dan ide - ide baru")
        self.radioButton_2.setText("Merasakan indah dan sejuknya pepohonan disekitar anda ")
        self.soal1_2.setText("Hal 11")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal11SenInt3, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal12TF3()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal10TF2()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Int")
              dialog3 =  soal12TF3()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Sense")
             dialog3 =  soal12TF3()
             dialog3.exec_()

################################################################
#################### DIFFERENT CLASS 3 ###########################
################################################################

class soal12TF3(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal12TF3, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Jika anda mengambil keputusan anda akan berdasar pada ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Berdasar logika dan peraturan yang sudah ditentukan")
        self.radioButton_2.setText("Berdasar pada perasaan pribadi dan kondisi orang lain")
        self.soal1_2.setText("Hal 12")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal12TF3, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal13SenInt4()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal11SenInt3()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Think")
              dialog5 =  soal13SenInt4()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Feel")
             dialog5 =  soal13SenInt4()
             dialog5.exec_()








########################################################################################################################






################################################################
################################################################
################################################################
################################################################
################################################################
#======================== PART 4 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################



################################################################
#################### DIFFERENT CLASS 4 ###########################
###############################################################


class soal13SenInt4(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal13SenInt4, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Anda adalah tipe orang yang selalu berfokus pada ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Masa kini (apa yang bisa diperbaiki sekarang)")
        self.radioButton_2.setText("Masa depan (apa yang mungkin dicapai di masa depan) ")  #########################
        self.soal1_2.setText("Hal 13")
        self.pushButton_2.setText("Sebelumnya ")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal13SenInt4, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal6IntroEx2()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal12TF3()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Sense")
              dialog2 =  soal14JP4()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Int")
             dialog2 =  soal14JP4()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 4 ###########################
################################################################

class soal14JP4(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal14JP4, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Bagaimana sikap anda terhadap sebuah deadline ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Serius terhadap deadline agar tepat pada rencana")
        self.radioButton_2.setText("Deadline adalah sesuatu yang sangat fleksibel bagi saya")
        self.soal1_2.setText("Hal 14")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal14JP4, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal6IntroEx2()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal13SenInt4()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Judg")
              dialog3 =  soal15SenInt5()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Percep")
             dialog3 =  soal15SenInt5()
             dialog3.exec_()


################################################################
#################### DIFFERENT CLASS 4 #########################
################################################################

class soal15SenInt5(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal15SenInt5, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya lebih pecaya pada ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Saya percaya inspirasi, wawasan, ide dan firasat")
        self.radioButton_2.setText("Saya percaya fakta, contoh-contoh konkret dan bukti")
        self.soal1_2.setText("Hal 15")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal15SenInt5, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal16IntroEx4()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal14JP4()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Int")
              dialog3 =  soal16IntroEx4()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Sense")
             dialog3 =  soal16IntroEx4()
             dialog3.exec_()

################################################################
#################### DIFFERENT CLASS 4 #########################
################################################################

class soal16IntroEx4(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal16IntroEx4, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya lebih suka ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Berorientasi pada dunia internal (memori, pemikiran, ide)")
        self.radioButton_2.setText("Berorientasi pada dunia eksternal (kegiatan, orang)")
        self.soal1_2.setText("Hal 16")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal16IntroEx4, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal17TF4()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal15SenInt5()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Intro")
              dialog5 =  soal17TF4()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Extro")
             dialog5 =  soal17TF4()
             dialog5.exec_()


################################################################
################################################################
################################################################
################################################################
################################################################
#======================== PART 5 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################


class soal17TF4(QtGui.QDialog):################################################
    def __init__(self, parent=None):
        super(soal17TF4, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya akan mempercayai perasaan atau feeling saya jika ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Logis atau tidak, saya tetap akan percaya pada feeling saya")
        self.radioButton_2.setText("Hanya jika perasaan atau feeling itu logis atau masuk akal")
        self.soal1_2.setText("Hal 17")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal17TF4, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal18JP5()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal16IntroEx4()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Feel")
              dialog2 =  soal18JP5()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Think")
             dialog2 =  soal18JP5()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 5 ###########################
################################################################

class soal18JP5(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal18JP5, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Anda akan lebih memilih ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Kontinuitas dan stabilitas lebih diutamakan ")
        self.radioButton_2.setText("Perubahan dan variasi lebih diutamakan")
        self.soal1_2.setText("Hal 18")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal18JP5, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal19IntroEx5()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal17TF4()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Judg")
              dialog3 =  soal19IntroEx5()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Percep")
             dialog3 =  soal19IntroEx5()
             dialog3.exec_()


################################################################
#################### DIFFERENT CLASS 5 ###########################
################################################################

class soal19IntroEx5(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal19IntroEx5, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Anda adalah seseorang yang ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Sangat suka dengan keramaian")
        self.radioButton_2.setText("Sangat menyukai tempat yang tenang ")
        self.soal1_2.setText("Hal 19")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal19IntroEx5, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal20TF5()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal18JP5()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append(("Extro"))
              dialog3 =  soal20TF5()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Intro")
             dialog3 =  soal20TF5()
             dialog3.exec_()

################################################################
#################### DIFFERENT CLASS 5 ###########################
################################################################

class soal20TF5(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal20TF5, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Menurut pendapat orang lain saya ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Sering dianggap keras kepala")
        self.radioButton_2.setText("Sering dianggap terlalu memihak")
        self.soal1_2.setText("Hal 20")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal20TF5, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = MyDialog5()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal19IntroEx5()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Think")
              dialog5 =  soal21SenInt6()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Feel")
             dialog5 =  soal21SenInt6()
             dialog5.exec_()



########################################################################################################################
#################################CONSTRUCTION##########################################################################





################################################################
################################################################
################################################################
################################################################
################################################################
#======================== PART 6 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################






################################################################
#################### DIFFERENT CLASS 6 #########################
################################################################

class soal21SenInt6 (QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal21SenInt6, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Dalam soal keahlian, anda adalah tipe orang ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Menggunakan keterampilan yang sudah dikuasai")
        self.radioButton_2.setText("Menyukai tantangan untuk menguasai keterampilan baru")
        self.pushButton.setText("Selanjutnya")

        self.soal1_2.setText("Hal 21")
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal21SenInt6, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):

        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog5 = soal22TF6()
            dialog5.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal20TF5()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Sense")
              dialog5 =  soal22TF6()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Int")
             dialog5 = soal22TF6()
             dialog5.exec_()


################################################################
#################### DIFFERENT CLASS 6 #########################
################################################################


class soal22TF6(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal22TF6, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Ketika teman dalam masalah, apa reaksi pertama anda ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Menanyakan tentang penyebab masalahnya ")
        self.radioButton_2.setText("Langsung membantu, tanpa bertanya ")
        self.soal1_2.setText("Hal 22")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal22TF6, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal23IntroEx6()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal21SenInt6()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Think")
              dialog2 =  soal23IntroEx6()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Feel")
             dialog2 =  soal23IntroEx6()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 6 ###########################
################################################################
#!

class soal23IntroEx6(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal23IntroEx6, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saat dihadapkan dalam suatu pilihan, anda akan?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Berpikir secara matang sebelum bertindak")
        self.radioButton_2.setText("Berani bertindak tanpa terlalu lama berfikir")
        self.soal1_2.setText("Hal 23")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal23IntroEx6, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal24JP6()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal22TF6()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Intro")
              dialog3 =  soal24JP6()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Extro")
             dialog3 =  soal24JP6()
             dialog3.exec_()


################################################################
#################### DIFFERENT CLASS 6 ##########################
################################################################

class soal24JP6(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal24JP6, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Anda seorang pemimpin tim project, untuk capai tujuan anda akan ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Membiarkan orang lain bertindak bebas asalkan tujuan tercapai")
        self.radioButton_2.setText("Mengatur orang lain dengan tata tertib agar tujuan tercapai")
        self.soal1_2.setText("Hal 24")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal24JP6, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal25IntroEx7()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal23IntroEx6()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Percep")
              dialog3 =  soal25IntroEx7()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Judg")
             dialog3 =  soal25IntroEx7()
             dialog3.exec_()


    ################################################################
    ################################################################
    ################################################################
    ################################################################
    ################################################################
    #======================== PART 7 ==============================#
    ################################################################
    ################################################################
    ################################################################
    ################################################################
    ################################################################




################################################################
#################### DIFFERENT CLASS 7 ###########################
################################################################

class soal25IntroEx7(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal25IntroEx7, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saat ingin berkomunikasi dengan seseorang anda akan ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Lebih suka komunikasi tidak langsung (telp, surat, e-mail)")
        self.radioButton_2.setText("Lebih suka komunikasi langsung (tatap muka)")
        self.soal1_2.setText("Hal 25")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal25IntroEx7, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal26TF7()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal24JP6()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Intro")
              dialog5 =  soal26TF7()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Extro")
             dialog5 =  soal26TF7()
             dialog5.exec_()


################################################################
#################### DIFFERENT CLASS 7 ###########################
################################################################


class soal26TF7(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal26TF7, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Anda adalah seorang ketua disuatu organisasi, anda lebih mementingkan ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Untuk selalu menjaga agar situasi harmonis tetap terjaga")
        self.radioButton_2.setText("Untuk menjaga agar tujuan organisasi selalu tercapai")
        self.soal1_2.setText("Hal 26")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal26TF7, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal27SenInt7()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal25IntroEx7()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Feel")
              dialog2 =  soal27SenInt7()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Think")
             dialog2 =  soal27SenInt7()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 7 ###########################
################################################################


class soal27SenInt7(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal27SenInt7, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Jika anda diharuskan mengambil keputusan, anda akan ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("menarik kesimpulan dengan cepat sesuai naluri")
        self.radioButton_2.setText("Menarik kesimpulan dengan lama dan hati-hati")
        self.soal1_2.setText("Hal 27")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal27SenInt7, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal28JP7()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal26TF7()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Int")
              dialog3 =  soal28JP7()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Sense")
             dialog3 =  soal28JP7()
             dialog3.exec_()


################################################################
#################### DIFFERENT CLASS 7 ###########################
################################################################
###
#######!!!!

class soal28JP7(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal28JP7, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Anda tipe seseorang yang  ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Puas ketika mampu beradaptasi dengan momentum yang terjadi")
        self.radioButton_2.setText("Puas ketika mampu menjalankan semuanya sesuai rencana")
        self.soal1_2.setText("Hal 28")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal28JP7, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal29TF8()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal27SenInt7()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Percep")
              dialog3 =  soal29TF8()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Judg")
             dialog3 =  soal29TF8()
             dialog3.exec_()




################################################################
################################################################
################################################################
################################################################
################################################################
# ======================== PART 8 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################


################################################################
#################### DIFFERENT CLASS 8 ###########################
################################################################

class soal29TF8(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal29TF8, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Jika dituntut profesional, manakah yang lebih penting ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Perasaan manusia lebih penting dari sekadar standar")
        self.radioButton_2.setText("Standar harus di atas segalanya ")
        self.soal1_2.setText("Hal 29")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal29TF8, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal30JP8()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal28JP7()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Feel")
              dialog5 =  soal30JP8()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Think")
             dialog5 =  soal30JP8()
             dialog5.exec_()


             ################################################################
             #################### DIFFERENT CLASS 8 ###########################
             ################################################################


class soal30JP8 (QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal30JP8, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Anda adalah tipe orang yang selalu berfokus pada ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Tidak menyukai hal-hal yang bersifat mendadak dan di luar perencanaan")
        self.radioButton_2.setText("Perubahan mendadak tidak jadi masalah")
        self.soal1_2.setText("Hal 30")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal30JP8, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal31IntroEx8()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal29TF8()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Judg")
              dialog2 =  soal31IntroEx8()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Percep")
             dialog2 =  soal31IntroEx8()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 8 ###########################
################################################################


class soal31IntroEx8 (QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal31IntroEx8, self).__init__(parent)
        self.resize(786, 346)
        font = QtGui.QFont()
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Dalam keadaan hanya berdua dengan seseorang anda akan ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Lebih banyak mendengarkan pembicaraan dari dia")
        self.radioButton_2.setText("Anda yang lebih banyak berbicara ")
        self.soal1_2.setText("Hal 31")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal31IntroEx8, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal32SenInt8()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal30JP8()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Intro")
              dialog3 =  soal32SenInt8()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Extro")
             dialog3 =  soal32SenInt8()
             dialog3.exec_()

################################################################
#################### DIFFERENT CLASS 8 ###########################
################################################################


class soal32SenInt8(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal32SenInt8, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya selalu memikirkan tentang ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Pekerjaan atau tugas apa yang harus saya lakukan selanjutnya")
        self.radioButton_2.setText("Makna tersembunyi dibalik suatu kejadian")
        self.soal1_2.setText("Hal 32")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal32SenInt8, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal33JP9()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal31IntroEx8()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Sense")
              dialog3 =  soal33JP9()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Int")
             dialog3 =  soal33JP9()
             dialog3.exec_()





################################################################
################################################################
################################################################
################################################################
################################################################
# ======================== PART 9 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################


################################################################
#################### DIFFERENT CLASS 9 #########################
################################################################

class soal33JP9(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal33JP9, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Pada saat mengerjakan suatu tugas anda selalu ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Menyelesaikan pekerjaan dengan secepatnya")
        self.radioButton_2.setText("Terkadang sering menunda pekerjaan")
        self.soal1_2.setText("Hal 33")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal33JP9, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal34SenInt9()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal32SenInt8()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Judg")
              dialog5 =  soal34SenInt9()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Percep")
             dialog5 =  soal34SenInt9()
             dialog5.exec_()

################################################################
#################### DIFFERENT CLASS 9 ###########################
################################################################


class soal34SenInt9 (QtGui.QDialog):################################################
    def __init__(self, parent=None):
        super(soal34SenInt9, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Teman saya menggambarkan saya sebagai orang yang ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Realistis dan melakukan suatu hal yang perlu dilakukan  ")
        self.radioButton_2.setText("Imajinatif selalu memikirkan tentang ide - ide yang abstrak")
        self.soal1_2.setText("Hal 34")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal34SenInt9, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal35TF9()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal33JP9()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Sense")
              dialog2 =  soal35TF9()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Int")
             dialog2 =  soal35TF9()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 9 ###########################
################################################################

class soal35TF9(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal35TF9, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya adalah orang yang ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Berhati lembut")
        self.radioButton_2.setText("Berfikiran Kuat")
        self.soal1_2.setText("Hal 35")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal35TF9, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal36IntroEx9()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal34SenInt9()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Feel")
              dialog3 =  soal36IntroEx9()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Think")
             dialog3 =  soal36IntroEx9()
             dialog3.exec_()


################################################################
#################### DIFFERENT CLASS 9 ###########################
################################################################

class soal36IntroEx9(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal36IntroEx9, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya adalah orang yang ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Membutuhkan waktu untuk bisa berteman ")
        self.radioButton_2.setText("Dapat dengan mudah untuk berteman")
        self.soal1_2.setText("Hal 36")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal36IntroEx9, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal20TF5()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal35TF9()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append(("Intro"))
              dialog3 =  soal37SenInt10()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Extro")
             dialog3 =  soal37SenInt10()
             dialog3.exec_()






################################################################
################################################################
################################################################
################################################################
################################################################
# ======================== PART 10 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################


################################################################
#################### DIFFERENT CLASS 10 ###########################
################################################################

class soal37SenInt10(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal37SenInt10, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya lebih suka menjelaskan sesuatu dengan ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Kata - kata kiasan atau dengan kata - kata yang filosofis ")
        self.radioButton_2.setText("kata - kata yang apa adanya, sesuai dengan fakta yang ada")
        self.soal1_2.setText("Hal 37")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal37SenInt10, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal38IntroEx10()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal36IntroEx9()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Int")
              dialog5 =  soal38IntroEx10()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Sense")
             dialog5 =  soal38IntroEx10()
             dialog5.exec_()



################################################################
#################### DIFFERENT CLASS 10 ###########################
################################################################

class soal38IntroEx10 (QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal38IntroEx10, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Disaat liburan lebih suka aktifitas ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("    Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Bersosialisasi dan menambah teman baru")
        self.radioButton_2.setText("Menjalani waktu dengan teman yang saya kenal dengan baik")

        self.soal1_2.setText("Hal 38")
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal38IntroEx10, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):

        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog5 = soal39JP10()
            dialog5.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")




    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal37SenInt10()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Extro")
              dialog5 =  soal39JP10()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Intro")
             dialog5 = soal39JP10()
             dialog5.exec_()


################################################################
#################### DIFFERENT CLASS 10 ###########################
################################################################


class soal39JP10(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal39JP10, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya seringkali mengukur sesuatu dengan ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Perkiraan dan penaksiran yang menurut saya sangat akurat")
        self.radioButton_2.setText("Pengitungan secara yang matematis dengan teliti")
        self.soal1_2.setText("Hal 39")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal39JP10, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal40TF10()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal38IntroEx10()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Percep")
              dialog2 =  soal40TF10()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Judg")
             dialog2 =  soal40TF10()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 10 ###########################
################################################################

class soal40TF10(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal40TF10, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya tipe orang yang lebih menghargai ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Keadilan")
        self.radioButton_2.setText("Kemurahan Hati")
        self.soal1_2.setText("Hal 40")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal40TF10, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal41IntroEx11()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal39JP10()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Think")
              dialog3 =  soal41IntroEx11()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Feel")
             dialog3 =  soal41IntroEx11()
             dialog3.exec_()








################################################################
################################################################
################################################################
################################################################
################################################################
# ======================== PART 11 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################


#######################################################################################################################
############################### PEMBANGUNAN TAHAP AKHIR ###############################################################




################################################################
#################### DIFFERENT CLASS 11 ###########################
################################################################

class soal41IntroEx11(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal41IntroEx11, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya adalah orang yang lebih peduli dengan ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("pikiran dan perasaan saya sendiri")
        self.radioButton_2.setText("dunia di sekitar saya")
        self.soal1_2.setText("Hal 41")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal41IntroEx11, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal42SenInt11()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal40TF10()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Intro")
              dialog5 =  soal42SenInt11()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Extro")
             dialog5 =  soal42SenInt11()
             dialog5.exec_()





################################################################
#################### DIFFERENT CLASS 11 ###########################
################################################################

class soal42SenInt11 (QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal42SenInt11, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya selalu menjalani kehidupan dengan ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Memprediksi keadaan apa yang akan terjadi selanjutnya")
        self.radioButton_2.setText("Fokus situasi saat ini, dan menyelesaikan permasalahanya")

        self.soal1_2.setText("Hal 42")
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal42SenInt11, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):

        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog5 = soal43TF11()
            dialog5.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal41IntroEx11()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Int")
              dialog5 =  soal43TF11()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Sense")
             dialog5 = soal43TF11()
             dialog5.exec_()



################################################################
#################### DIFFERENT CLASS 11 ###########################
################################################################

class soal43TF11(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal43TF11, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya adalah orang yang cepat dalam hal ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Mengkritik kesalahan orang lain")
        self.radioButton_2.setText("Memberi pujian terhadap orang lain")
        self.soal1_2.setText("Hal 43")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal43TF11, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal44JP11()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal42SenInt11()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Think")
              dialog2 =  soal44JP11()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Feel")
             dialog2 =  soal44JP11()
             dialog2.exec_()


################################################################
#################### DIFFERENT CLASS 11 ###########################
################################################################

class soal44JP11(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal44JP11, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Jika harus mengerjakan tugas, saya biasanya ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Bermain dulu baru saya akan belajar")
        self.radioButton_2.setText("Selesaikan semua tugas terlebih dahulu setelah itu bermain")
        self.soal1_2.setText("Hal 44")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal44JP11, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal45TF12()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal43TF11()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Percep")
              dialog3 =  soal45TF12()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Judg")
             dialog3 =  soal45TF12()
             dialog3.exec_()


################################################################
################################################################
################################################################
################################################################
################################################################
# ======================== PART 12 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################

################################################################
#################### DIFFERENT CLASS 12 ###########################
################################################################

class soal45TF12(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal45TF12, self).__init__(parent) #############Samapai sini ################################# SOAL 45
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Ketika anda mengoreksi kesalahan seseorang, saya akan ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Dengan cepat saya akan melakukannya")
        self.radioButton_2.setText("Berfikir ulang, karena takut untuk menyakiti perasaan mereka")
        self.soal1_2.setText("Hal 45")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal45TF12, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal46JP12()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal44JP11()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Think")
              dialog3 =  soal46JP12()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Feel")
             dialog3 =  soal46JP12()
             dialog3.exec_()





################################################################
#################### DIFFERENT CLASS 12 ###########################
################################################################

class soal46JP12(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal46JP12, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Ruang kerja saya biasanya selalu ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Tidak Terorganisir, biasanya agak berantakan")
        self.radioButton_2.setText("Terorganisir, bersih dan sangat rapi")
        self.soal1_2.setText("Hal 46")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal46JP12, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal47IntroEx12()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal45TF12()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Percep")
              dialog5 =  soal47IntroEx12()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Judg")
             dialog5 =  soal47IntroEx12()
             dialog5.exec_()


################################################################
#################### DIFFERENT CLASS 12 ###########################
################################################################


class soal47IntroEx12(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal47IntroEx12, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Ketika di sekitar orang lain saya ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Lebih banyak diam dan lebih memilih menyendiri")
        self.radioButton_2.setText("Langsung memulai pembicaraan dengan orang disekitar saya")
        self.soal1_2.setText("Hal 47")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal47IntroEx12, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal48SenInt12()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal46JP12()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Intro")
              dialog2 =  soal48SenInt12()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Extro")
             dialog2 =  soal48SenInt12()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 12 ###########################
################################################################


class soal48SenInt12(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal48SenInt12, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya selalu tertarik dengan ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Mempelajari fakta - fakta nyata dari suatu kejadian")
        self.radioButton_2.setText("Mempelajari suatu teori - teori yang menarik")
        self.soal1_2.setText("Hal 48")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal48SenInt12, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal49JP13()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal47IntroEx12()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Sense")
              dialog3 =  soal49JP13()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Int")
             dialog3 =  soal49JP13()
             dialog3.exec_()





################################################################
################################################################
################################################################
################################################################
################################################################
# ======================== PART 13 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################
#BEDA PART

################################################################
#################### DIFFERENT CLASS 13 ###########################
################################################################

class soal49JP13(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal49JP13, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya menikmati suatu tugas kekita saya ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Telah selesai mengerjakan semua tugas tersebut")
        self.radioButton_2.setText("Baru mulai mengerjakan tugas - tugas tersebut")
        self.soal1_2.setText("Hal 49")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal49JP13, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal50TF13()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal48SenInt12()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Judg")
              dialog3 =  soal50TF13()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Percep")
             dialog3 =  soal50TF13()
             dialog3.exec_()


################################################################
#################### DIFFERENT CLASS 13 ###########################
################################################################

class soal50TF13(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal50TF13, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya adalah orang yang cendrung lebih ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Mengutamakan Keramahan dan kelumbutan hati")
        self.radioButton_2.setText("Mengutamakan penilaian yang adil terhadap sesuatu")
        self.soal1_2.setText("Hal 50")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal50TF13, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal51SenInt13()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal49JP13()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Feel")
              dialog5 =  soal51SenInt13()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Think")
             dialog5 =  soal51SenInt13()
             dialog5.exec_()


             ################################################################
             #################### DIFFERENT CLASS 13 ###########################
             ################################################################


class soal51SenInt13 (QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal51SenInt13, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya suka menghibur diri saya dengan ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Tentang sesuatu yang menarik dilingkungan disekitar saya")
        self.radioButton_2.setText("Membayangkan sesuatu menghibur dengan imajinasi saya ")
        self.soal1_2.setText("Hal 51")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal51SenInt13, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal52IntroEx13()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        self._want_to_close = True
        choice.pop()
        self.close()
        dialog = soal50TF13()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Sense")
              dialog2 =  soal52IntroEx13()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Int")
             dialog2 =  soal52IntroEx13()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 13 ###########################
################################################################


class soal52IntroEx13 (QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal52IntroEx13, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Jika menjadi pusat perhatian, anda akan merasa ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Anda menjadi merasa sangat bersemangat ")
        self.radioButton_2.setText("Anda menjadi merasa sangat tidak nyaman ")
        self.soal1_2.setText("Hal 52")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal52IntroEx13, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal53IntroEx14()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal51SenInt13()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Extro")
              dialog3 =  soal53IntroEx14()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Intro")
             dialog3 =  soal53IntroEx14()
             dialog3.exec_()






################################################################
################################################################
################################################################
################################################################
################################################################
# ======================== PART 14 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################






################################################################
#################### DIFFERENT CLASS 14 ###########################
################################################################


class soal53IntroEx14(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal53IntroEx14, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya sering kali suka menghabiskan waktu dengan ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Menginstrospeksi diri dengan menyendiri")
        self.radioButton_2.setText("Berinteraksi dan bersosialisasi dengan teman - teman anda")
        self.soal1_2.setText("Hal 53")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal53IntroEx14, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal54TF14()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal52IntroEx13()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Intro")
              dialog3 =  soal54TF14()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Extro")
             dialog3 =  soal54TF14()
             dialog3.exec_()




################################################################
#################### DIFFERENT CLASS 14 ###########################
################################################################

class soal54TF14(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal54TF14, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya lebih menyukai seseorang yang ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Seseorang yang pintar, cerdas dan berbakat")
        self.radioButton_2.setText("Seseorang yang memiliki pribadi yang baik dan hangat ")
        self.soal1_2.setText("Hal 54")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal54TF14, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal55JP14()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal53IntroEx14()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Think")
              dialog5 =  soal55JP14()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Feel")
             dialog5 =  soal55JP14()
             dialog5.exec_()

################################################################
#################### DIFFERENT CLASS 14 ###########################
################################################################

class soal55JP14 (QtGui.QDialog):################################################
    def __init__(self, parent=None):
        super(soal55JP14, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Bagi saya, sangat buruk bagi saya menjadi ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Menjadi seseorang yang bimbang dalam mengambil keputusan")
        self.radioButton_2.setText("Menjadi terlalu kaku dalam menyikapi suatu keputusan")
        self.soal1_2.setText("Hal 55")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal55JP14, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal56SenInt14()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        self._want_to_close = True
        choice.pop()
        self.close()
        dialog = soal54TF14()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Percep")
              dialog2 =  soal56SenInt14()
              dialog2.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Judg")
             dialog2 =  soal56SenInt14()
             dialog2.exec_()

################################################################
#################### DIFFERENT CLASS 14 ###########################
################################################################

#BLUMMMMMMMMM

class soal56SenInt14(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal56SenInt14, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya selalu memikir sesuatu yang bersifat ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Memikirkan sesuatu yang bersifat ide - ide abstrak")
        self.radioButton_2.setText("Memikirkan sesuatu yang pasti dan realistis")
        self.soal1_2.setText("Hal 56")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal56SenInt14, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal57SenInt15()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal55JP14()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Int")
              dialog3 =  soal57SenInt15()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Sense")
             dialog3 =  soal57SenInt15()
             dialog3.exec_()


################################################################
################################################################
################################################################
################################################################
################################################################
# ======================== PART 15 ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################

################################################################
#################### DIFFERENT CLASS 15 ###########################
################################################################ CONSTRUC

class soal57SenInt15(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal57SenInt15, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya merasa bangga pada diri saya saat ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Saat saya merasa telah menjadi sukses")
        self.radioButton_2.setText("Saat saya menyelesaikan daftar target didalam hidup saya"  )
        self.soal1_2.setText("Hal 57")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal57SenInt15, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 =  soal58IntroEx15()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal56SenInt14()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append(("Sense"))
              dialog3 =  soal58IntroEx15()
              dialog3.exec_()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Int")
             dialog3 =  soal58IntroEx15()
             dialog3.exec_()





################################################################
#################### DIFFERENT CLASS 15 ###########################
################################################################

class soal58IntroEx15(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal58IntroEx15, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya lebih sering melibatkan diri pada kegiatan ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Bersifat individual yang menarik bagi saya ")
        self.radioButton_2.setText("Bersifat kelompok dan melibatkan banyak orang ")
        self.soal1_2.setText("Hal 58")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal58IntroEx15, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog2 = soal59TF15()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog3 = soal57SenInt15()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Intro")
              dialog5 =  soal59TF15()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Extro")
             dialog5 =  soal59TF15()
             dialog5.exec_()



################################################################
#################### DIFFERENT CLASS 15 ###########################
################################################################

class soal59TF15 (QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal59TF15, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Anda berhadapan dengan masalah, anda akan fokus kepada ? ")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.setText("Mengkhawatirkan perasaan dan kodisi mental mereka ")
        self.radioButton_2.setText("Fokus di penyelesaian maasalah yang mereka hadapi")

        self.soal1_2.setText("Hal 59")
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self._want_to_close = False
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal59TF15, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")

    def nextButton (self):

        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.close()
            dialog5 = soal60JP15()
            dialog5.exec_()
        else:
            QtGui.QMessageBox.information(self, "Pesan", "Silahkan isi pilihan terlebih dahulu")




    def lastButton(self):
        self._want_to_close = True
        choice.pop()
        self.close()
        dialog3 = soal58IntroEx15()
        dialog3.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Feel")
              dialog5 =  soal60JP15()
              dialog5.exec_()
        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Think")
             dialog5 = soal60JP15()
             dialog5.exec_()


################################################################
#################### DIFFERENT CLASS 15 ###########################
################################################################


class soal60JP15(QtGui.QDialog):
    def __init__(self, parent=None):
        super(soal60JP15, self).__init__(parent)
        self.resize(786, 346)
        self.setFixedHeight(346)
        self.setFixedWidth(786)
        self.setWindowIcon(QtGui.QIcon('programbg.png'))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(False)
        self.soal1 = QtGui.QLabel(self)
        self.soal1.setGeometry(96, 30, 591, 71)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle("")
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353652_basics-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/faisal21/Downloads/1433353645_basics-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowTitle("Tes MBTI")
        self.soal1.setText("Saya lebih suka berfikir secara ?")
        self.groupBox.setTitle("   Pilihan   ")
        self.pushButton.setText("      Selanjutnya")
        self.radioButton.setText("Acak tanpa urutan tata cara berfikir yang pasti")
        self.radioButton_2.setText("Berurut dengan tata urutan befikir yang terstruktur ")
        self.soal1_2.setText("Hal 60")
        self.pushButton_2.setText("Sebelumnya")
        self.radioButton.clicked.connect(self.next)
        self.radioButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.nextButton)
        self.pushButton_2.clicked.connect(self.lastButton)
        self._want_to_close = False

    def closeEvent(self, evnt):
        if self._want_to_close:
            super(soal60JP15, self).closeEvent(evnt)
        else:
            evnt.ignore()
            QtGui.QMessageBox.information(self, "Pesan", "Mohon selesaikan tes terlebih dahulu")




    def nextButton (self):
        if(self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self._want_to_close = True
            self.close()
            dialog2 =  MyDialog5()
            dialog2.exec_()
        else:
            QtGui.QMessageBox.information(self,"Pesan","Silahkan isi pilihan terlebih dahulu")

    def lastButton(self):
        choice.pop()
        self._want_to_close = True
        self.close()
        dialog = soal59TF15()
        dialog.exec_()

    def next(self):
        if (self.radioButton.isChecked()):
              self._want_to_close = True
              self.close()
              choice.append("Percep")
              dialog2 =  MyDialog5()

        elif (self.radioButton_2.isChecked()):
             self._want_to_close = True
             self.close()
             choice.append("Judg")
             dialog2 =  MyDialog5()




















































################################### END CONSTRUCTION ###################################################################
########################################################################################################################





################################################################
################################################################
################################################################
################################################################
################################################################
#================== Calculation ==============================#
################################################################
################################################################
################################################################
################################################################
################################################################



class MyDialog5():
    def __init__(self):


        self.jumlah = choice.__len__()
        self.Exstro = choice.count("Extro")
        self.Intro = choice.count("Intro")
        self.Sense = choice.count("Sense")
        self.Intuisi = choice.count("Int")
        self.Think = choice.count("Think")
        self.Feel = choice.count("Feel")
        self.Judg = choice.count("Judg")
        self.Percep = choice.count("Percep")

        if (self.Intro < self.Exstro):
            self.IorE = "E"
        else :
            self.IorE = "I"

        if (self.Sense < self.Intuisi):
            self.SorI = "N"
        else:
            self.SorI = "S"

        if (self.Think < self.Feel):
            self.TorF = "F"
        else:
            self.TorF = "T"

        if (self.Percep < self.Judg):
            self.PorJ = "J"
        else:
            self.PorJ = "P"

        print "Extro = %i" % self.Exstro
        print "Intro = %i" % self.Intro
        print "Sense = %i" % self.Sense
        print "Intuisi = %i" % self.Intuisi
        print "Think = %i" % self.Think
        print "Feel = %i" % self.Feel
        print "Judg = %i" % self.Judg
        print "Percep = %i" % self.Percep

        if ((self.IorE == "I") and (self.SorI == "N") and (self.TorF == "T") and (self.PorJ == "P")):
            from INTP1 import Ui_Dialog
            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)            
            u.tabWidget.raise_()

            choice[:] = []
            Dialog.exec_()


        elif ((self.IorE == "I") and (self.SorI == "N") and (self.TorF == "T") and (self.PorJ == "J")):
            from INTJ1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
            
            u.tabWidget.raise_()
            choice[:] = []

            Dialog.exec_()
        elif ((self.IorE == "E") and (self.SorI == "N") and (self.TorF == "T") and (self.PorJ == "J")):
            from ENTJ1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
            
            u.tabWidget.raise_()
            choice[:] = []

            Dialog.exec_()
        elif ((self.IorE == "E") and (self.SorI == "N") and (self.TorF == "T") and (self.PorJ == "P")):
            from ENTP1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
            
            u.tabWidget.raise_()
            choice[:] = []
            Dialog.exec_()
        elif ((self.IorE == "I") and (self.SorI == "S") and (self.TorF == "T") and (self.PorJ == "P")):
            from ISTP1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
            
            u.tabWidget.raise_()
            choice[:] = []

            Dialog.exec_()
        elif ((self.IorE == "I") and (self.SorI == "S") and (self.TorF == "T") and (self.PorJ == "J")):
            from ISTJ1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
            
            u.tabWidget.raise_()
            choice[:] = []

            Dialog.exec_()
        elif ((self.IorE == "E") and (self.SorI == "S") and (self.TorF == "T") and (self.PorJ == "P")):
            from ESTP1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
           
            u.tabWidget.raise_()
            choice[:] = []

            Dialog.exec_()
        elif ((self.IorE == "E") and (self.SorI == "S") and (self.TorF == "T") and (self.PorJ == "J")):
            from ESTJ1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
            
            u.tabWidget.raise_()
            choice[:] = []

            Dialog.exec_()
        elif ((self.IorE == "I") and (self.SorI == "S") and (self.TorF == "F") and (self.PorJ == "P")):
            from ISFP1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
           
            u.tabWidget.raise_()

            choice[:] = []
            Dialog.exec_()
        elif ((self.IorE == "I") and (self.SorI == "S") and (self.TorF == "F") and (self.PorJ == "J")):
            from ISFJ1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
          
            u.tabWidget.raise_()

            choice[:] = []
            Dialog.exec_()
        elif ((self.IorE == "E") and (self.SorI == "S") and (self.TorF == "F") and (self.PorJ == "P")):
            from ESFP1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
           
            u.tabWidget.raise_()

            choice[:] = []
            Dialog.exec_()
        elif ((self.IorE == "E") and (self.SorI == "S") and (self.TorF == "F") and (self.PorJ == "J")):
            from ESFJ1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
            
            u.tabWidget.raise_()
            choice[:] = []

            Dialog.exec_()
        elif ((self.IorE == "I") and (self.SorI == "N") and (self.TorF == "F") and (self.PorJ == "P")):
            from INFP1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
            
            u.tabWidget.raise_()
            choice[:] = []

            Dialog.exec_()
        elif ((self.IorE == "I") and (self.SorI == "N") and (self.TorF == "F") and (self.PorJ == "J")):
            from INFJ1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
           
            u.tabWidget.raise_()

            choice[:] = []
            Dialog.exec_()
        elif ((self.IorE == "E") and (self.SorI == "N") and (self.TorF == "F") and (self.PorJ == "P")):
            from ENFP1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
           
            u.tabWidget.raise_()
            choice[:] = []
            Dialog.exec_()
        elif ((self.IorE == "E") and (self.SorI == "N") and (self.TorF == "F") and (self.PorJ == "J")):
            from ENFJ1 import Ui_Dialog

            Dialog = QtGui.QDialog()
            u = Ui_Dialog()
            u.setupUi(Dialog)
            
            u.tabWidget.raise_()
            choice[:] = []
            Dialog.exec_()





if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window1 = soal1JP1()
    window1.show()

    sys.exit(app.exec_())

