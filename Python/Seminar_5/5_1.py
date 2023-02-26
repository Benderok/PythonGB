# Хакер Василий получил доступ к классному журналу и хочет заменить все
#  свои минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# 5 4 2 2 3 4 5

def max_to_min(list):
    minimal = min(list)
    maximal = max(list)
    return[minimal if i == maximal else i for i in list]
print(*max_to_min([int(i) for i in input().split()]))