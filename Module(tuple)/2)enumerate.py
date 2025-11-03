"""import random

alphabet = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
first_list = random.choices(alphabet, k=10) # создаются списки из 10 случайных букв алфавита, которые могут повторяться
second_list = random.choices(alphabet, k=10)
print("Первый список: ", first_list)
print("Второй список: ", second_list)

first_dict = {}
second_dict = {}

for index, char in enumerate(first_list):  # через цикл вытаскиваем индекс и значение и заполняем словарь ключ: значение
    first_dict[index] = char
for index, char in enumerate(second_list):
    second_dict[index] = char

print("Первый словарь: ", first_dict)
print("Второй словарь: ", second_dict)
"""


# Один заказчик попросил нас написать небольшой скрипт для своих криптографических нужд.
# При этом он заранее предупредил, что скрипт должен уметь работать с любым итерируемым типом данных.
# Напишите функцию, которая возвращает список из элементов итерируемого объекта
# (кортежа, строки, списка, словаря), у которых индекс чётный.

# Примечание: для проверки типа можно использовать функцию
# isinstance(<элемент>, <тип данных>), которая возвращает True,
# если элемент принадлежит к этому типу данных, и возвращает False в противном случае.

def list_of_even_indices(obj):
    output_list = []
    if isinstance(obj, tuple):
        print("Допустим, есть такой кортеж: ", obj)
        for index, char in enumerate(obj):
            if index % 2 == 0:
                 output_list.append(char)
    elif isinstance(obj, str):
        print("Допустим, есть такая строка: ", obj)
        for index, char in enumerate(obj):
            if index % 2 == 0:
                output_list.append(char)
    elif isinstance(obj, list):
        print("Допустим, есть такой список: ", obj)
        for index, char in enumerate(obj):
            if index % 2 == 0:
                output_list.append(char)
    elif isinstance(obj, dict):
        print("Допустим, есть такой словарь: ", obj)
        for index, char in enumerate(obj):
            if index % 2 == 0:
                output_list.append(obj[index])

    return output_list


text = input("Введите строку: ")
some_list = [100, 200, 300, 'буква', 0, 2, 'а']
some_dict = {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}

output = list_of_even_indices(text)

print(output)







