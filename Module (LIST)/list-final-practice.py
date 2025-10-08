"""
#Поиска гласных в тексте с помощью генерации списков
text = list(input("введите текст: "))
vowels = "аеёиоуыэюяAEЁИОУЫЭЮЯ"
output = [char for char in text if char in vowels]
print(output)
print("Длина списка: ", len(output))
"""
"""
# Есть список 2х команд, сформировать 3 список победителей из попарно выставленных участников
import random

squad_1 = [round(random.uniform(5,10), 2) for _ in range(20)] 
squad_2 = [round(random.uniform(5,10), 2) for _ in range(20)]
squad_3_condition = [max(squad_1[player], squad_2[player]) for player in range(20)]

print("первая команда: ", squad_1)
print("вторая команда: ", squad_2)
print("команда победителей", squad_3_condition)"""

"""
#Тренировка со срезами
alphabet = 'abcdefg'
copy = alphabet[:]

print("1. Копия строки: ", copy)
print("2. Ревёрс: ", alphabet[::-1])
print("3. Каждый 2-ой элемент: ", alphabet[::2])
print("4. Каждый 2-ой элемент после первого: ", alphabet[1::2])
print("5. Все элементы до второго: ", alphabet[:1])
print("6. Все элементы с конца, до предпоследнего: ", alphabet[:-2:-1])
print("7. все элементы в диапазоне индексов от 3 до 4 (не включая 4): ", alphabet[3:4])
print("8. Последние 3 элемента: ", alphabet[-3:])
"""

"""
#На вход в программу подаётся строка, в которой буква h встречается как минимум два раза. 
# Реализуйте код, который разворачивает последовательность символов, 
# заключённую между первым и последним появлением буквы h, в противоположном порядке.
text = input("Введите строку: ")
a_point = text.index("h")
b_point = text.rindex("h")

print(" Развёрнутая последовательность между первым и последним h: ", text[b_point - 1  : a_point : -1])"""

"""
#Генерация ДВУмерного списка  и обратное разложение в одинарный список
two_dimensional_list = [[x for x in range(i, i + 3)] for i in range(1, 13, 3)]
print(two_dimensional_list)

usual_list = [x for sublist in two_dimensional_list for x in sublist]
print(usual_list)
"""



