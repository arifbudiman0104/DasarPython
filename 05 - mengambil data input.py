# input user

# data yang dimasukan pasti string
data = input('Masukan data: ')
print('data = ', data, type(data))

# jika ingin mengambil int maka
angka = int(input('Masukan angka bulat: '))
print('data = ', angka, type(angka))
angka = float(input('Masukan angka koma: '))
print('data = ', angka, type(angka))

# bagaimana dengan boolean
biner = bool(int(input('masukan nilai boolean(1/0):')))
print('data = ',biner,'type=',type(biner))