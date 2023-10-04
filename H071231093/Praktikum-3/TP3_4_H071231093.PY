nilai = int(input('Masukan nilai:  '))

while True:
    tanda_minus = ("----------------------")
    print(tanda_minus)
    print("Menu:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Hasil")

    pilihan = int(input("Pilih Menu: "))
    tanda_minus = ("----------------------")
    print(tanda_minus)

    if pilihan == 1:
        angka = float(input("Masukkan Nilai: "))
        nilai += angka
    elif pilihan == 2:
        angka = float(input("Masukkan Nilai: "))
        nilai -= angka
    elif pilihan == 3:
        angka = float(input("Masukkan Nilai: "))
        nilai *= angka
    elif pilihan == 4:
        angka = float(input("Masukkan Nilai: "))
        if angka != 0:
            nilai /= angka
        else:
            print("Tidak bisa dibagi 0")
    elif pilihan == 5:
        print("Hasil adalah", nilai)
        break
    else:
        print("Menu Tidak Tersedia")