# Operasi pada List, Set, dan String
# len()
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
print(len(contoh_list))

contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(contoh_list)
print(len(contoh_list))

contoh_string = "Belajar Python"
print(contoh_string)
print(len(contoh_string))

# min() dan max()
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

# Count
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

# In dan Not In
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

# Memberikan Nilai untuk Multiple Variable
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]

data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

# Sort
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)

# Anda dapat membalikkan urutan dengan cara berikut
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)

# Metode sort menggunakan urutan ASCII sehingga nilai huruf 
# kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)