print("Pilih jenis Operasi ?")
print("A.Persegi Panjang")
print("B.Segitiga")

operasi =input(">> ") .upper()

Angka1 = float(input("Masukan Nominal 1 :"))
Angka2 = float(input("Masukan Nominal 2 :"))

if operasi =="A" : 
    hasil = Angka1 * Angka2
elif operasi =="B" :
    hasil = 1/2 * Angka1 * Angka2  
else : 
    print("Tidak Valid")
    exit() 

print(hasil)
