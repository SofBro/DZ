# Напишите программу, которая обрабатывает результаты IQ-теста из файла “2-in.txt".
# В файле лежат несколько строк со значениями(не менее 4-х).
# Программа должна вывести в консоль среднее арифметическое по лучшим трем в каждой строке результатам(одно число).
a = []
n = []
t = True
f = open('2-in.txt')
for line in f:
    a.append(line)
f.close()
b = []*3*len(a)
for i in range(len(a)):
    s = a[i].split(' ')
    for k in range(len(s)):
        if s[k].isdigit() == t:
            n.append(s[k])
    n = map(int, n)
    n = sorted(n)
    for h in range(len(n) - 3, len(n)):
        b.append(n[h])
    n = []
print(sum(b)/len(b))
input()