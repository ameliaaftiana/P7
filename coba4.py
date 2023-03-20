# def cek_palindrome(kalimat):
#     #palindrome hanya mengecek alfabet (A-Z dan a-z)
#     #konversi semuanya ke huruf kecil
#     kalimat=kalimat.lower()
#     #penggunaan lower tidak merubah inputan asli
#     balik=kalimat[::-1]
#     #untuk mereverse suatu kalimat atau kata atau menulis dari belakang tapi langkahnya mundur
#     if kalimat==balik:
#         print("Palindrome!")
#     else:
#         print("Bukan Palindrome")

# #input
# kalimat=input("Masukkan kalimat = ")

# cek_palindrome(kalimat)

def cek_palindrome(kalimat):
    #palindrome hanya mengecek alfabet (A-Z dan a-z)
    #konversi semuanya ke huruf kecil
    kalimat=kalimat.lower()
    #buang semua yang bukan alfabet
    hasil=""
    for karakter in kalimat:
        if karakter.isalpha():
            hasil=hasil+karakter

    balik=hasil[::-1] #start,stop,stop

    if hasil==balik:
        print("Palindrome!")
    else:
        print("Bukan Palindrome")

   
#input
kalimat=input("Masukkan kalimat = ")

cek_palindrome(kalimat)

'''
kalau string terlalu panjang, lebih baik masukkan dalam file lalu program membaca filenya
'''