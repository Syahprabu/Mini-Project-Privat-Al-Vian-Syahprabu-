panjang =int(input("Masukkan Panjang ?"))
lebar = int (input("Masukkan Lebar ?"))

counter1 = 1
while counter1 <= panjang :
    counter2 = 1
    kosong = ""
    while counter2 <= lebar: 
        if counter1 == 1 or counter1 == panjang or counter2 == 1 or counter2 == lebar:
            kosong  += "* "
        else:
            kosong += "  "
        counter2 += 1
    print(kosong)
    counter1 += 1     



