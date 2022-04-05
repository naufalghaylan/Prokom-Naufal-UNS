def luas_sisi(sisi):
    luas = (sisi*sisi)
    print("============")
    print("luas bujur sangkar", luas)
    return(luas)

def volume_kubus(sisi): 
    volume = luas_sisi(sisi)*sisi
    print("=========================")
    print("Volume kubus = ", volume)
    return(volume)

def menu():
    print("=====================")
    print(" (1) Luas Bujur Sangkar ")
    print(" (2) volume kubus ")
    print("=====================")

print("selamat datang di program matematika")
menu()
sisi = int(input("Masukkan besaran sisi kubus = "))
pilih = int(input("Masukkan pilihan menu = "))
print("===========================")
if pilih == 1:
    luas_sisi(sisi)
else:
    volume_kubus(sisi)