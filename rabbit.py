# Напишите программу, которая удаляет из массива все простые числа встречающиеся больше одного раза.
print('Введите значение количества элемнтов в массиве')
n = int(input())
a = []
b = []
for i in range(n):
    print('Введите значение элемента массива')
    m = int(input())
    a.append(m)
for k in range(n):
    if a[k] < 2:
        b.append(a[k])
    elif a[k] == 2:
        q = 0
        w = 0
        for l in range(k):
            if a[k] == a[l]:
                q = 1
        for j in range(k + 1, n):
            if a[k] == a[j]:
                w = 1
        if (q != 1) and (w != 1):
            b.append(a[k])
    else:
        e = 0
        for h in range(2, k):
            if a[k] % h == 0:
                e = 1
        if e != 1:
            t = 0
            y = 0
            for g in range(k):
                if a[k] == a[g]:
                    t = 1
            for r in range(k+1, n):
                if a[k] == a[r]:
                    y = 1
            if (t != 1) and (y != 1):
                b.append(a[k])
        elif e == 1:
            b.append(a[k])
print(b)
input()
