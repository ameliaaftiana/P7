def vokal(kalimat):
    #siapkan daftar huruf vokal, huruf besar dan kecil
    vokal='aAiIuUeEoO'
    jumlah=0
    #cek satu persatu karakternya
    for karakter in kalimat:
        #jika karakter ada di dalam daftar huruf vokal 
        if karakter in vokal:
            jumlah+=1
    return jumlah

def konsonan(kalimat):
    vokal='aAiIuUeEoO'
    jumlah=0
    for karakter in kalimat:
        #konsonan adalah karakter yang tidak termasuk vokal, tapi termasuk dalam alfabet 
        if karakter not in vokal and karakter.isalpha(): 
            jumlah += 1
    return jumlah

def angka(kalimat):
    angka='1234567890'
    jumlah=0
    for karakter in kalimat:
        if karakter in angka:
            jumlah += 1
    return jumlah 

def kosong(kalimat):
    jumlah=0
    for karakter in kalimat:
        if karakter.isspace():
            jumlah += 1
    return jumlah

def tanda(kalimat):
    tanda="'.!?"
    jumlah=0
    for karakter in kalimat:
        if karakter in tanda:
            jumlah += 1 
    return jumlah

#prgram utama
#input
kalimat=input("Masukan sebuah kalimat = ")

#proses
hasil=vokal(kalimat)
hasil2=konsonan(kalimat)
hasil3=angka(kalimat)
hasil4=kosong(kalimat)
hasil5=tanda(kalimat)

#output
print(f"Jumalh huruf vokal: {hasil}")
print(f"Jumlah huruf konsonan: {hasil2}")
print(f"Jumlah huruf digit: {hasil3}")
print(f"Jumlah white space: {hasil4}")
print(f"Jumlah tanda baca: {hasil5}")