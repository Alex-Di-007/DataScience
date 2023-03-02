# задание 1
#a = 8
#print(a)

# задание 2
#time = int(input())
#print('чч', time // 3600, 'мм', time % 360 % 60, 'cc', time % 360 % 60 % 60)

# задание3
#n = int(input())
#print(n + n * 11 + n * 111)

# задание 4
#num = int(input())
#maxi = 0
#while num > 0:
#    last_dig = num % 10
#    if last_dig > maxi:
#        maxi = last_dig
#           if maxi == 9:
#                break
#    num //= 10
#print(maxi)

# задание 5 - 6
#tr = float(input('выручка:'))
#tc = float(input('издержки:'))
#p = tr - tc
#if p > 0:
#    print('вы получили прибыль')
#   print('рентабельность:', p / tr)
#    i = int(input('количество сотрудников:'))
#    if i == 0:
#        while i == 0:
#            print('Неможет быть!')
#            i = int(input('количество сотрудников:'))
#    print('прибыль одного сотрудника:', p / i)
#elif p == 0:
#    print('вы получаете нулевую прибыль')
#else: print('вы работаете в убыток')

# задание 7
a = int(input('значение а:'))
b = int(input('значение b:'))
days = 1
print('результат:')
while a < b:
    print(f'{days}-й день: {round(a, 2)}')
    a = a * 1.1
    days += 1
    print(f'на {days}-й день спортсмен достиг результата - не менее {b} км')