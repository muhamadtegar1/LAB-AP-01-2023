harga = int(input('Harga Barang: '))
uang = int(input('Uang: '))

kembalian = uang - harga  # Menghitung kembalian uang

if kembalian >= 0:
        print('Kembalian Anda: ')
else:
        print('Uang Tidak Cukup')

uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
jumlah = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(uang_pecahan)):
    if kembalian >= uang_pecahan[i]: 
        jumlah[i] = kembalian // uang_pecahan[i]
        kembalian = kembalian % uang_pecahan[i]

for i in range(len(jumlah)): 
    print(f'{jumlah[i]} Uang sejumlah Rp.{uang_pecahan[i]}')