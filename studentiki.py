# Напишите программу, которая обрабатывает файл “1-in.txt” с результатами сессии студентов.
# В файле в первой строке лежит число студентов, количество зачетов и экзаменов.
# Затем про каждого студента: ФИО, результаты зачетов(зачтено/незачтено) и оценки за экзамены.
# Программа должна в файл “1-out.txt" записать информацию про каждую категорию студентов:
# стипендианты, отчисленные, должники, остальные.
# Выходной файл должен состоять из 8 строк: 1 строка) Стипендианты: количество, 2 строка) Фамилии стипендиантов...
a = []
k = []
n = []
c = []
v = []
h = []
f = open('1-in.txt')
for line in f:
    a.append(line)
f.close()
for i in range(1, len(a)):
    s = a[i].split(' ')
    if s.count('незачтено') + s.count('2') > 2:
        k.append(s[0])
    elif (s.count('незачтено') + s.count('2') > 0) and (s.count('незачтено') + s.count('2') <= 2):
        n.append(s[0])
    elif s.count('незачтено') + s.count('2') == 0:
        if s.count('3') == 0:
            c.append(s[0])
        else:
            v.append(s[0])
p = open('1-out.txt', 'w')
p.write('Стипенданты: {}\n{}\n'.format(len(c), ' '.join(c)))
p.write('Отчисленные: {}\n{}\n'.format(len(k), ' '.join(k)))
p.write('Должники: {}\n{}\n'.format(len(n), ' '.join(n)))
p.write('Остальные: {}\n{}\n'.format(len(v), ' '.join(v)))
p.close()
input()