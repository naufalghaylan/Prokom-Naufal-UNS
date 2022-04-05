def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

nilai = int(input("Masukkan nilai untuk difaktorialkan = "))
print("------------------")
print("Nilai faktorial dari ", nilai, "adalah = ", faktorial(nilai))
print("-------------------------")