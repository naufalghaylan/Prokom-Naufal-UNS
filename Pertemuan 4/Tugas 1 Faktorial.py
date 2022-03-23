angka = int(input("Masukkan angka= "))
faktorial = 1
if angka < 0 :
    print("Angka negatif tidak terdapat faktorial")
elif angka == 0 :
    print("Faktorial 0 adalah 1")
else :
    for i in range(1, angka+1):
        faktorial= faktorial*i
    print("Faktorial angka", angka,"adalah",faktorial)