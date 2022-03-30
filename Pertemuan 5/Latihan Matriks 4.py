print("======================")
matriksA= [[2,2,2],
           [3,3,3],
           [4,4,4]]
matriksB= [[1,2,3],
           [5,1,7],
           [2,9,1]]
matriksC=[]

print("===================")
print("Mulai mengkali dua matriks:")

for x in range (0, len(matriksA)):
    print()
    baris=[]
    for y in range(0, len(matriksA[0])):
        total=0
        for z in range(0, len(matriksA)):
            total = total + (matriksA[x][z] * matriksB[z][y])
        baris.append(total)
    matriksC.append(baris) 
print("===================")

for x in range(0, len(matriksC)):
    for y in range(0, len(matriksC)):
        print(matriksC[x][y], end="   ")
    print()