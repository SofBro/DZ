# Реализуйте в виде рекурсивной функции алгоритм Быстрой Сортировки для массива чисел.
def qui(s):
 if len(s) <= 1:
  return s
 n = s[0]
 m = []
 r = []
 b = []
 for i in range(len(s)):
  if s[i] < n:
   m.append(s[i])
  if s[i] == n:
   r.append(s[i])
  if s[i] > n:
   b.append(s[i])
 return qui(m) + r + qui(b)
k = [546, 67, 34, 567, 0, -56, 6244, 67]
print(qui(k))
input()