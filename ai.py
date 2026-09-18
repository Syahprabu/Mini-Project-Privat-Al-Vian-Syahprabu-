import os

menu = {
    1: ("Nasi Goreng", 12000),
    2: ("Bakmi Goreng", 14000),
    3: ("Kwetiaw Goreng", 14000),
    4: ("Capcay Goreng / Kuah", 15000),
    5: ("Es Teh / Panas", 3000),
    6: ("Es Teh Kampul / Panas", 4000),
}

pesanan = []  # list of [no_menu, jumlah]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_menu():
    print("+" + "-" * 55 + "+")
    print("| No. | Menu                    | Harga           |")
    print("+" + "-" * 55 + "+")
    for no, (nama, harga) in menu.items():
        print(f"|  {no:<2} | {nama:<23} | Rp {harga:>10,} |")
    print("+" + "-" * 55 + "+")


def tampilkan_pesanan():
    print("\nList Pesanan :")
    if not pesanan:
        print("(Belum ada pesanan)")
    else:
        for i, (no_menu, jumlah) in enumerate(pesanan, start=1):
            nama = menu[no_menu][0]
            print(f"{i}. {jumlah} {nama}")
    print("-" * 55)


def tambah_pesanan():
    try:
        no_menu = int(input("Masukkan No. Menu: "))
        if no_menu not in menu:
            print("Menu tidak ditemukan!")
            return
        jumlah = int(input("Jumlah: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return
        pesanan.append([no_menu, jumlah])
        print("Pesanan ditambahkan.")
    except ValueError:
        print("Input tidak valid!")


def edit_pesanan():
    if not pesanan:
        print("Belum ada pesanan untuk diedit.")
        return
    tampilkan_pesanan()
    try:
        idx = int(input("Pilih nomor pesanan yang ingin diedit: ")) - 1
        if idx < 0 or idx >= len(pesanan):
            print("Nomor pesanan tidak valid!")
            return
        jumlah_baru = int(input("Jumlah baru: "))
        if jumlah_baru <= 0:
            print("Jumlah harus lebih dari 0!")
            return
        pesanan[idx][1] = jumlah_baru
        print("Pesanan diperbarui.")
    except ValueError:
        print("Input tidak valid!")


def hapus_pesanan():
    if not pesanan:
        print("Belum ada pesanan untuk dihapus.")
        return
    tampilkan_pesanan()
    try:
        idx = int(input("Pilih nomor pesanan yang ingin dihapus: ")) - 1
        if idx < 0 or idx >= len(pesanan):
            print("Nomor pesanan tidak valid!")
            return
        dihapus = pesanan.pop(idx)
        print(f"Pesanan '{menu[dihapus[0]][0]}' dihapus.")
    except ValueError:
        print("Input tidak valid!")


def bayar_pesanan():
    if not pesanan:
        print("Belum ada pesanan untuk dibayar.")
        return
    tampilkan_pesanan()
    total = sum(menu[no_menu][1] * jumlah for no_menu, jumlah in pesanan)
    print(f"Total Bayar: Rp {total:,}")
    konfirmasi = input("Konfirmasi pembayaran? (y/n): ").strip().lower()
    if konfirmasi == "y":
        print("Pembayaran berhasil. Terima kasih!")
        pesanan.clear()
        input("\nTekan Enter untuk kembali...")
    else:
        print("Pembayaran dibatalkan.")


def main():
    while True:
        clear()
        tampilkan_menu()
        tampilkan_pesanan()
        print("Mau Ngapain Bang?")
        print("A. Tambah Pesanan")
        print("B. Edit Pesanan")
        print("C. Hapus Pesanan")
        print("D. Bayar Pesanan")
        print("E. Keluar")
        pilihan = input(">> ").strip().upper()

        if pilihan == "A":
            tambah_pesanan()
        elif pilihan == "B":
            edit_pesanan()
        elif pilihan == "C":
            hapus_pesanan()
        elif pilihan == "D":
            bayar_pesanan()
        elif pilihan == "E":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid!")

        if pilihan != "D":
            input("\nTekan Enter untuk lanjut...")


if __name__ == "__main__":
    main()