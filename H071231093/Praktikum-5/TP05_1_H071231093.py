def mix_string(s1, s2):
    s2 = s2[::-1]  
    mixed = min(len(s1), len(s2))
    hasil = ''

    for i in range(mixed):
        hasil = hasil + s1[i] + s2[i]

    if len(s1) > len(s2):
        hasil = hasil + s1[mixed:]
    elif len(s2) > len(s1):
        hasil = hasil + s2[mixed:]

    return hasil

s1 = input('s1 = ')
s2 = input('s2 = ')

hasil = mix_string(s1, s2)
print(f'Hasil Mixed = "{hasil}"')
