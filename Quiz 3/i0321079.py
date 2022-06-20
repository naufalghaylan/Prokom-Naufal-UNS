import modul.matrik as matrik
from modul.matrik import *
seed = int
row = int
col = int

def printmatrik(seed, row, col):
    jadi = matrik.buatmatrik(seed, row, col)
    for i in range(len(jadi)):
        print(jadi[i])


def main():
    print("1. Matrik 1")
    print("2. Matrik 2")
    print("3. Masukkan manual")
    print("4. Penjumlahan Matriks")
    x = int(input("Masukkan NIlai= "))
    if x == 1:
        printmatrik(79, 7, 9)
    if x == 2:
        printmatrik(2021, 7, 9)
    if x == 3:
        seed = int(input("seed= "))
        row = int(input("row= "))
        col = int(input("col= "))
        printmatrik(seed, row, col)
    else:
        for i in range(0,len(printmatrik(79, 7, 9))):
            for j in range(0,len(printmatrik(79, 7, 9)[0])):
                print(printmatrik(79, 7, 9)[i][j] + printmatrik(2021, 7, 9)[i][j],end='\t')
        print()

if __name__ =="_main_":
    main()
main()