# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intp.ui'
#
# Created: Mon May 04 07:04:37 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_Dialog(QtGui.QDialog):
    def __init__(self,parent):
        QtGui.QDialog.__init__(self,parent)

        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1281, 612)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 431, 491))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFrameShadow(QtGui.QFrame.Raised)
        self.label.setLineWidth(5)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/faisal21/PycharmProjects/5b9594c61c0709747b74f04c810943e1.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(560, 30, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(540, 110, 691, 471))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtGui.QFrame.Raised)
        self.label_3.setLineWidth(2)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(13)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1281, 611))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/faisal21/PycharmProjects/BFBC2_Clean_Background_2160_8-Bit.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(520, 10, 20, 581))
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(530, 90, 731, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "Kepribadian INTP", None))
        self.label_3.setText(_translate("Dialog", "INTP adalah orang-orang pendiam dan tidak banyak bicara. Mereka suka menggali hingga ke dasar masalah – rasa ingin tahu adalah dorongan terbesar mereka. Mereka ingin tahu apa yang menyatukan dunia jauh di dalamnya. Mereka tidak butuh lebih banyak untuk kebahagiaan mereka karena mereka adalah orang-orang yang rendah hati. Banyak ahli matematika, filsuf, dan ilmuwan merupakan tipe ini. Tipe Pemikir Analitis tidak suka kontradiksi dan ketidaklogisan; dengan kecerdasan mereka yang tajam, dengan cepat dan menyeluruh mereka menangkap pola, prinsip, dan struktur. Secara khusus mereka tertarik dengan sifat mendasar segala hal dan penemuan-penemuan teoritis; bagi mereka, tidak penting apakah mereka harus menerjemahkannya menjadi tindakan-tindakan praktis atau membagi pemikiran mereka kepada orang lain. Tipe Pemikir Analitis suka bekerja sendiri; kemampuan mereka untuk berkonsentrasi lebih menonjol dibanding tipe kepribadian yang lain. Mereka terbuka dan tertarik pada informasi baru.  Tipe Pemikir Analitis hanya memiliki sedikit ketertarikan pada masalah sehari-hari – mereka selalu agak seperti „profesor linglung“ yang rumah dan tempat kerjanya berantakan dan hanya mengkhawatirkan diri sendiri dengan hal-hal dasar seperti kebutuhan fisik ketika hal itu menjadi sangat tidak bisa dihindarkan. Pengakuan atas karya mereka oleh orang lain juga memegang peranan penting bagi mereka; \n"
"\n"
"secara umum, mereka cukup mandiri dalam hubungan sosial dan sangat mengandalkan diri sendiri. Oleh karena itu tipe Pemikir Analitis sering memberi kesan kepada orang lain bahwa mereka arogan atau congkak – terutama karena mereka tidak ragu untuk melontarkan isi kepala mereka dengan kritik mereka yang biasanya pedas (sekalipun beralasan) dan rasa percaya diri mereka yang tak tergoyahkan. Orang-orang di sekitarnya yang tidak kompeten tidak akan lolos dengan mudah dari mereka. Namun barangsiapa berhasil memenangkan rasa hormat dan ketertarikan mereka akan mendapatkan orang yang jenaka dan sangat cerdas untuk diajak berbincang. Pasangan yang membuat seseorang takjub dengan pengamatannya yang tajam dan selera humornya yang getir.", None))



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window1 = Ui_Dialog()
    window1.label.raise_()
    window1.label_2.raise_()
    window1.label_3.raise_()
    window1.show()
    sys.exit(app.exec_())


