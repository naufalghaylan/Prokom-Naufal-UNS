import bacadata 

def main():
    "Main program of UAS"
    "Lengkapi baris-baris kode di bawah ini dan ikuti semua permintaan dari soal setahap demi setahap"
    
    # A. pembacaan data menggunakan modul bacadata
    print("A. Baca file produk yang telah tersedia menggunakan modul bacadata")
    dict = bacadata.bacaJSON("produk.json") # Lengkapi
    print() # spasi untuk memudahkan penilaian
    
    # B. Tampilkan data produk hasil pembacaan data
    print("B. Menampilkan data seluruh produk hasil pembacaan data")
    produk = dict['Produk'] # Lengkapi
    print(produk) # Lengkapi untuk menampilkan dictionary data produk seluruhnya
    print() # spasi untuk memudahkan penilaian
    
    # C. Tampilkan/print satu contoh data produk secara lengkap
    print("C. Menampilkan/print satu contoh data produk ")
    satudata = produk["P513"]
    print(satudata)
    # Buat KODE PROGRAM SEDERHANA untuk menampilkan satu data produk 
    print() # spasi untuk memudahkan penilaian
    
    # D. Baca data penjualan pada file penjualan.json, gunakan modul bacadata
    print("D. Membaca data pada file penjualan")
    penjualan = bacadata.bacaJSON('penjualan.json') # Lengkapi
    penjualan["P231"][15] = 79 #Ganti Angka 10 dengan angka integer nim Anda
    print() # spasi untuk memudahkan penilaian
    
    # E. Hitung dan simpan dalam dictionary pendapatan setiap produk
    print("E. Hitung jumlah penjualan dan pendapatan setiap produk dan simpan masing2 dalam dictionary")
    jualan={} 
    pendapatan={}   
    for kode in penjualan:
        harga = produk[kode]["harga"]# Lengkapi
        jual = 0
        total = 0
        for i in range (len(penjualan[kode])): # Lengkapi
            jual += penjualan[kode][i] # Lengkapi
            total += harga*jual # Lengkapi
        # Menyimpan ke dictionary
        jualan[kode] = jual #Lengkapi
        pendapatan[kode] = total # Lengkapi
    print(pendapatan)
    # Tampilkan pendapatan setiap produk secara sederhana seperti contoh (Tidak harus rapi sekali)
    # Kode Nama Satuan Stock Harga Terjual Pendapatan
    # P574 Mie Bumbu Pack 225 2500 x y
    # Gunakan mekanisme Loop atau pengulangan sederhana untuk membuat tampilan seperti contoh
    print() # spasi untuk memudahkan penilaian
    
    # F. Hitung total pendapatan dari seluruh produk sebulan tersebut
    print("F. Hitung total pendapatan")
    totalpendapatan=0
    for i in pendapatan:
        totalpendapatan += pendapatan[i]
    print("Total pendapatan sebulan: ", totalpendapatan)
    print()
    # Buat KODE PROGRAM SENDIRI untuk hitung total pendapatan seluruh produk
    # Gunakakan loop/pengulangan atau mekanisme lainnya
    
    print("Total pendapatan sebulan : ", totalpendapatan)
    print() # spasi untuk memudahkan penilaian
    
    # G. Hitung % pendapatan setiap produk dan simpan dalam sebuah dictionary
    print("G. Hitung prosentase pendapatan setiap produk dan simpan ke tipe data dictionary")
    dictProsentase ={}
    for kode in pendapatan:
        prosentase = pendapatan[kode]/totalpendapatan*100 # lengkapi
        dictProsentase[kode] = prosentase #Lengkapi
    print(dictProsentase)
    print() # spasi untuk memudahkan penilaian
    
    # H. Urutkan data pada dictionary prosentase, dari terbesar ke kecil
    # Buat KODE PROGRAM SENDIRI, wajib menggunakan algoritma bubble 
    #sort ATAU selection sort dalam bentuk FUNGSI sebagai bagian dari ujian
    # Boleh membuat dictionary baru untuk menyimpan ururan daftar prosentase 
    print("H. Mengurutkan data prosentase pendapatan") 
    kp = []
    for i in dictProsentase:
        kp.append(i)
    for i in range (0, len(dictProsentase)-1):
        for j in range (len(dictProsentase)-1, i, -1):
            if dictProsentase[kp[j]] < dictProsentase[kp[j-1]]:
                dictProsentase[kp[j]], dictProsentase[kp[j-1]] = dictProsentase[kp[j-1]], dictProsentase[kp[j]]

    print(dictProsentase)
    print() # spasi untuk memudahkan penilaian

if __name__=="__main__":
    main()