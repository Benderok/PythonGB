# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Option 1

n = int(input('Enter size of list: '))
x = int(input('Enter element to search: '))
count = 0
for i in range(n):
    a = int(input())
    if a == x:
        count += 1
print('=>', count)

# Option 2

n = int(input('Enter size of list: '))
k = []
count = 0
for i in range(n):
    a = int(input())
    k.append(a)
x = int(input('Enter element to search: '))
for j in range(len(k)):
    if k[j] == x:
        count += 1
print('->', count)

# Option 3

n = int(input('Enter size of list: '))
k = []
for i in range(n):
    a = int(input())
    k.append(a)
x = int(input('Enter element to search: '))
xnums = [n for n in k if n == x]
print('->', len(xnums))