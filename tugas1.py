print("Pilih jenis Operasi ?")
print("A.Pertambahan")
print("B.Pengurangan")
print("C.Perkalian")
print("D.Pembagian")
print("E.Modulus")
print("F.Perpangkatan")



operasi =input(">> ") .upper()

Angka1 = float(input("masuakn angka pertama :"))
Angka2 = float(input("masuakn angka kedua :"))

if operasi =="A" :

    hasil = Angka1 + Angka2
elif operasi =="B" :
    hasil = Angka1 - Angka2   
elif operasi =="C" :
    hasil = Angka1 * Angka2    
elif operasi =="D" :
    hasil = Angka1 / Angka2      
elif operasi =="E" :
    hasil = Angka1 % Angka2
elif operasi =="F" :
    hasil = Angka1 ** Angka2
else : 
    print("Tidak Valid")
    exit() 

print(hasil)
         




