matriksB= [[1,2,3],
           [5,1,7],
           [2,9,1]]
print(matriksB)

print("======================")
print("Mencetak Matriks Kotak")

for x in range (0, len(matriksB)):
    print()
    for y in range(0, len(matriksB[0])):
        print(matriksB[x][y], end="  ")
    print()
print("======================")

