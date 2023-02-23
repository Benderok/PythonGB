# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

n = int(input('Enter total ammount of coins:'))
case1 = 0
case2 = 0
for i in range(n):
    coin = int(input('Enter 1/0:'))
    if coin == 1:
        case1 += 1
    else:
        case2 += 1
if case1 >= case2:
    print('Need to switch', case2)
else:
    print('Need to switch', case1)
