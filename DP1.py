nama = input("Masukkan nama mahasiswa: ")
nilai = []

#looping input nilai
for i in range (3) :
    nilai_input = float(input(f"Masukkan nilai ke - {i + 1} : "))
    nilai.append(nilai_input)

kehadiran = float(input("Masukkan persentase kehadiran (%) : "))

total = 0
for i in nilai :
    total += i
    print(f"total : {total}")
    rata = total / len(nilai)

matkul = input("Masukkan mata kuliah: ")
semester = int(input("Masukkan semester: "))

matkul_semester = (matkul,semester)

bonus = rata * 0.05

nilai_akhir = rata + bonus

if nilai_akhir > 100 :
    nilai_akhir =100

if nilai_akhir >= 70 and kehadiran >= 75:
    status_lulus = True
else :
    status_lulus= False

ringkasan ={
    "Nama" : nama , 
    "Mata Kuliah" : matkul_semester,
    "Persentase Kehadiran" : f"{kehadiran:.0f} %",
    "Nilai Akhir" : nilai_akhir,
    "Lulus" : status_lulus
}

print(ringkasan)