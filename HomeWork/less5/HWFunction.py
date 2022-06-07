def zero():
    return

def num(x):
    x *= 2
    return x
print(num(3))

def funct(x):
    if x%2 == 0:
        return print('yes')
    else:
        return print('no')

funct(2)

def funct1(x,y):
    if x > 10:
        return print('yes')
    elif x < 10:
        return  print('no')

funct1(1,2)

#лямбда
fl = lambda x, y: x % y
print(fl(14, 5))

#Чистая функция
def f2(x, y):
    return x + y
print(f2(1,2))

#Нечистая функция

peremen=100
def f3(x,y):
    z = x + y
    return peremen / z
print(f3(12 , 13))

# функции map filter

street = ['Ленина', 'Мира', 'Беды', 'Аэродромная', 'Альшевкого']
def st(x):
    return 'улица ' + x

street = list(map(st, street))
print(street)

def vowels(x):
    return x[6].lower() in 'уеыаоэяию'
filtered_street = filter(vowels, street)
print(list(filtered_street))

# max min

list3 = [1, 4, 5, 33, 12, 2, 554]
max_value = max(list3)
min_value = min(list3)
print('max = ', max_value)
print('min = ', min_value)

#
'''
def year_leap(y):
    if y % 4 == 0:
        return True
    else:
         return False


year_leap(2000)
print(year_leap())
'''
def season(num):
   if num == 12 or 1 <= num <= 2:
       print("Зима")
   elif  3 <= num <= 5:
       print("Весна")
   elif 6 <= num <= 8:
       print("Лето")
   elif 9 <= num <= 11:
       print("Осень")
   else:
       print("Неверно введён номер месяца!")
n = int(input("Введите номер месяца (1-12): "))
season(n)

#list_4 = к [16, -17, 2, 78.7, False, False, {‘True’:True}, 555, 12, 23, 42, ‘DD’]