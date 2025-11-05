"""data = {
    (5000, 123456): ('Иванов', 'Василий'),  # использование составных ключей в словарях
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

def get_passport_info(series, number):
    key = (series, number)
    if key in data:
        last_name, first_name = data[key]
        return f"{last_name} {first_name}"
    else:
        return "Паспорт не найден"

# Пример вызова функции
print(get_passport_info(7000, 222222))  # Медведев Алексей
print(get_passport_info(1234, 111111))  # Паспорт не найден"""


names = ["Tom", "Robert", "Alla"]
ages = [20, 35, 55]

people = zip (names, ages)  # объединение в кортеж
print("Вывод объединенной информации в виде кортежа")
for i_person in people:
    print(i_person)


# объединение в словарь

people_2 = dict(zip(names, ages))
# people_2 = {
#     i_name : i_age
#     for i_name, i_age in zip(names, ages)
# }
print("Вывод объединенной информации в виде словаря")
print(people_2)