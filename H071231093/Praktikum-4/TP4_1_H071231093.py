def permutasi_kata(kata):
    try:
        hasil = ''
        for i in range(len(kata)):
            kata_mutasi = kata[-1] + kata[:-1]
            hasil = hasil + kata_mutasi + ' | '
            kata = kata_mutasi
        return hasil
    
    except TypeError as pesan:
        return 'Terjadi Kesalahan: ' + str(pesan)

kata_input = input('Masukkan sebuah kata: ')
print(f'String Permutation({kata_input})')
print(permutasi_kata(kata_input))
