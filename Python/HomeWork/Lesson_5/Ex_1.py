# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def sqr(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    return a * sqr(a, b-1)
a = int(input())
b = int(input())

print(sqr(a, b))