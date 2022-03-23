totalbelanja = int(input("Masukkan total belanja anda= Rp "))
print("=========================")
member= int(input("Apakah anda member? Jika anda member ketik 1, jika tidak ketik 0 = "))
print("=========================")
if member == 1 :
    if totalbelanja>500000:
        totalbelanja= totalbelanja-(totalbelanja*0.25)
    elif totalbelanja>100000:
        totalbelanja= totalbelanja-(totalbelanja*0.20)
    else :
        totalbelanja= totalbelanja-(totalbelanja*0.10)
else:
    if totalbelanja>100000 :
        totalbelanja= totalbelanja-(totalbelanja*0.10)
print(totalbelanja)
