# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

n = int(input())
m = 1
print('1', end=' ')
for i in range(0, n):
    m *= 2
    if m <= n:
        print(m, end=' ')
print()


n = int(input())
m = 1
print('1', end=' ')
while m*2 <= n:
    m *= 2
    print(m, end=' ')