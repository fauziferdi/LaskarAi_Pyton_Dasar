# Mengubah Huruf Besar/Kecil
# upper()
kata = "dicoding"
kata = kata.upper()
print(kata)

# lower()
kata = "DICODING"
kata = kata.lower()
print(kata)

# Awalan dan Akhiran
# rstrip()
print("Nama saya           ".rstrip())

#Istrip()
print("           Nama saya".lstrip())

#strip()
print("                  Nama saya                ".strip())

# Jika ingin menghilangkan karakter selain whitespace,
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

# startswith()
print('Dicoding Indonesia'.startswith('Dicoding'))

# endswith()
print('Dicoding Indonesia'.endswith('Indonesia'))


# Memisah dan Menggabung String
# join()
print(' '.join(['Dicoding','Indonesia', '!']))
print('123'.join(['Dicoding','Indonesia']))

# split()
print('Dicoding Indonesia !'.split())
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

# Mengganti Elemen String
# replace()
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

# Pengecekan String
# isupper()
kata = "DICODING"
kata = kata.isupper()
print(kata)

# islower()
kata = "dicoding"
kata = kata.islower()
print(kata)

# isalpha()
kata = "dicoding123"
kata = kata.isalpha()
print(kata)

# isalnum()
kata = "dicoding123"
kata = kata.isalnum()
print(kata)

# isdecimal()
kata = "12345"
kata = kata.isdecimal()
print(kata)

# isspace()
kata = "   "
kata = kata.isspace()
print(kata)

# istitle()
kata = "Dicoding Python"
kata = kata.istitle()
print(kata)

# Formatting pada String
# zfill()
teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number)

# rjust()
print('Dicoding'.rjust(20))

# ljust()
print('Dicoding'.ljust(20))

# center()
print('Dicoding'.center(20))

# String Literals
st1 = "Jum'at"
st1 = 'Jum\'at'
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")

# Raw String
print(r'Dicoding\tIndonesia')