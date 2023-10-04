# Memasukan input
n = int(input('Masukkan nilai: '))

# Dua suku pertama deret fibonacci
s1 = 0
s2 = 1

if n <= 0:
    print('Invalid Data')
elif n == 1:
    print('0')
else:
    for i in range(n):
        print(s1, end=('2')) 
        angka_selanjutnya = s1 + s2
        s1 = s2                      #angka diperbarui
        s2 = angka_selanjutnya       #angka diperbarui