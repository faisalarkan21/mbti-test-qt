# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formUtama.ui'
#
# Created: Mon May 04 01:53:05 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1366, 768)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButtonMulai = QtGui.QPushButton(self.centralwidget)
        self.pushButtonMulai.setGeometry(QtCore.QRect(610, 70, 411, 171))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aller"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonMulai.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/faisal21/PycharmProjects/book-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonMulai.setIcon(icon)
        self.pushButtonMulai.setIconSize(QtCore.QSize(138, 120))
        self.pushButtonMulai.setCheckable(False)
        self.pushButtonMulai.setAutoDefault(False)
        self.pushButtonMulai.setDefault(False)
        self.pushButtonMulai.setFlat(True)
        self.pushButtonMulai.setObjectName(_fromUtf8("pushButtonMulai"))
        self.pushButtonCoba = QtGui.QPushButton(self.centralwidget)
        self.pushButtonCoba.setGeometry(QtCore.QRect(780, 220, 251, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aller"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCoba.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/faisal21/PycharmProjects/007485-blue-metallic-orb-icon-arrows-arrow-undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCoba.setIcon(icon1)
        self.pushButtonCoba.setIconSize(QtCore.QSize(120, 120))
        self.pushButtonCoba.setFlat(True)
        self.pushButtonCoba.setObjectName(_fromUtf8("pushButtonCoba"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 591, 421))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/faisal21/PycharmProjects/untitled1/Logo_Azul_MBTI-01.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1060, 40, 511, 451))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/faisal21/PycharmProjects/wall_lamp_png_by_paradise234-d5m5p0m.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(770, 320, 701, 401))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/faisal21/PycharmProjects/png_viny_leaves_by_moonglowlilly-d5n4df5.png")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-20, 310, 671, 391))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/faisal21/PycharmProjects/png_floating_terrain_by_moonglowlilly-d5qb58m.png")))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 1371, 771))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/faisal21/PycharmProjects/BFBC2_Clean_Background_2160_8-Bit.png")))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuKepribadian = QtGui.QMenu(self.menubar)
        self.menuKepribadian.setObjectName(_fromUtf8("menuKepribadian"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionTentang_kami = QtGui.QAction(MainWindow)
        self.actionTentang_kami.setObjectName(_fromUtf8("actionTentang_kami"))
        self.actionTentang_kami_2 = QtGui.QAction(MainWindow)
        self.actionTentang_kami_2.setObjectName(_fromUtf8("actionTentang_kami_2"))
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionTentang_kami_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuKepribadian.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButtonMulai.setToolTip(_translate("MainWindow", "Klik disini ", None))
        self.pushButtonMulai.setText(_translate("MainWindow", "Mulai Tes MBTI", None))
        self.pushButtonCoba.setText(_translate("MainWindow", "Tes Ulang", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuKepribadian.setTitle(_translate("MainWindow", "Kepribadian", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionTentang_kami.setText(_translate("MainWindow", "Tentang kami", None))
        self.actionTentang_kami_2.setText(_translate("MainWindow", "Tentang Kami", None))

