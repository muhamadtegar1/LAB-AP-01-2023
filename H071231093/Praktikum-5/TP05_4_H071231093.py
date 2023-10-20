def kebalikan(kalimat):
    hasil = kalimat
    kalimat = kalimat.split()
    index_tidak = -1
    index_jelek = -1

    for i, kata in enumerate(kalimat):
        if kata.lower() == "tidak":
            index_tidak = i
        elif kata.lower() == "jelek":
            index_jelek = i

    if index_tidak >= 0 and index_jelek >= 0 and index_tidak < index_jelek:
        awal_kata = kalimat[:index_tidak]
        akhir_kata = kalimat[index_jelek + 1:]
        hasil = " ".join(awal_kata) + " bagus " + " ".join(akhir_kata)

    return hasil

kalimattest = input("Input Kalimat: ")
print(kebalikan(kalimattest))
