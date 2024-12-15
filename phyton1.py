
numbers = [4, 5, 10, 20, 40, 60, 80]
new_list1 = []
for number in numbers:
    if number > 10:
        new_list1.append(number)
print(new_list1)
#Homework 1

def angka (a,b):
    result = a + b
    return result
hasil = angka (10,20)
print(hasil)

#Homework 2.1

def angka (a,b):
    result = a*b
    return result
hasil = angka (10,20)
print(hasil)

#Homework 2.2

def angka (a,b):
    result = max (a,b)
    return result
hasil = angka (10,20)
print(hasil)

#Homework 2.3

def luas_lingkaran(r):
    phi = 22/7
    luas = phi * r * r
    return luas
luas_lingkaran (12)
