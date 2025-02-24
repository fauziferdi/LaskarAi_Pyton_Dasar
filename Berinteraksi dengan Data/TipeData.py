
#Numbers

x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))


# tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah

var =10
print(var)
print(id(var))

var = 11
print(var)
print(id(var))

print("========")



#Boolean

x = True
print(type(x))

x = False
print(type(x))

print("========")


#String

x = 'Dicoding'
print(type(x))


# Anda dapat menggunakan tiga single quote atau double quote untuk menyimpan string yang lebih dari satu baris (multi-line).

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)


# String merupakan urutan karakter yang setiap karakternya memiliki indeks. 
# Anda dapat mengakses setiap karakter dari string (substring) dengan menggunakan metode indexing. 
# Perlu diingat bahwa indeks selalu dimulai dari 0. Namun, Anda tidak dapat mengubah substring di dalamnya. Ini dikarenakan string pada Python bersifat immutable.

x = 'Dicoding'
print(x[0])

# Anda dapat mengakses beberapa substring dengan menggunakan metode indexing dan slicing.

x = 'Dicoding'
print(x[2:])

# Anda dapat menampilkan teks/string berdasarkan input dari pengguna dengan berbagai cara
# 1 Formatted String
name = "Perseus Evans"
print(f"Hello, nama saya {name}")

# 2 %-formatting
name = "Perseus Evans"
print("Hello, nama saya %s" % name)

# 3 str.format()
name = "Perseus Evans"
print("Hello, Nama saya {}".format(name))
print("========")

# Tipe Data Collection
# List
# List merupakan jenis kumpulan data terurut (ordered sequence) dan salah satu tipe data yang sering digunakan pada Python.

x = [1, 2.2, 'Dicoding']
print(type(x))

# Setiap data atau elemen dalam list memiliki indeks yang selalu dimulai dari 0.
x = [1, 'Dicoding', True, 1.0]
print(x[2])

# List Python bersifat mutable yang artinya nilai di dalamnya dapat diubah.
x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

# Konsep indexing merujuk kepada pengambilan data dalam Python berdasarkan indeksnya.
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])

#  implementasi slicing pada Python.
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])
print("========")

# Tuple
# Tuple adalah jenis dari list yang tidak dapat diubah elemennya.

x = (1, "Dicoding", 1+3j)
print(type(x))

x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])
print("========")


# Set
# Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collection),
# dan dapat diinisialisasikan dengan kurawal “{}” di mana setiap elemennya dipisahkan dengan koma.

x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))