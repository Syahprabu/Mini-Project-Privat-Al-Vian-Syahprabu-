while True:
    
    while True:
        tinggi_input = input("Masukkan tinggi segitiga: ")
        if tinggi_input.isdigit():
            n = int(tinggi_input)
            break
        else:
            print("Input harus bilangan bulat! Silakan masukkan ulang.")

    
    print()
    for i in range(1, n + 1):
        spasi = " " * (n - i)
        bintang = "*" * (2 * i - 1)
        print(spasi + bintang)
    print()

    
    while True:
        pilihan = input("Buat segitiga lagi? (Y = ya, T = tidak): ").upper()
        
        posisi_y = pilihan.find('Y')
        posisi_t = pilihan.find('T')

        if posisi_y == -1 and posisi_t == -1:
            print("Pilihan tidak dikenali! Masukkan lagi input yang mengandung 'Y' atau 'T'.")
            continue

        if posisi_y != -1 and (posisi_t == -1 or posisi_y < posisi_t):
            
            break  
        else:
            
            print("Program selesai.")
            exit_program = True
            break
    
    if 'exit_program' in locals() and exit_program:
        break

    