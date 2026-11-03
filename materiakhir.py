class rekord:
    def __init__(self,tanggal,keterangan,nominal) :
        self.tan = tanggal
        self.ket = keterangan
        self.nom = nominal



data = [

]
anggaran = 0
bulan = None
tahun = None

def tabel() :
    global data
    global anggaran
    global bulan
    global tahun
    anggaran_sisa = anggaran
    print("="*75)
    print(f"{f"catatan pengluaran bulan {bulan} tahun {tahun}":^75}")
    print("="*75)
    print(f"Anggaran Bulan Ini = Rp {anggaran:,}")
    print("="*75)
    print(f"| {"No.":^5} | {"Tanggal":^7} | {"Keterangan":^40} | {"Nominal":^11}|")
    print("="*75)
    for i in range(len(data)) :
        print(f"| {i+1:^5} | {data[i].tan:^7} | {data[i].ket:<40} | Rp {data[i].nom:^8,}|")
        anggaran_sisa -= data[i].nom
    print("="*75)
    print(f"Sisa Anggaran = Rp {anggaran_sisa:,}")
tabel()

def bulan_tahun():
    global bulan,tahun
    while True:
        bulan = input("masukan bulan ? ").capitalize()
        if bulan not in ["Januari","Februaru","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"] :
            print("Bulan Wajib Menggunaka Bahasa Indonesia")
        else :
            break

    while True:
        try :
            tahun = int(input("masukan tahun : "))
            break
        except ValueError :
            print("Tahun wajib Menggunakan Bilangan Bulat")

def load_data():
    global data,bulan,tahun,anggaran
    filename = f"Pengeluaran {bulan} {tahun}.csv"
    try:
        with open(filename,"r",encoding = "utf-8") as f:
            is_first = True
            for baris in f :
                if is_first:
                    anggaran = int(baris)
                    is_first = False
                    continue
                barisa = list(baris.split(","))
                baris[2] = int(baris[2])
                data.append(rekord(baris[0],baris[1],baris[2]))
    except FileNotFoundError :
        while True:
            try:
                anggaran = int(input("masukan anggaran untuk bulan ini : "))
                break
            except ValueError :
                print("Anggaran Wajib nominal !")
        with open(filename,"w",encoding = "utf-8")as f :
            print(anggaran,file = f)     

def tambah_data():
    tabel()
    while True:
        tanggal = input("Masukan Tanggal\t\t: ")
        try :
            if int (tanggal)< 1 or int(tanggal)>31:
                print("Tanggal harus di antara 1 sampai 31 !!!")
            else : 
                break
        except ValueError:
            print("Tanggal wajib berupa angka !!")
    keterangan = input("Masukan Keterangan\t\t: ")
    if len(keterangan) >40 :
        keterangan = keterangan[:40:]
    while True :
        try :
            nominal = int(input("masukan nominal Pengeluaran\t: "))
            break
        except ValueError:
            print("Nominal Pengeluaran Wajib berupa Angka Tanpa titik / koma")
    data.append(rekord(tanggal,keterangan,nominal))

def edit_data():
    global data
    tabel()
    try :
        indeks = int(input("Masukan nomer baris yang akan di edit : "))
        if indeks < 1 or indeks > len(data):
            print("baris tidak di temukan !!")
            return
    except ValueError:
        print("Indeks wajib menggunakan angka ")
        return
    while True:
        tanggal = input("Masukan Tanggal\t\t: ")
        try :
            if int (tanggal)< 1 or int(tanggal)>31:
                print("Tanggal harus di antara 1 sampai 31 !!!")
            else : 
                break
        except ValueError:
            print("Tanggal wajib berupa angka !!")
    keterangan = input("Masukan Keterangan\t\t: ")
    if len(keterangan) >40 :
        keterangan = keterangan[:40:]
    while True :
        try :
            nominal = int(input("masukan nominal Pengeluaran\t: "))
            break
        except ValueError:
            print("Nominal Pengeluaran Wajib berupa Angka Tanpa titik / koma")
        data[indeks - 1] = rekord(tanggal,keterangan,nominal)


def hapus_data():
    global data
    tabel()
    try :
        indeks = int(input("Masukan nomer baris yang akan di edit : "))
        if indeks < 1 or indeks > len(data):
            print("baris tidak di temukan !!")
            return
    except ValueError:
        print("Indeks wajib menggunakan angka ")
        return
    data.pop (indeks-1)

def tambah_anggaran():
    global anggaran
    tabel()
    try: 
        tambahan = int(input("masukan nominal penambahan anggaran : "))
        anggaran += tambahan
    except ValueError :
        print("anggran wajib menggunakan bilangan bulat !")


def edit_anggaran():
    global anggaran
    tabel()
    try: 
        tambahan = int(input("masukan nominal anggran yang baru : "))
        anggaran = tambahan
    except ValueError :
        print("anggran wajib menggunakan bilangan bulat !")
    

def save_data():
    global anggaran,data,bulan,tahun
    filename = f"pengeluaran {bulan} {tahun}.csv"
    with open(filename,"w",encoding = "utf-8")as f :
        print(anggaran,file = f)
        for i in data :
            print(i.tan , i.ket , i.nom ,sep=",",file = f)


    
bulan_tahun()
load_data()
while True:
    tabel()
    print("Mau Ngapaig Bang ?\n","A. Tambahin Data\n","B. Edit Data\n","C. Hapus Data\n","D. Tambah Anggaran\n","E. Edit Anggaran\n","F. Ganti Bulan/Tahun\n","G. Keluar\n")
    pilihan = input(">> ").upper()

    if pilihan =="A":
        tambah_data()
    elif pilihan == "B":
        edit_data()
    elif pilihan == "C":
        hapus_data()
    elif pilihan == "D":
        tambah_anggaran()
    elif pilihan == "E":
        edit_anggaran()
    elif pilihan == "F":
        save_data()
        bulan_tahun()
        load_data()
    elif pilihan == "G":
        save_data()
        exit()
    else:
        print("Pilihan tidak Valid ")
        input("Tekan enter Untuk Lanjutkan......")
