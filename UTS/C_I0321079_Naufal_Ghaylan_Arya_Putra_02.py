def CC():
    h=250000000
    um=h*0.10
    b= h*0.05
    t=12
    print("{:<13} {:<6} {:<14} {:<15}"
    .format("Jenis Mobil", "Tenor", "Uang Muka", "Angsuran Bulanan"))
    print("-----------------------------------------------------------------")
    while t <=60:
        appb=h/t
        apb=appb+b
        print("{:<13} {:<6} {:<14} {:<15}"
    .format("City Car", t, um, apb))
        t= t + 12

def MPV():
    hm=350000000
    umm=hm*0.10
    bm= hm*0.05
    tm=12
    print("{:<13} {:<6} {:<14} {:<15}"
    .format("Jenis Mobil", "Tenor", "Uang Muka", "Angsuran Bulanan"))
    print("-------------------------------------------------------1----------")
    while tm <=60:
        appbm=hm/tm
        apbm=appbm+bm
        print("{:<13} {:<6} {:<14} {:<15}"
    .format("MPV", tm, umm, apbm))
        
        tm= tm + 12
    
jm = int(input("Masukkan Jenis Mobil (City Car = 1, MPV = 2) = "))
print("=====================================================================")
if jm  == 1 :
    CC()
else: 
    MPV()