# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def is_prime_num(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    for i in range(3, int((n**0.5)+1), 2):
        if n % i == 0:
            return False
    return True

print(is_prime_num(int(input())))