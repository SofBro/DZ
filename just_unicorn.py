# Найти кол-во чисел взаимно простых с n не превосходящих n^2.
print('Введите число')
n = int(input())
a = []
b = []
for i in range(2, n + 1):
    if n % i == 0:
        a.append(i)
for k in range(n ** 2):
    z = 0
    for l in range(len(a)):
        if k % a[l] == 0:
            z = 1
    if z == 0:
        b.append(k)
print(b)
input()