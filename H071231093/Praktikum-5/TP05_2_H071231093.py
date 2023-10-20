def ini_string_baru(kata):
    if len(kata) < 3:
        return "string terlalu pendek, min. 3 huruf"
    else:
        pertama = kata[0]
        if len(kata) % 2 == 0:  
            tengah = kata[len(kata) // 2 - 1 : len(kata) // 2 + 1]  
        else:  
            tengah = kata[len(kata) // 2] 
        akhir = kata[-1]
        hasil = pertama + tengah + akhir
        return hasil

string_baru = input("Masukkan string: ")
hasil = ini_string_baru(string_baru)
print("String baru dibuat:", hasil)