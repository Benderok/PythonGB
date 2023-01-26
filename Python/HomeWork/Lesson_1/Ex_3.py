# Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

bilet = int(input('Enter ticket number XXXXXX: '))
firstDigit = bilet % 1000000//100000
secDigit = bilet % 100000//10000
thirdDigit = bilet % 10000//1000
forthDigit = bilet % 1000//100
fithDigit = bilet % 100//10
sixthDigit = bilet % 10
if firstDigit+secDigit+thirdDigit == forthDigit+fithDigit+sixthDigit:
    print('YES')
else:
    print('NO')
