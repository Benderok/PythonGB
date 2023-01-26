# Найдите сумму цифр трехзначного числа.

a = int(input('Enter number: '))
firstDigit = a % 1000//100
secDigit = a % 100//10
thirdDigit = a % 10
print(firstDigit+secDigit+thirdDigit)
