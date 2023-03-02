# 1
#def div(x, y):
#    try:
#        x, y = int(x), int(y)
#        res = x / y
#    except valuerro:
#        return "введите число"
#    except zerroDivisionErro:
#        return "нельзя делить на 0"
#    return res
#x = input('№1:')
#y = input('№2:')
#print(div(x, y))

#2
#name= input('enter name')
#surname = input('enter surname')
#year = int(input('enter year'))
#city = input('enter city')
#email = input('enter email')
#telephone = input('input telephone')
#def my_func(name, surname, year, city, email, telephone):
#    return "join(my_func {name}, {surname}, {year}, {city}, {email}, {telephone})"
#print (f'{name}, {surname}, {year}, {city}, {email}, {telephone}')

#3
#def my_func(arg1 , arg2, arg3):
#    if arg1 >= arg3 and arg2 >= arg3:
#        return arg1 + arg2
#    elif arg1 > arg2 and arg1 < arg3:
#        return arg1 + arg3
#    else:
#        return arg2 + arg3
#print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')

#4 (получился толькоодин вариант, второй)

#def pw(x, y):
#    res = x ** y
#    return res
#num1 = int(input())
#num2 = float(input())
#s = pw(num1, num2)
#print(s)

#num1 = int(input())
#num2 = int(input())
#res = 0
#i = 1
#while i <= num2:
#    res = num1 ** (- num2)
#    i = i + 1
#print(res)

#5
#def my_sum ():
#    sum_res = 0
#    ex = False
#    while ex == False:
#        number = input('Input numbers or Q for quit - ').split()
#
#        res = 0
#        for el in range(len(number)):
#            if number[el] == 'q' or number[el] == 'Q':
#                ex = True
#                break
 #           else:
#                res = res + int(number[el])
#        sum_res = sum_res + res
#        print(f'Current sum is {sum_res}')
#    print(f'Your final sum is {sum_res}')
#my_sum()

# 6
#def int_func (*args):
#    word = input("Input words ")
#    print(word.title())
#    return
#int_func()

#7
#def int_func (*args):
#    Word = input("Введите слова через пробел").split()
#    for word in Word:
#        len1 = int(input())
#        if 3 <= ord(Word) <=122:
#            len1 +=1
#        if len1 == len(word):
#            print(word.title())
#        else:
#            print(f'{Word} - допустим только нижний регистр')
#        print(word.title())
#    return
#int_func()