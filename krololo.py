# Напишите программу, которая находит во входном потоке простые числа.
# Входной поток заканчивается символом ‘!’.
t = True
k = 0
n = []
while n != '!':
    print('Введите строку')
    n = input()
    if n.isdigit() == t:
        n = int(n)
        if n < 2:
            if n == 1:
                print(n, '- единица')
            elif n == 0:
                print(n, '- ноль')
            else:
                print(n, '- составное число')
        elif n == 2:
            print(n, '- простое число')
        else:
            for i in range(2, n):
                if n % i == 0:
                    k = 1
            if k == 1:
                print(n, '- составное число')
            else:
                print(n, '- простое число')
    elif n != '!':
        print(n, '- не число')
input()
