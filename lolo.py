a = input("Masukan angka : ")

z=0
x=0
if (a%2==0):
    print 'genap'
    for i in range (2,a,2):
        print i
        z = z + i
    print a
    print "jumlah", z+a

elif (a%2==1):
    print 'ganjil'
    for i in range (1,a,2):
        print i
        z = z + i
    print a
    print "jumlah", z+a

else :
    "engga ada"

