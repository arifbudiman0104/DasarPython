# Casting adalah mengubah dari satu tipe ke tipe lain
# tipe data = int, float, string, boolean

# INTEGER
print('====INT====')

data_int = 110
print('data = ', data_int, 'tipe = ', type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # akan false jika nilai int = 0

print('data = ', data_float, 'tipe = ', type(data_float))
print('data = ', data_str, 'tipe = ', type(data_str))
print('data = ', data_bool, 'tipe = ', type(data_bool))

# FLOAT
print('====FLOAT====')

data_float = 9.5
print('data = ', data_float, 'tipe = ', type(data_float))

data_int = int(data_float)  # akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)  # akan false jika nilai float = 0

print('data = ', data_int, 'tipe = ', type(data_int))
print('data = ', data_str, 'tipe = ', type(data_str))
print('data = ', data_bool, 'tipe = ', type(data_bool))
