__author__ = 'faisal21'

import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog
from PyQt4 import QtCore
from dialog import  Ui_Dialog
from Tkinter import *

class Test(QtGui.QDialog,Toplevel):
    def __init__(self,parent):
        QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.setEnabled(False)




        self.backExstro()
        self.backFeel()
        self.backIntro()
        self.backIntusi()
        self.backJudg()
        self.backPercep()
        self.backSense()
        self.backThink()
        self.actTombol()
        self.act()


    ##############################################
    ################InstalasiVariable###################
    ##############################################

    def backIntusi(self):
        self.Intuisi = 0
        self.subIntuisi1= 0
        self.subIntuisi2 = 0
        self.subIntuisi3 = 0
        self.subIntuisi4 = 0
        self.subIntuisi5 = 0

    def backSense(self):
        self.Sense = 0
        self.subSense1 = 0
        self.subSense2 = 0
        self.subSense3 = 0
        self.subSense4 = 0
        self.subSense5 = 0
    def backExstro(self):
        self.Exstro = 0
        self.subExstro1 = 0
        self.subExstro2 = 0
        self.subExstro3 = 0
        self.subExstro4 = 0
        self.subExstro5 = 0
    def backIntro(self):
        self.Intro = 0
        self.subIntro1 = 0
        self.subIntro2 = 0
        self.subIntro3 = 0
        self.subIntro4 = 0
        self.subIntro5 = 0
    def backJudg(self):
        self.Judg = 0
        self.subJudg1 = 0
        self.subJudg2 = 0
        self.subJudg3 = 0
        self.subJudg4 = 0
        self.subJudg5 = 0
    def backPercep(self):
        self.Percep =0
        self.subPercep1 = 0
        self.subPercep2 = 0
        self.subPercep3 = 0
        self.subPercep4 = 0
        self.subPercep5 = 0
    def backThink(self):
        self.Think = 0
        self.subThink1 = 0
        self.subThink2 = 0
        self.subThink3 = 0
        self.subThink4 = 0
        self.subThink5 = 0
    def backFeel(self):
        self.Feel = 0
        self.subFeel1 = 0
        self.subFeel2 = 0
        self.subFeel3 = 0
        self.subFeel4 = 0
        self.subFeel5 = 0


    ##############################################
    ################Action###################
    ##############################################

    def actTombol (self):
        self.ui.pushButton.clicked.connect(self.jumTotal)
        self.ui.pushButton_2.clicked.connect(self.kalkulasi)

    def act(self):
        self.ui.radioButtonP1.clicked.connect(self.soal1)
        self.ui.radioButtonJ1.clicked.connect(self.soal1)

        self.ui.radioButtonI1.clicked.connect(self.soal2)
        self.ui.radioButtonE1.clicked.connect(self.soal2)

        self.ui.radioButtonT1.clicked.connect(self.soal3)
        self.ui.radioButtonF1.clicked.connect(self.soal3)

        self.ui.radioButtonN1.clicked.connect(self.soal4)
        self.ui.radioButtonS1.clicked.connect(self.soal4)

        self.ui.radioButtonJ1_2.clicked.connect(self.soal5)
        self.ui.radioButtonP1_2.clicked.connect(self.soal5)

        self.ui.radioButtonI1_2.clicked.connect(self.soal6)
        self.ui.radioButtonE1_2.clicked.connect(self.soal6)

        self.ui.radioButtonN2.clicked.connect(self.soal7)
        self.ui.radioButtonS2.clicked.connect(self.soal7)

        self.ui.radioButtonE2.clicked.connect(self.soal8)
        self.ui.radioButtonI2.clicked.connect(self.soal8)

        self.ui.radioButtonJ2.clicked.connect(self.soal9)
        self.ui.radioButtonP2.clicked.connect(self.soal9)


        self.ui.radioButtonF2.clicked.connect(self.soal10)
        self.ui.radioButtonT2.clicked.connect(self.soal10)

        self.ui.radioButtonS2_2.clicked.connect(self.soal11)
        self.ui.radioButtonN2_2.clicked.connect(self.soal11)

        self.ui.radioButtonT2_2.clicked.connect(self.soal12)
        self.ui.radioButtonF2_2.clicked.connect(self.soal12)

        self.ui.radioButtonS3.clicked.connect(self.soal13)
        self.ui.radioButtonN3.clicked.connect(self.soal13)

        self.ui.radioButtonJ3.clicked.connect(self.soal14)
        self.ui.radioButtonP3.clicked.connect(self.soal14)

        self.ui.radioButtonN3_3.clicked.connect(self.soal15)
        self.ui.radioButtonS3_3.clicked.connect(self.soal15)

        self.ui.radioButtonI3.clicked.connect(self.soal16)
        self.ui.radioButtonE3.clicked.connect(self.soal16)

        self.ui.radioButtonF3.clicked.connect(self.soal17)
        self.ui.radioButtonT3.clicked.connect(self.soal17)

        self.ui.radioButtonJ3_2.clicked.connect(self.soal18)
        self.ui.radioButtonP3_2.clicked.connect(self.soal18)

        self.ui.radioButtonE4.clicked.connect(self.soal19)
        self.ui.radioButtonI4.clicked.connect(self.soal19)

        self.ui.radioButtonT4.clicked.connect(self.soal20)
        self.ui.radioButtonF4.clicked.connect(self.soal20)


    ##############################################
    ################ Check Button Choice ###################
    ##############################################

    def soal1 (self):
        if (self.ui.radioButtonP1.isChecked()):
            self.jwb1 = 1
        elif (self.ui.radioButtonJ1.isChecked()):
            self.jwb1 = 2

    def soal2 (self):
        if (self.ui.radioButtonI1.isChecked()):
            self.jwb2 = 1
        elif (self.ui.radioButtonE1.isChecked()):
            self.jwb2 = 2

    def soal3 (self):
        if (self.ui.radioButtonT1.isChecked()):
            self.jwb3 = 1
        elif (self.ui.radioButtonF1.isChecked()):
            self.jwb3 = 2

    ###################

    def soal4 (self):
        if (self.ui.radioButtonN1.isChecked()):
            self.jwb4 = 1
        elif (self.ui.radioButtonS1.isChecked()):
            self.jwb4 = 2

    def soal5 (self):
        if (self.ui.radioButtonJ1_2.isChecked()):
            self.jwb5 = 1
        elif (self.ui.radioButtonP1_2.isChecked()):
            self.jwb5 = 2

    def soal6 (self):
        if (self.ui.radioButtonI1_2.isChecked()):
            self.jwb6 = 1
        elif (self.ui.radioButtonE1_2.isChecked()):
            self.jwb6 = 2

    #####################

    def soal7 (self):
        if (self.ui.radioButtonN2.isChecked()):
            self.jwb7 = 1
        elif (self.ui.radioButtonS2.isChecked()):
            self.jwb7 = 2

    def soal8 (self):
        if (self.ui.radioButtonE2.isChecked()):
            self.jwb8 = 1
        elif (self.ui.radioButtonI2.isChecked()):
            self.jwb8 = 2

    def soal9 (self):
        if (self.ui.radioButtonJ2.isChecked()):
            self.jwb9 = 1
        elif (self.ui.radioButtonP2.isChecked()):
            self.jwb9 = 2


    def soal10 (self):
        if (self.ui.radioButtonF2.isChecked()):
            self.jwb10 = 1
        elif (self.ui.radioButtonT2.isChecked()):
            self.jwb10 = 2

    def soal11 (self):
        if (self.ui.radioButtonS2_2.isChecked()):
            self.jwb11 = 1
        elif (self.ui.radioButtonN2_2.isChecked()):
            self.jwb11 = 2

    def soal12 (self):
        if (self.ui.radioButtonT2_2.isChecked()):
            self.jwb12 = 1
        elif (self.ui.radioButtonF2_2.isChecked()):
            self.jwb12 = 2

    ################

    def soal13 (self):
        if (self.ui.radioButtonS3.isChecked()):
            self.jwb13 = 1
        elif (self.ui.radioButtonN3.isChecked()):
            self.jwb13 = 2

    def soal14 (self):
        if (self.ui.radioButtonJ3.isChecked()):
            self.jwb14 = 1
        elif (self.ui.radioButtonP3.isChecked()):
            self.jwb14 = 2

    def soal15 (self):
        if (self.ui.radioButtonN3_3.isChecked()):
            self.jwb15 = 1
        elif (self.ui.radioButtonS3_3.isChecked()):
            self.jwb15 = 2

    ###################

    def soal16 (self):
        if (self.ui.radioButtonI3.isChecked()):
            self.jwb16 = 1
        elif (self.ui.radioButtonE3.isChecked()):
            self.jwb16 = 2

    def soal17 (self):
        if (self.ui.radioButtonF3.isChecked()):
            self.jwb17 = 1
        elif (self.ui.radioButtonT3.isChecked()):
            self.jwb17 = 2

    def soal18 (self):
        if (self.ui.radioButtonJ3_2.isChecked()):
            self.jwb18 = 1
        elif (self.ui.radioButtonP3_2.isChecked()):
            self.jwb18 = 2

    #####################

    def soal19 (self):
        if (self.ui.radioButtonE4.isChecked()):
            self.jwb19 = 1
        elif (self.ui.radioButtonI4.isChecked()):
            self.jwb19 = 2

    def soal20 (self):
        if (self.ui.radioButtonT4.isChecked()):
            self.jwb20 = 1
        elif (self.ui.radioButtonF4.isChecked()):
            self.jwb20 = 2



    ##############################################
    ################subJumlah###################
    ##############################################

    def jumSoal1 (self):
        if (self.jwb1 == 1):
            self.subPercep1 =+1
        else :
            self.subJudg1 = +1

    def jumSoal2 (self):
        if (self.jwb2 == 1):
            self.subIntro1 =+1
        else :
            self.subExstro1 = +1

    def jumSoal3 (self):
        if (self.jwb3 == 1):
            self.subThink1 =+1
        else :
            self.subFeel1 = +1

    ##############

    def jumSoal4 (self):
        if (self.jwb4 == 1):
            self.subIntuisi1 =+1
        else :
            self.subSense1 = +1

    def jumSoal5 (self):
        if (self.jwb5 == 1):
            self.subJudg2 =+1
        else :
            self.subPercep2 = +1

    def jumSoal6 (self):
        if (self.jwb6 == 1):
            self.subIntro2 =+1
        else :
            self.subExstro2 = +1

    #########################

    def jumSoal7 (self):
        if (self.jwb7 == 1):
            self.subIntuisi2 =+1
        else :
            self.subSense2 = +1

    def jumSoal8 (self):
        if (self.jwb8 == 1):
            self.subExstro3 =+1
        else :
            self.subIntro3 = +1

    def jumSoal9 (self):
        if (self.jwb9 == 1):
            self.subJudg3 =+1
        else :
            self.subPercep3 = +1


    def jumSoal10 (self):
        if (self.jwb10 == 1):
            self.subFeel2 =+1
        else :
            self.subThink2 = +1

    def jumSoal11 (self):
        if (self.jwb11 == 1):
            self.subSense3 =+1
        else :
            self.subIntuisi3 = +1
    def jumSoal12 (self):
        if (self.jwb12 == 1):
            self.subThink3 =+1
        else :
            self.subFeel3 = +1

    def jumSoal13 (self):
        if (self.jwb13 == 1):
            self.subSense4 =+1
        else :
            self.subIntuisi4 = +1

    def jumSoal14 (self):
        if (self.jwb14 == 1):
            self.subJudg4 =+1
        else :
            self.subPercep4 = +1

    def jumSoal15 (self):
        if (self.jwb15 == 1):
            self.subIntuisi5 =+1
        else :
            self.subSense5 = +1

    def jumSoal16 (self):
        if (self.jwb16 == 1):
            self.subIntro4 =+1
        else :
            self.subExstro4 = +1

    def jumSoal17 (self):
        if (self.jwb17 == 1):
            self.subFeel4 =+1
        else :
            self.subThink4 = +1

    def jumSoal18 (self):
        if (self.jwb18 == 1):
            self.subJudg5 =+1
        else :
            self.subPercep5 = +1

    def jumSoal19 (self):
        if (self.jwb19 == 1):
            self.subExstro5 =+1
        else :
            self.subIntro5 = +1

    def jumSoal20 (self):
        if (self.jwb20 == 1):
            self.subThink5 =+1
        else :
            self.subFeel5 = +1


    ##############################################
    ################jumlahTotal###################
    ##############################################


    def jumTotal(self):

        if ((self.ui.radioButtonP1.isChecked() or self.ui.radioButtonJ1.isChecked()) and
                (self.ui.radioButtonI1.isChecked() or self.ui.radioButtonE1.isChecked()) and
                (self.ui.radioButtonT1.isChecked() or self.ui.radioButtonF1.isChecked()) and
                (self.ui.radioButtonN1.isChecked() or self.ui.radioButtonS1.isChecked()) and
                (self.ui.radioButtonJ1_2.isChecked() or self.ui.radioButtonP1_2.isChecked()) and
                (self.ui.radioButtonI1_2.isChecked() or self.ui.radioButtonE1_2.isChecked()) and
                (self.ui.radioButtonN2.isChecked() or self.ui.radioButtonS2.isChecked()) and
                (self.ui.radioButtonE2.isChecked() or self.ui.radioButtonI2.isChecked()) and
                (self.ui.radioButtonJ2.isChecked() or self.ui.radioButtonP2.isChecked()) and
                (self.ui.radioButtonF2.isChecked() or self.ui.radioButtonT2.isChecked())and
                (self.ui.radioButtonS2_2.isChecked() or self.ui.radioButtonN2_2.isChecked()) and
                (self.ui.radioButtonT2_2.isChecked() or self.ui.radioButtonF2_2.isChecked()) and
                (self.ui.radioButtonS3.isChecked() or self.ui.radioButtonN3.isChecked()) and
                (self.ui.radioButtonJ3.isChecked() or self.ui.radioButtonP3.isChecked()) and
                (self.ui.radioButtonN3_3.isChecked() or self.ui.radioButtonS3_3.isChecked()) and
                (self.ui.radioButtonI3.isChecked() or self.ui.radioButtonE3.isChecked()) and
                (self.ui.radioButtonF3.isChecked() or self.ui.radioButtonT3.isChecked()) and
                (self.ui.radioButtonJ3_2.isChecked() or self.ui.radioButtonP3_2.isChecked()) and
                (self.ui.radioButtonE4.isChecked() or self.ui.radioButtonI4.isChecked()) and
                (self.ui.radioButtonT4.isChecked() or self.ui.radioButtonF4.isChecked())):


            self.jumSoal1()
            self.jumSoal2()
            self.jumSoal3()
            self.jumSoal4()
            self.jumSoal5()
            self.jumSoal6()
            self.jumSoal7()
            self.jumSoal8()
            self.jumSoal9()
            self.jumSoal10()
            self.jumSoal11()
            self.jumSoal12()
            self.jumSoal13()
            self.jumSoal14()
            self.jumSoal15()
            self.jumSoal16()
            self.jumSoal17()
            self.jumSoal18()
            self.jumSoal19()
            self.jumSoal20()
            self.ui.pushButton_2.setEnabled(True)
            QDialog.QMessageBox.information(self, "Pehatihan", "Silahkan tekan tombol Lihat hasil","Oke")
        else :
          QDialog.QMessageBox.information(self, "Pehatihan", "Tolong isi semua pilihan Terlebih dahulu","Oke")













    ##############################################
    ################KalkulasiTotal###################
    ##############################################


    def kalkulasi (self):
        self.ui.pushButton_2.setEnabled(False)
        self.Intro =  self.subIntro1 + self.subIntro2 + self.subIntro3 +self.subIntro4+self.subIntro5
        self.Exstro =  self.subExstro1 + self.subExstro2 + self.subExstro3 +self.subExstro4 + self.subExstro5
        self.Percep = self.subPercep1 + self.subPercep2 + self.subPercep3 +self.subPercep4 +self.subPercep5
        self.Judg = self.subJudg1 + self.subJudg2 + self.subJudg3+ self.subJudg4+self.subJudg5
        self.Feel = self.subFeel1 + self.subFeel2 + self.subFeel3 + self.subFeel4 + self.subFeel5
        self.Think = self.subThink1 + self.subThink2+ self.subThink3 + self.subThink4 + self.subThink5
        self.Sense = self.subSense1 + self.subSense2 +self.subSense3 +self.subSense4 +self.subSense5
        self.Intuisi = self.subIntuisi1 + self.subIntuisi2 + self.subIntuisi3 +self.subIntuisi4 +self.subIntuisi5



        if (self.Intro<self.Exstro):
            self.IorE = "E"
        elif (self.Intro>self.Exstro):
             self.IorE = "I"

        if (self.Sense < self.Intuisi):
             self.SorI = "N"
        else :
             self.SorI = "S"

        if (self.Think < self.Feel):
             self.TorF = "F"
        else :
             self.TorF = "T"

        if (self.Percep < self.Judg):
            self.PorJ = "J"
        else :
            self.PorJ = "P"



        self.ui.label_2.setText("Skor Inrovert anda adalah : %d" % self.Intro + "\n" + "Skor Extrovert anda adalah : %d" % self.Exstro +"\n"
                                + "Skor Peception anda adalah : %d" % self.Percep + "\n" + "Skor Jugje anda adalah : %d" % self.Judg +"\n"+
                                "Skor Feel anda adalah : %d" % self.Feel + "\n" + "Skor Think anda adalah : %d" % self.Think + "\n" +
                                "Skor Sense anda adalah : %d" % self.Sense + "\n" + "Skor Intuisi anda adalah : %d" % self.Intuisi + "\n" + "Anda Adalah : " + self.IorE+self.SorI+self.TorF+self.PorJ )

        QDialog.QMessageBox.information(self, "Pehatihan", "Selamat anda adalah seorang  %s%s%s%s" % (self.IorE,self.SorI,self.TorF,self.PorJ),"Terimakasih :)")



        print "nilai Inrovert anda adalah : %d" % self.Intro
        print "nilai Extrovert anda adalah : %d" % self.Exstro
        print "Nilai Peception anda adalah : %d" % self.Percep
        print "Nilai Jugje anda adalah : %d" % self.Judg
        print "Nilai Feel anda adalah : %d" % self.Feel
        print "Nilai Think anda adalah : %d" % self.Think
        print "Nilai Sense anda adalah : %d" % self.Sense
        print "Nilai Intuisi anda adalah : %d" % self.Intuisi






##############################################
################MainExcecution###################
##############################################

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())

