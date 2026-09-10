print("Kalkulator Sederhana\n","A.Pertambahan\n","B.Pengurangan\n","C.Perkalian\n","D.Pembagian\n")

operasi = input(">>").upper()
angka1 = float(input ("masukan 1 : "))
angka2 = float(input ("masukan 2 : "))

if  operasi =="A" :
    hasil = angka1 + angka2
elif operasi == "B" :
    hasil = angka1 - angka2    
elif operasi == "C" :
    hasil = angka1 * angka2     
elif operasi == "D" :
    hasil = angka1 / angka2
else :
    print("Tidak ada")
    exit()
print(hasil)                   
