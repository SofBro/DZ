# Напишите программу, содержащую функцию вычисляющую функцию Эйлера для произвольного натурального числа.
# Программа должна считывать из файла массив чисел, находить ср.геометрическое значений функции Эйлера чисел массива.


def euler(n):
    a = []
    b = []
    if n == 1:
        return 1
    for i in range(2, n):
        if n % i == 0:
            a.append(i)
    for k in range(1, n):
        z = 0
        for m in range(len(a)):
            if k % a[m] == 0:
                z = 1
        if z != 1:
            b.append(k)
    return len(b)
x = []
f = open('two.txt')
for line in f:
    x.append(line)
f.close()
for t in range(len(x)):
    s = x[t].split(' ')
    s1 = list(map(int, s))
    s2 = list(map(euler, s1))
    e = 1
    for r in range(len(s2)):
       e *= s2[r]
    print(e ** 0.5)
input()
