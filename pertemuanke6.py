total_nilai = 0
jumlah_data = 0

while True:
    nim = input("Masukkan NIM (atau 'Tidak' untuk berhenti): ")
    
    if nim == 'Tidak':
        print("Looping dihentikan.")
        break
    
    nama = input("Masukkan Nama: ")
    
    
    while True:
        nilai_input = input("Masukkan Nilai: ")
        try:
            nilai = float(nilai_input)
            break
        except ValueError:
            print("Input harus berupa angka! Silakan masukkan ulang.")
    
    total_nilai += nilai
    jumlah_data += 1
    print(f"Data '{nama}' berhasil disimpan.\n")


if jumlah_data > 0:
    rata_rata = total_nilai / jumlah_data
    print(f"\nJumlah nilai: {total_nilai}")
    print(f"Rata-rata nilai: {rata_rata}")
else:
    print("\nTidak ada data yang diinput.")