list_menu =[["Nasi Goreng",12000],
            ["Mie Goreng",13000],
            ["Bakso",15000],
            ["Iga Bakar",20000],
            ["Es Teh",3000],
            ["Es Jeruk",5000],
            ["Es Kampul",4000]]
list_pesenan = [
    ["Nasi Goreng",3],
    ["Es Teh",5]
]

header1 = "No."
header2 = "Menu"
header3 = "Harga"

print("+-" + "-"*3 + "---" + "-"*25 + "---" + "-"*10 + "-+")
print("| " +header1+ " "*(3-len(header1)) + " | " +header2+ " "*(25-len(header2)) + " | " +header3+ " "*(10-len(header3)) + " |")
print("+-" + "-"*3 + "---" + "-"*25 + "---" + "-"*10 + "-+")
counter = 0
while counter < len (list_menu):
    nomor = str(counter+1)
    menu = list_menu[counter][0]
    harga = f"{list_menu[counter][1]:,}"
    print("| " + " "*(3-len(nomor)) +nomor+ " | " +menu+ " "*(25-len(menu)) + " | Rp" + " "*(8-len(harga)) +harga+  " |")
    counter += 1
print("+-" + "-"*3 + "---" + "-"*25 + "---" + "-"*10 + "-+")

print("List Pesanan ? ")


# counter = 0

# while counter <  len(list_pesanan) :
# print (list_pesenan)

print("-"*48)
print("Mau ngapain bang ?\n","A.Tambah Pesanan\n","B.Edit Pesanan\n","C.Hapus Pesanan\n","D.Bayar pesanan\n","E.Keluar\n")
milih=input(">>")
# match pesana :
#     case  "A" :
#         hasil = 
