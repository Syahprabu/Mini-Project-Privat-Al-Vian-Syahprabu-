buku=[]
wra 
def tabellll(data):
    print("="*55)
    print(f"| {"No":^3} | {"NAMA BUKU":^45} |")
    print("="*55)
    for i in range(len(data)):
        print(f"| {i+1:^3} | {data[i]:<45} |")
    print("="*55)

while True:
    tabellll(data=buku)
    print("mau ngapain di sini ?")
    print("A.nambah buku ")
    print ("B.menghapus no buku")
    print ("C.edit")
    print("D.keluar")
    pilihan = input(">> ").upper()

    if pilihan == "A":
        nama = input("masukan nama buku : ")
        buku.append(nama)
    elif pilihan == "B":
        nomer = int(input("masukan no yang ingin di hapus :"))
        buku.pop(nomer-1) 
    elif pilihan == "C":
        edit = int(input("masukan no yang ingin di edit ? "))
        baru = input("nama buku baru ? ")
        buku[edit-1]= baru
        
    else : 
        exit()

    

    