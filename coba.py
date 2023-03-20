'''#untuk komentar panjang menggunakan tanda petik tiga
a,A=4
i,I=1
e,E=3
s,S=5
o,O=0
g,G=9
b=6
B=8
'''



#alay translator

def translate (kalimat):
    #daftar huruf alay
    nonalay='aAiIeEsSgGoOBb'
    alay='44113355990086'
    #cek satu persatu karakternya
    #for i in range (len(kalimat)): => menggunakan index (lebh fleksibel karenabisa dari depan maupun dari belakang)
    hasil=''
    for karakter in kalimat: #(hanya bisa salah satu dari depan atau dari belakang)
        if karakter in nonalay:
            #harus direplace
            idx=nonalay.index(karakter)
            hasil=hasil+alay[idx]
        else:
            hasil=hasil+karakter
    return hasil

#program utama
#input
kalimat=input("Masukkan sebuah kalimat = ")

#proses
hasil=translate(kalimat)
#output
print(hasil)