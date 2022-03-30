from operator import le
print(range(9))
print("==================")
kelas = ['Ali', 'Budi', 'Caca','Dinda', 'Elo', 'Bayu', "Adi", 'Nina']

kelas.append("Siska")
kelas.append("Maya")
kelas.insert(3, "Zasa")


print(kelas[4])
print(kelas[0])

print (len(kelas))
print("==================")
for i in range (0, len(kelas)):
    print("no murid =", i, "  ", kelas[i])
print("==================")