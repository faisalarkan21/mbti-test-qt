# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ENFP1.ui'
#
# Created: Mon Jun 15 11:09:31 2015
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
        Dialog.resize(1278, 640)
        Dialog.setMinimumSize(QtCore.QSize(1278, 640))
        Dialog.setMaximumSize(QtCore.QSize(1278, 640))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 140, 1281, 500))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("NewsGoth Cn BT"))
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)

        self.tabWidget.setFont(font)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.widget = QtGui.QWidget()
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(-10, -10, 1291, 501))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("Base Picture/ENFP/ciri.jpg")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.widget, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(-10, -40, 1291, 581))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("Base Picture/ENFP/kerja1.jpg")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(-10, -30, 1291, 541))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("Base Picture/ENFP/tokoh.jpg")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(-10, -30, 1291, 541))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("Base Picture/ENFP/pengembangan.jpg")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(-10, -30, 1291, 541))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("Base Picture/ENFP/dekprip.jpg")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -30, 1291, 640))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Base Picture/ENFP/base.jpg")))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Kepribadian ENFP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Dialog", "Ciri - Ciri ENFP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Saran Karir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tokoh Terkenal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Saran Pengembangan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Deskripsi Lebih Lanjut", None))

