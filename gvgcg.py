print("kalkulator suhu\n","A.celcius\n","B.Reamur\n","C.Fahremheit\n","D.Kelvin\n")

nilai = input(">>").upper()

suhu1=float(input("masukan suhu awal ?"))

match nilai :
    case "A" :
        hasil = suhu1/5
    case "B" :
        hasil = suhu1/4
    case "C" :
        hasil = (suhu1-32)/9
    case "D" :
        hasil = (suhu1-273)/5 
    case _ :
        print("Gak Masuk Case")           

print("Pilih Satuan Suhu Akhir :\n","A.celcius\n","B.Reamur\n","C.Fahrenheit\n","D.Kelvin\n")
jawaban = input(">>").lower()

match jawaban:
    case "a" :
        jawablah = hasil * 5
    case "b" :
        jawablah = hasil * 4
    case "c" :
        jawablah= hasil *9+32
    case "d":
        jawablah= hasil *5 + 273

print (jawablah)   
        