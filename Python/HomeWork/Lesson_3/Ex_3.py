# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо 
# только английские, либо только русские буквы.


score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, 
        "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, 
        "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, 
        "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, 
        "y": 4, "z": 10}

n = input()
total = 0
for i in n:
    total += score[i]
print(total)

# Option 2

# n = input('Enter word: ')
# count = 0
# for i in range(len(n)):
#     if n[i].lower() == 'a' or n[i].lower() == 'e' or n[i].lower() == 'i' or n[i].lower() == 'o' or n[i].lower() == 'u' or n[i].lower() == 'l' or n[i].lower() == 'n' or n[i].lower() == 's' or n[i].lower() == 't' or n[i].lower() == 'r':
#         count += 1
#     if n[i].lower() == 'd' or n[i].lower() == 'g':
#         count += 2
#     if n[i].lower() == 'b' or n[i].lower() == 'c' or n[i].lower() == 'm' or n[i].lower() == 'p':
#         count += 3
#     if n[i].lower() == 'f' or n[i].lower() == 'h' or n[i].lower() == 'v' or n[i].lower() == 'w' or n[i].lower() == 'y':
#         count += 4
#     if n[i].lower() == 'k':
#         count += 5
#     if n[i].lower() == 'j' or n[i].lower() == 'x':
#         count += 8
#     if n[i].lower() == 'q' or n[i].lower() == 'z':
#         count += 10
#     if n[i].lower() == 'а' or n[i].lower() == 'в' or n[i].lower() == 'е' or n[i].lower() == 'и' or n[i].lower() == 'н' or n[i].lower() == 'о' or n[i].lower() == 'р' or n[i].lower() == 'с' or n[i].lower() == 'т':
#         count += 1
#     if n[i].lower() == 'д' or n[i].lower() == 'к' or n[i].lower() == 'л' or n[i].lower() == 'м' or n[i].lower() == 'п' or n[i].lower() == 'у':
#         count += 2
#     if n[i].lower() == 'б' or n[i].lower() == 'г' or n[i].lower() == 'ё' or n[i].lower() == 'ь' or n[i].lower() == 'я':
#         count += 3
#     if n[i].lower() == 'й' or n[i].lower() == 'ы':
#         count += 4
#     if n[i].lower() == 'ж' or n[i].lower() == 'з' or n[i].lower() == 'х' or n[i].lower() == 'ц' or n[i].lower() == 'ч':
#         count += 5
#     if n[i].lower() == 'ш' or n[i].lower() == 'э' or n[i].lower() == 'ю':
#         count += 8
#     if n[i].lower() == 'ф' or n[i].lower() == 'щ' or n[i].lower() == 'ъ':
#         count += 10
# print(count)