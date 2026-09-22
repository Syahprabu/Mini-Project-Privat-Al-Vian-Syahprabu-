panjang = int(input("Masukkan Panjang :"))

counter1 = 1
while counter1 <= panjang*2 :
    if counter1 == panjang*2:
        counter2 = 1
        while counter2 <= panjang:
            print("* ",end="")
            counter2 += 1
    else:
        print("* ")
    counter1 += 1    
