# operasi komparasi
# setiap hasil dari operasi komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print('===lebih besar dari (>)===')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# lebih kecil dari <
print('===lebih kecil dari (<)===')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# lebih besar samadengan >=
print('===lebih besar samadengan (>=)===')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# lebih kecil samadengan <=
print('===lebih kecil samadengan (<=)===')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# samadengan ==
print('===samadengan (==)===')
hasil = a == 4
print(a,'==', 4 , '=', hasil)
hasil = b == 4
print(b,'==', 4 , '=', hasil)

# tidak samadengan !=
print('===tidak samadengan (!=)===')
hasil = a != 4
print(a,'!=', 4 , '=', hasil)
hasil = b != 4
print(b,'!=', 4 , '=', hasil)

# 'is' sebagai komparasi objek identity
print('===objeck identity (is)===')

x = 5 #ini adalah assignment membuat objek
y = 5 #ini adalah assignment membuat objek

print('nilai x = ', x, ',id = ',hex(id(x)))
print('nilai y = ', y, ',id = ',hex(id(x)))

hasil = x is y
print('x is y = ', hasil)

# 'is not' sebagai komparasi objek identity
print('===objeck identity (is not)===')

x = 5 #ini adalah assignment membuat objek
y = 5 #ini adalah assignment membuat objek

print('nilai x = ', x, ',id = ',hex(id(x)))
print('nilai y = ', y, ',id = ',hex(id(x)))

hasil = x is not y
print('x is not y = ', hasil)