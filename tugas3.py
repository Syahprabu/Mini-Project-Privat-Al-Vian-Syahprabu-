print ("Pilih Suhu :\n","A.celcius\n","B.Reamur\n","C.Fahrenheit\n","D.Kelvin\n")

suhu = input(">>")

suhu1 = float(input("Masukan nominal suhu awal :"))

if suhu =="A":
    hasil = suhu1 / 5 
elif suhu =="B" :
    hasil = suhu1 /4
elif suhu =="C":
    hasil = (suhu1 - 32)/9
elif suhu =="D": 
    hasil = (suhu1 - 273)/5

print ("Pilih Satuan Suhu Akhir :\n","A.celcius\n","B.Reamur\n","C.Fahrenheit\n","D.Kelvin\n")
suhu = input(">>")

if suhu =="A":
    hasil = hasil * 5 
elif suhu =="B" :
    hasil = hasil * 4
elif suhu =="C":
    hasil = (hasil + 32)*9
elif suhu =="D": 
    hasil = (suhu1 + 273)*5


print(hasil)
