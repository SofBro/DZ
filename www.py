# Напишите программу, которая подсчитывает, сколько раз в строке встретился символ ‘w
a = []
print('Введите элементы в строку')
s = input()
h = len(s)
for i in range(0, h):
    if s[i] == 'w':
        a.append(s[i])
print(len(a))
input()
