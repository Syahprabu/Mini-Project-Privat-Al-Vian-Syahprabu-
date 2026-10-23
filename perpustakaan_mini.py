buku = []
with open("FileMateri09.csv","a",encoding="utf-8") as ffile :
     pass
with open("FileMateri09.csv","r",encoding="utf-8") as ffile :
    for baris in ffile :
        baris = list(baris.strip().spilt(","))
        baris[2]= int(baris[2])
        buku.append(baris)
       

def tabel():
      
      print("="*56)
      print(f"|{"No.":<5}| {"Judul":^20}| {"Tema":^15}| {"Halaman":<8}|")
      print("="*56)
      for i in range(len(buku)):
            print(f"|{i+1:<5}| {buku[i][0]:^20}| {buku[i][1]:^15}| {buku[i][2]:>8}|")
      print("="*56)


def nambahin():
      global buku
      tabel()
      nama = input("masukan nama buku? ")
      tema = input("masukan tema buku? ")
      halaman = int(input("masukan jumlah halaman? "))
      buku.append([nama,tema,halaman])
      

def edit_bang():
      global buku 
      tabel()
      nomer = int(input ("masukan no yang ingin di edit ? "))
      nama = input("masukan nama buku? ")
      tema = input("masukan tema buku? ")
      halaman = int(input("masukan jumlah halaman? "))
      buku[nomer-1]=([nama,tema,halaman])
      

def hapus():
      global buku
      tabel()
      dihapus = int(input("masukan nomer yang ingin anda hapus ? "))
      buku.pop(dihapus-1)
      

while True:
      tabel()
      pilihan = input("mau apa mas ?\nA.Menambahkan\nB.Edit\nC.Hapus\nD.keluar\n>>").upper()
      if pilihan == "A":
            nambahin()
      elif pilihan == "B":
           edit_bang()
      elif pilihan == "C":
            hapus()
      else :
            with open("FileMateri09.csv","w",encoding="utf-8") as ffile :
             for i in range(len(buku)) :
                  print(buku[i][0] , buku[i][1] , buku[i][2] , sep="," , file=ffile)
            exit()