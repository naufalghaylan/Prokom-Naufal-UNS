totalBelanja= int(input("Berapa nilai Pembelian anda?= Rp."))
totalBayar = totalBelanja
print("==========================")
if totalBelanja >= 100000:
    print("Selamat, Pelanggan mendapatkan diskon 10%")
    potongan= totalBelanja*0.1
    totalBayar= totalBelanja-potongan
print("Total pembayaran anda setelah discount adalah Rp.", int(totalBayar))
print("==========================")