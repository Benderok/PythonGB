# Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница.
# Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

import math
s = int(input('Summ of x1 and x2:'))
p = int(input('Produpt of x1 and x2:'))
d = s**2 - 4*p
if d < 0:
    print('No answer!')
elif d == 0:
    print(s/2, s/2)
else:
    x1 = ((s - math.sqrt(d))/(2))
    x2 = ((s + math.sqrt(d))/(2))
    print(x1, x2)




s = int(input('Summ of x1 and x2: '))
p = int(input('Product of x1 and x2: '))
x1 = x2 = 0
sol = False
for i in range(0, 1001):
    x1 = i
    for j in range(0, 1001):
        x2 = j
        if x1+x2==s and x1*x2==p:
            sol = True
            print('Solution: ', x1, x2)
if sol == False:
    print('No answer!')