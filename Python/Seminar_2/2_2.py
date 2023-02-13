# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от -50 до 50.

n = int(input())
maximum_row = current_row = 0
for i in range(n):
    temp = int(input())
    if temp > 0:
        current_row += 1
    else:
        if current_row > maximum_row: 
            maximum_row = current_row
        current_row = 0
print(maximum_row)