matriksB= [[1,2,3],
           [5,1,7],
           [2,9,1]]
print(matriksB)
matriksA= [[1,2],
           [3,4]]
print(matriksA)

print("======================")
print("Mencetak Matriks Kotak")

for x in range (0, len(matriksB)):
    print()
    for y in range(0, len(matriksB[0])):
        print(matriksA[x][y]+matriksB[x][y], end="  ")
    print()
print("======================")

