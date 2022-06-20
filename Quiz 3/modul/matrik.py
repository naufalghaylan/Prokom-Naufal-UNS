def printmatrik(var):
    for i in range(0,len(var)):
        for j in range(0,len(var)):
            print(var[i][j],end='\t')
        print()

def buatmatrik(nilaiseed, row, col):
    "membuat matrik"
    import random
    MA = [0] * row
    random.seed(nilaiseed)
    for baris in range(row):
        MA[baris] = [0] * col
        for j in range(col):
            MA[baris][j] = random.randrange(1,100)
    return MA

def main():
    matriks1 = buatmatrik(2021,7,9)
    matriks2 = buatmatrik(92,7,9)
    print("MATRIKS 1")
    printmatrik(matriks1)
    print()
    print('MATRIKS 2')
    printmatrik(matriks2)
    print()
    print("Penjumlahan Matriks")
    for i in range(0,len(matriks1)):
        for j in range(0,len(matriks1[0])):
            print(matriks1[i][j] + matriks2[i][j],end='\t')
        print()

    return
if __name__=="__main__":
	main