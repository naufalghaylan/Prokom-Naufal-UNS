#data mahassiwa
mahasiswa = [["Joko Wardoyo", "Jl. Majapahit no 5", 1234567],
             ["Anwar Hidayat", "Jl. Mega Mendung no 7", 2718976],
             ["Desi Anwar", "Jl. Rajawali no 45", 42211123]]
#fungsi format alamat rumah
alamat_mahasiswa = '''
                    nama mahasiswa  =  \t:{0},
                    alamat rumah    =  \t:{1},
                    no telephone    =  \t"{2},
                    '''

print("Daftar Mahaswaa TI UNS")
print("============================")
for indeks in range(len(mahasiswa)):
    print (alamat_mahasiswa.format(mahasiswa[indeks][0],
                                    mahasiswa[indeks][1],
                                    mahasiswa[indeks][2]))