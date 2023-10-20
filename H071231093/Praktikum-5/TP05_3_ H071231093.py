def anagram(kata1, kata2):
    kata1 = kata1.lower().replace(' ', '')
    kata2 = kata2.lower().replace(' ', '')

    for huruf in kata1:
        hasil1 = kata1.count(huruf)
        hasil2 = kata2.count(huruf)
        if hasil1 == hasil2:
            continue
        else:
            return False

    if hasil1 == hasil2:
        return True

kata1 = input('Masukkan Kata Pertama: ')
kata2 = input('Masukkan Kata Kedua: ')

if anagram(kata1, kata2):
    print("True")
else:
    print("False")