# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nextForm.ui'
#
# Created: Wed Jun 03 20:17:32 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(786, 346)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Dialog.setFont(font)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.soal1 = QtGui.QLabel(Dialog)
        self.soal1.setGeometry(QtCore.QRect(96, 30, 591, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.soal1.setFont(font)
        self.soal1.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1.setLineWidth(1)
        self.soal1.setAlignment(QtCore.Qt.AlignCenter)
        self.soal1.setObjectName(_fromUtf8("soal1"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(166, 110, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButtonJ1 = QtGui.QRadioButton(self.groupBox)
        self.radioButtonJ1.setGeometry(QtCore.QRect(20, 70, 471, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(13)
        self.radioButtonJ1.setFont(font)
        self.radioButtonJ1.setObjectName(_fromUtf8("radioButtonJ1"))
        self.radioButtonP1 = QtGui.QRadioButton(self.groupBox)
        self.radioButtonP1.setGeometry(QtCore.QRect(20, 40, 361, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(13)
        self.radioButtonP1.setFont(font)
        self.radioButtonP1.setObjectName(_fromUtf8("radioButtonP1"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 731, 61))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(37, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/faisal21/Downloads/1433353652_basics-05.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(563, 14, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/faisal21/Downloads/1433353645_basics-06.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.soal1_2 = QtGui.QLabel(self.groupBox_2)
        self.soal1_2.setGeometry(QtCore.QRect(317, 8, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soal1_2.setFont(font)
        self.soal1_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.soal1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.soal1_2.setLineWidth(1)
        self.soal1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.soal1_2.setObjectName(_fromUtf8("soal1_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.soal1.setText(_translate("Dialog", "Anda adalah tipe seseorang yang ?", None))
        self.groupBox.setTitle(_translate("Dialog", "Pilihan", None))
        self.radioButtonJ1.setText(_translate("Dialog", "Terencana, Terstruktur dan memiliki deadline yang jelas ", None))
        self.radioButtonP1.setText(_translate("Dialog", "Spontan, Fleksibel, tidak diikat waktu ", None))
        self.pushButton_2.setText(_translate("Dialog", "Kembali     ", None))
        self.pushButton.setText(_translate("Dialog", "       Selanjutnya", None))
        self.soal1_2.setText(_translate("Dialog", "Hal 1", None))

