# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi kurang -
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi kali *
hasil = a * b
print(a, '*', b, '=', hasil)

# operasi bagi / (akan menjadi float)
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi modulus (sisa pembagian) %
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor division //
hasil = a // b
print(a, '//', b, '=', hasil)

# prioritas operasi
x = 3
y = 2
z = 4

hasiilll = x ** y * z + x / y - y % z//x
print(hasiilll)

hasiillli = x ** y * (z + x) / y - y % z//x
print(hasiillli)

'''
urutannya adalah
()
eksponen
kali, bagi, modulus, floor division
tambah, kurang
'''