def luas_segitiga(alas, tinggi):
    luas = (alas*tinggi)/2
    print("==========================")
    print("Luas segitiga =", luas)

#program utama
print("Selamat datang di program utama")
alas = int(input("Masukkan nilai alas segitiga = "))
tinggi = int(input("Masukkan nilai tinggi segitiga = "))
#memanggil fungsi   
luas_segitiga(alas, tinggi)
