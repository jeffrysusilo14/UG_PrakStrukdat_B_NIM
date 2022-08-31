def jumlah (x,y):
    return x + y
def kurang (x,y):
    return x - y
def kali (x,y):
    return x * y
def bagi (x,y):
    return x / y

print('1.jumlah')
print('2.kurang')
print('3.kali')
print('4.bagi')

pilih=int(input('masukan pilhan (angkanya ya brooo): '))

bil1=int(input('masukan angka ke 1: '))
bil2=int(input('masukang angka ke 2: '))

if pilih == 1 :
    print(jumlah(bil1,bil2))

elif pilih == 2 :
    print(kurang(bil1,bil2))

elif pilih == 3 :
    print(kali(bil1,bil2))

elif pilih == 4: 
    print(bagi(bil1,bil2))