# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input())
m = int(input())
k = []
l = []
for i in range(n):
    a = int(input())
    k.append(a)
for j in range(m):
    b = int(input())
    l.append(b)
print(*sorted(set(k).intersection(l)))
