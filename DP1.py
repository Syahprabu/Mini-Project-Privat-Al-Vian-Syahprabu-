"""
Tugas Praktikum Dasar Pemrograman 1
Mini SIAKAD (Rapor Mahasiswa)
"""

# 1. INPUT DATA MAHASISWA

nama_mahasiswa = input("Masukkan nama mahasiswa: ")

# List untuk menyimpan tiga nilai tugas
nilai_tugas = []
for i in range(1, 4):
    nilai = float(input(f"Masukkan nilai tugas ke-{i}: "))
    nilai_tugas.append(nilai)

persentase_kehadiran = float(input("Masukkan persentase kehadiran (%): "))

# 2. TOTAL & RATA-RATA NILAI TUGAS (for loop)

total_nilai = 0
for nilai in nilai_tugas:
    total_nilai += nilai

rata_rata_tugas = total_nilai / len(nilai_tugas)

# 3. TUPLE: NAMA MATA KULIAH & SEMESTER

info_mk = ("Dasar Pemrograman", 1)  

# 4. BONUS & NILAI AKHIR

bonus = 0.05 * rata_rata_tugas          
nilai_akhir = rata_rata_tugas + bonus


# 5. STATUS KELULUSAN (boolean)

lulus = nilai_akhir >= 70 and persentase_kehadiran >= 75

# 6. DICTIONARY RINGKASAN RAPOR

rapor = {
    "nama": nama_mahasiswa,
    "mata_kuliah": info_mk[0],
    "semester": info_mk[1],
    "nilai_tugas": nilai_tugas,
    "total_nilai": total_nilai,
    "rata_rata_tugas": round(rata_rata_tugas, 2),
    "bonus": round(bonus, 2),
    "nilai_akhir": round(nilai_akhir, 2),
    "kehadiran (%)": persentase_kehadiran,
    "lulus": lulus,
}

# TAMPILKAN HASIL

print("\n===== RAPOR MAHASISWA =====")
for key, value in rapor.items():
    print(f"{key.replace('_', ' ').capitalize()}: {value}")
print("============================")