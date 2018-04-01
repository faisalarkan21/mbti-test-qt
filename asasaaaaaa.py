__author__ = 'faisal21'

from Tkinter import *


class project:


    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.komponen()
        self.backExstro()
        self.backFeel()
        self.backIntro()
        self.backIntusi()
        self.backJudg()
        self.backPercep()
        self.backSense()
        self.backThink()

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



    def komponen(self):
        self.frame = Frame(self.root, bd=5)
        self.frame.pack(fill=BOTH, expand=1)

        tombolJumlah = Button(self.frame, text="call!!" , command=self.call1)
        tombolJumlah.place(x=600,y=450)

        tombolJumlah = Button(self.frame, text="Submit!!" , command=self.jumlah)
        tombolJumlah.place(x=600,y=400)

        self.soal1()
        self.soal2()
        self.soal3()
        self.soal4()
        self.soal5()
        self.soal6()
        self.soal7()
        self.soal8()
        self.soal9()

    def soal1 (self):
        label = Label(self.frame,text="1. Apakah anda suka dengan kesendirian ?", font="Calibri 11" )
        self.nilai1 = IntVar()
        pilihan1 = Radiobutton(self.frame,text="Iya",value=1,variable=self.nilai1, command=self.calThink1)
        pilihan2 = Radiobutton(self.frame,text="Tidak",value=2,variable=self.nilai1, command=self.calThink1)
        label.place(x=50,y=50)
        pilihan1.place(x=60,y=70)
        pilihan2.place(x=60,y=90)

    def soal2 (self):
        label = Label(self.frame,text="2. Apakah anda suka dengan Keramaian ?", font="Calibri 11" )
        self.nilai2 = IntVar()
        pilihan1 = Radiobutton(self.frame,text="Iya",value=1,variable=self.nilai2, command=self.calThink1)
        pilihan2 = Radiobutton(self.frame,text="Tidak",value=2,variable=self.nilai2, command=self.calThink1)
        label.place(x=50,y=120)
        pilihan1.place(x=60,y=140)
        pilihan2.place(x=60,y=160)

    def soal3 (self):
        label = Label(self.frame,text="3. Apakah anda suka Mengkritik seseorang ?", font="Calibri 11" )
        self.nilai3 = IntVar()
        pilihan1 = Radiobutton(self.frame,text="Iya",value=1,variable=self.nilai3, command=self.calThink3)
        pilihan2 = Radiobutton(self.frame,text="Tidak",value=2,variable=self.nilai3, command=self.calThink3)
        label.place(x=50,y=190)
        pilihan1.place(x=60,y=210)
        pilihan2.place(x=60,y=240)

    def soal4 (self):
        label = Label(self.frame,text="4. Pergi sendiri atau berdua dengan teman ?", font="Calibri 11" )
        self.nilai4 = IntVar()
        pilihan1 = Radiobutton(self.frame,text="sendiri",value=1,variable=self.nilai4, command=self.calIntuisi1)
        pilihan2 = Radiobutton(self.frame,text="berdua",value=2,variable=self.nilai4, command=self.calIntuisi1)
        label.place(x=50,y=270)
        pilihan1.place(x=60,y=290)
        pilihan2.place(x=60,y=310)

    def soal5 (self):
        label = Label(self.frame,text="5. Pergi sendiri atau berdua dengan teman ?", font="Calibri 11" )
        self.nilai5 = IntVar()
        pilihan1 = Radiobutton(self.frame,text="sendiri",value=1,variable=self.nilai5, command=self.calIntuisi2)
        pilihan2 = Radiobutton(self.frame,text="berdua",value=2,variable=self.nilai5, command=self.calIntuisi2)
        label.place(x=50,y=340)
        pilihan1.place(x=60,y=360)
        pilihan2.place(x=60,y=380)

    def soal6 (self):
        label = Label(self.frame,text="6. Pergi sendiri atau berdua dengan teman ?", font="Calibri 11" )
        self.nilai6 = IntVar()
        pilihan1 = Radiobutton(self.frame,text="sendiri",value=1,variable=self.nilai6, command=self.calIntuisi3)
        pilihan2 = Radiobutton(self.frame,text="berdua",value=2,variable=self.nilai6, command=self.calIntuisi3)
        label.place(x=50,y=410)
        pilihan1.place(x=60,y=430)
        pilihan2.place(x=60,y=450)

    def soal7 (self):
        label = Label(self.frame,text="7. Pergi sendiri atau berdua dengan teman ?", font="Calibri 11" )
        self.nilai7 = IntVar()
        pilihan1 = Radiobutton(self.frame,text="sendiri",value=1,variable=self.nilai7, command=self.calIntro1)
        pilihan2 = Radiobutton(self.frame,text="berdua",value=2,variable=self.nilai7, command=self.calIntro1)
        label.place(x=50,y=480)
        pilihan1.place(x=60,y=500)
        pilihan2.place(x=60,y=520)

    def soal8 (self):
        label = Label(self.frame,text="8. Pergi sendiri atau berdua dengan teman ?", font="Calibri 11" )
        self.nilai8 = IntVar()
        pilihan1 = Radiobutton(self.frame,text="sendiri",value=1,variable=self.nilai8, command=self.calIntro2)
        pilihan2 = Radiobutton(self.frame,text="berdua",value=2,variable=self.nilai8, command=self.calIntro2)
        label.place(x=50,y=550)
        pilihan1.place(x=60,y=570)
        pilihan2.place(x=60,y=590)

    def soal9 (self):
        label = Label(self.frame,text="9. Pergi sendiri atau berdua dengan teman ?", font="Calibri 11" )
        self.nilai9 = IntVar()
        pilihan1 = Radiobutton(self.frame,text="sendiri",value=1,variable=self.nilai9, command=self.calIntro3)
        pilihan2 = Radiobutton(self.frame,text="berdua",value=2,variable=self.nilai9, command=self.calIntro3)
        label.place(x=50,y=620)
        pilihan1.place(x=60,y=640)
        pilihan2.place(x=60,y=660)



    def call1(self, event=None):
        if (self.jwb1 == 1):
            self.subThink1 =+1

        elif(self.jwb1 == 2) :
            self.subFeel1 =+1



    def calThink1(self):
        self.jwb1 = self.nilai1.get()
        print self.jwb1





    def calThink2(self, event=None):
        jwb = self.nilai2.get()
        if (jwb==1):
            self.subThink2 =+1
        else :
            self.subFeel2 =+1

    def calThink3(self, event=None):
        jwb = self.nilai3.get()

        if (jwb==1):
            self.subThink3 =+1
        else:
            self.subFeel3 =+1

    def calIntuisi1(self, event=None):
        jwb = self.nilai4.get()

        if (jwb==1):
            self.subIntuisi1 =+1
        else:
            self.subSense1 =+1

    def calIntuisi2(self, event=None):
        jwb = self.nilai5.get()

        if (jwb==1):
            self.subIntuisi2 =+1
        else:
            self.subSense2 =+1

    def calIntuisi3(self, event=None):
        jwb = self.nilai6.get()

        if (jwb==1):
            self.subIntuisi3 =+1
        else:
            self.subSense3 =+1

    def calIntro1(self, event=None):
        jwb = self.nilai7.get()

        if (jwb==1):
            self.subIntro1 =+1
        else:
            self.subExstro1 =+1


    def calIntro2(self, event=None):
        jwb = self.nilai8.get()

        if (jwb==1):
            self.subIntro2 =+1
        else:
            self.subExstro2 =+1

    def calIntro3(self, event=None):
        jwb = self.nilai9.get()

        if (jwb==1):
            self.subIntro3 =+1
        else:
            self.subExstro3 =+1



    def jumlah (self , event=None):
        self.Think = self.subThink1 + self.subThink2 + self.subThink3
        self.Feel = self.subFeel1 + self.subFeel2 + self.subFeel3
        self.intuisi= self.subIntuisi1 +  self.subIntuisi2 + self.subIntuisi3
        self.sense = self.subSense1 + self.subSense2  + self.subSense3
        self.Intro = self.subIntro1 + self.subIntro2 + self.subIntro3
        self.Exstro = self.subExstro1 + self.subExstro2 + self.subExstro3



        skorThink = Label(self.frame,text="Skor Think Anda : %d" % self.Think)
        skorFeel = Label(self.frame,text="Skor Feel Anda : %d" % self.Feel)
        skorintuisi = Label(self.frame,text="Skor Intuisi Anda : %d" % self.intuisi)
        skorsense = Label(self.frame,text="Skor Feel Sense : %d" % self.sense)
        skorInto = Label(self.frame,text="Skor Feel Intro : %d" % self.Intro)
        skorExtro = Label(self.frame,text="Skor Feel Ektro : %d" % self.Exstro)


        skorThink.place(x=300, y=430)
        skorFeel.place(x=300, y=450)
        skorintuisi.place(x=300, y=470)
        skorsense.place(x=300, y=490)
        skorInto.place(x=300, y=510)
        skorExtro.place(x=300,y=530)




if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    obj = project(root, "Coba1")
    root.mainloop()






