# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.

def rev_nums(num):
    if num == 0:
        return ''
    nums = input()
    return rev_nums(num - 1) + f"{nums}"

print(rev_nums(int(input())))