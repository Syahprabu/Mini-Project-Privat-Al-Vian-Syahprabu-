list_menu =[["Nasi Goreng",12000],["Mie Goreng",13000]]

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