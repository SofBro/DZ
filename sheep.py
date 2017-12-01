# Напишите программу содержащую логическую функцию проверки списка чисел, на то составные ли они.
# Программа должна применять эту функцию к списку считанному с файла.


def sheep(n):
    k = 0
    if n == 1:
        return '- единица'
    elif n == 0:
        return '- ноль'
    else:
        for i in range(2, n):
            if n % i == 0:
                k = 1
        if k != 0:
            return '- составное'
    return '- простое'
t = True
a = []
f = open('one.txt', 'r')
for line in f:
    a.append(line)
f.close()
for t in range(len(a)):
    s = a[t].split(' ')
    for y in range(len(s)):
        print(int(s[y]), sheep(int((s[y]))))
input()
