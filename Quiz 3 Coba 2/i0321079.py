def buatmatrik(nilaiseed, row, col):
    #"membuat matrik"
    global MA
    import random
    MA = [0] * row
    random.seed(nilaiseed)
    for baris in range(row):
        print("[", end =" ")
        MA[baris] = [0] * col
        for j in range(col):
            MA[baris][j] = random.randrange(1,100)
            mat = MA[baris][j]
            print(mat, end=" ")
        print("]")

    return MA


def penjumlahanbaris (baris,col):
    print("INI HASIL Matriks 1 dan Matriks 2")
    print("Matriks 1 =")
    MA1=buatmatrik(21,7,9)
    print("Matriks 2 =")
    MA2=buatmatrik(79,7,9)
    print("")
    print("")
    print("========HASIL PENJUMLAHAN BARIS =====")
    for i in range (col):
        hjb = MA1[baris][i]+ MA2[baris][i]
        print (hjb, end=" ")
    print("")

def penjumlahankolom (baris,col):
    print("INI HASIL MA1 dan MA 2")
    print("MA 1 =")
    MA1=buatmatrik(21,7,9)
    print("MA 2 =")
    MA2=buatmatrik(79,7,9)
    print("")
    print("")
    print("HASIL PENJUMLAHAN KOLOM =====")
    for i in range (baris):
        hjk = MA1[i][col]+ MA2[i][col]
        print (hjk, end=" ")

def penjumlahanmatrik():
    print("INI HASIL MA1 dan MA 2")
    print("MA 1 =")
    MA1=buatmatrik(21,7,9)
    print("MA 2 =")
    MA2=buatmatrik(96,7,9)
    print("")
    print("")
    for i in range(0,len(MA1)):
        for j in range(0,len(MA1[0])):
            print(MA1[i][j] + MA2[i][j],end='\t')
        print()


def main():
    print("")
    p = str(input("Pilih Matriks 1 atau 2= "))
    if p == "1":
        buatmatrik(21,7,9)
    elif p == "2":
        buatmatrik(79,7,9)
    print("")
    pb1 = int(input("Pilih Baris Ke Berapa (1)= "))
    pb2 = int(input("Pilih Baris Ke Berapa (2)= "))
    print("")
    penjumlahanbaris (pb1,pb2)
    print()
    pk1 = int(input("Pilih Kolom Ke Berapa (1)= "))
    pk2 = int(input("Pilih Kolom Ke Berapa (1)= "))
    penjumlahankolom (pk2,pk1)
    penjumlahanmatrik()
    return
if __name__== "__main__":
    main()