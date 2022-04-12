#data mahassiwa
mahasiswa = [["Joko Wardoyo", "Jl. Majapahit no 5", 1234567],
             ["Anwar Hidayat", "Jl. Mega Mendung no 7", 2718976],
             ["Desi Anwar", "Jl. Rajawali no 45", 42211123]]
for indeks in range(len(mahasiswa)):
    print("nama mahasiswa %s alamat di %s no telepohone %d" %(mahasiswa[indeks][0],
                                                              mahasiswa[indeks][1],
                                                              mahasiswa[indeks][2]))