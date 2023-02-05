# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному
# числу X. Пользователь в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

n = int(input('Enter size of list: '))
k = []
for i in range(n):
    a = int(input())
    k.append(a)
x = int(input('Enter element to search: '))
closest = k[0]
minimaldiff = abs(closest - x)
for j in range(1, n):
    differ = abs(k[j] - x)
    if differ < minimaldiff:
        closest = k[j]
        minimaldiff = differ
print('->', closest)