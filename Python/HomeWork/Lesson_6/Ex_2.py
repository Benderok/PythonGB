# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


list_nums = [int(input()) for i in range(int(input('Enter ammount of nums: ')))]
min_num = int(input('Enter lower boundary: '))
max_num = int(input('Enter upper boundary: '))
print(*[i for i in range(len(list_nums)) if list_nums[i] >= min_num and list_nums[i] <= max_num])