#number1 = int(input('Введите первое число:'))
#number2 = int(input('Введите второе число:'))

# if number2 == number1**2 or number1 == number2**2:
#    print('да')
# else:
#    print('нет')

#list = [0,0,0,0,0]

# for i in range(len(list)):
#    list[i] = int(input('Введите число:'))
# print(list)

# max=list[0]

# for i in range(len(list)):
#    if max<list[i]:
#        max=list[i]
# print(max)

#import random

#my_list = []
#for i in range(5):
#    my_list.append(int(input('Введите число:'))) #my_list.append(random.randint(0,100)) # my_list.append(int(input(f'Введите {i+1} число:')))

#print(my_list)

#maxx = my_list[0]

#for item in my_list:
#    if item > maxx:
#        maxx = item

#print(maxx)


# N = int(input('Введите число:'))
# my_str = ""
# for i in range(-N,N+1):
#     if i<N:
#         my_str+=str(i) + ","
#     else:
#         my_str+=str(i)
# print(my_str)

# N = int(input('Введите число:'))
# my_str = ""
# for i in range(-N,N+1):
#     my_str+=str(i) + ", "

# print(my_str[:-2])


N = int(input('Введите число:'))
my_list = []
for i in range(-N,N+1):
    my_list.append(i)

print(*my_list, sep=', ') #раскрытие списка с разделителем sep


# На вход принимается дробное число  и показывать первую цифру дробной части числа

# number = float(input('Введите число: '))
# ostatok = (number*10)%10
# if number-round(number) ==0:
#     print('нет')
# else:
#     print(round(ostatok))

#number = float(input('Введите число: '))
# print(number)
# print(round(number, 2))
# print(int(number))

# if number==int(number):
#     print('no')
# else:
#     print(int(number*10)%10)


# number = input('Введите число: ')

# # for i in range(len(number)):
# #     if number[i] =='.':
# #         print(number[i+1])

# number=number.split('.')

# if len(number)<2:
#     print('целое')
# else:
#     print(number[1][0])


