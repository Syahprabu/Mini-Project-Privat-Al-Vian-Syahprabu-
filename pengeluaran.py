class rekord:
    def __init__(self,tanggal,keterangan,nominal) :
        self.tan = tanggal
        self.ket = keterangan
        self.nom = nominal



data = [
    rekord("01","Sambal Krecek", 3000)
]
anggaran = 3400000
bulan = "Maret"
tahun = 2026

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





