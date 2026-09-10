print("Pilih jenis Operasi ?")
print("A.Pertambahan")
print("B.Pengurangan")
print("C.Perkalian")
print("D.Pembagian")
print("E.Modulus")
print("F.Perpangkatan")



operasi =input(">> ") .upper()

    
if operasi =="A" :
    Angka1 = float(input("masuakn angka pertama :"))
    Angka2 = float(input("masuakn angka kedua :"))
    hasil = Angka1 + Angka2
    
elif operasi =="B" :
    Angka1 = float(input("masuakn angka pertama :"))
    Angka2 = float(input("masuakn angka kedua :"))
    hasil = Angka1 - Angka2  

elif operasi =="C" :
    Angka1 = float(input("masuakn angka pertama :"))
    Angka2 = float(input("masuakn angka kedua :"))   
    hasil = Angka1 * Angka2 

elif operasi =="D" :
    Angka1 = float(input("masuakn angka pertama :"))
    Angka2 = float(input("masuakn angka kedua :"))   
    hasil = Angka1 / Angka2    
  
elif operasi =="E" :
    Angka1 = float(input("masuakn angka pertama :"))
    Angka2 = float(input("masuakn angka kedua :"))  
    hasil = Angka1 % Angka2
elif operasi =="F" :
    Angka1 = float(input("masuakn angka pertama :"))
    Angka2 = float(input("masuakn angka kedua :"))  
    hasil = Angka1 ** Angka2
else : 
    print("Tidak Valid")
    exit() 

print(hasil)
         




