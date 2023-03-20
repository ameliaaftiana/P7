#cara 1
# tanggal=input("Masukkan tanggal (tahun bulan tanggal) = ")

# baru=tanggal.split(" ")
# print (baru[-1], baru[-2], baru[0])

#cara 2
def tanggal(tgl):
    return tgl[-2:] + '-' + tgl[5:7] + '-' + tgl[:4]

#program utama
tgl='2021-11-31'
hasil=tanggal(tgl)
print(f"Konversi ke DD-MM-YYYY = {hasil}")
