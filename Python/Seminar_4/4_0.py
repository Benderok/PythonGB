# Напишите программу, которая принимает
# на вход строку, и отслеживает, сколько
# раз каждый символ уже встречался.
# Количество повторов добавляется к
# символам с помощью постфикса формата _n.


string = input().split()

D = {}.fromkeys(string, 0)

for i in string:
    print(f"{i}_{D[i]}" if D[i] else i, end=" ")
    D[i] += 1