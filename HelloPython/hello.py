#print('Введите a');
#a=int(input())
#print('Введите b');
#b=int(input())
#print(a, '+', b, '=', a+b)
#print('{} {}'.format(a,b))
#print(f'{a} {b}')


#Арифметические операции

#a=123
#b=321
#c=a+b
#print(c)

#Логические операции

#f=[1,2,3,4]
#print(f)
#print(2 in f)
#is_odd = f[0] % 2 ==0 # is_odd = not f[0] % 2

#Управляющие конструкции

#a=int(input('a= '))
#b=int(input('b= '))
#if a>b:
#    print(a)
#else:
#    print(b)

#username = input('Введите имя: ')
#if username == 'Маша':
# print('Ура, это же МАША!')
#elif username == 'Марина':
# print('Я так ждала Вас, Марина!')
#elif username == 'Ильнар':
# print('Ильнар - топ)')
#else:
# print('Привет, ', username)

#original = 23
#inverted = 0
#while original != 0:
# inverted = inverted * 10 + (original % 10)
# original //= 10
#print(inverted)

#original = 23
#inverted = 0
#while original != 0:
# inverted = inverted * 10 + (original % 10)
# original //= 10
# print(original)
#else:
# print('Пожалуй')
# print('хватит )')
#print(inverted)

#for i in 1, -2, 3, 14, 5:
#    print(i**2)


#r=range(10)
#for i in r:     #for i in range(10) выводит числа от 0 до 9
                #for i in range(1, 10) выводит числа от 1 до 9
                #for i in range(1, 10, 2) выводит числа от 1 до 9 через 2 числа 
                #for i in 'qwe-rty' тоже счамое со строками
#    print(i)


text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
 print(c)

 text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

#

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6)) # преобразование рэнж в лист
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(f'{len(numbers)} len')
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент


def f(x):
 if x == 1:
    return 'Целое'
 elif x == 2.3:
    return 23
 else:
    return

print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType
