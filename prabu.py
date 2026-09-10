print("kakulator")
print("A.tamabah")
print("B.kurang")
print("C.kali")
print("D.bagi")

operasi = input(">>") .upper()

angka1 = float(input ("masukan 1 : "))
angka2 = float(input ("masukan 2 : "))

if operasi =="A" :
    hasil = angka1 + angka2
elif operasi =="B" :
    hasil = angka1 - angka2
elif operasi =="C" :
    hasil = angka1 * angka2 
elif operasi =="D" :
    hasil = angka1 / angka2    
else : 
    print("tidak ada") 
    exit()
print(hasil)
       
    
