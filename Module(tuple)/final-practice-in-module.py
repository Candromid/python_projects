"""# Словарь со студентами: ключ — ID, значение — данные о студенте
students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology' , 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

# Функция возвращает список всех интересов и суммарную длину фамилий
def get_interests_and_surname_length(data):
    interests = []                 # хранит все интересы студентов
    total_surname_length = 0       # сумма длин всех фамилий

    # перебор всех студентов
    for student_info in data.values():
        interests.extend(student_info['interests'])        # добавляем интересы студента
        total_surname_length += len(student_info['surname'])  # прибавляем длину фамилии

    return interests, total_surname_length  # возвращаем кортеж значений


# список кортежей (id, возраст) для всех студентов
result = [(student_id, info["age"]) for student_id, info in students.items()]
print(result)  # вывод списка (ID, возраст)

# получаем интересы и сумму длин фамилий
interests, length = get_interests_and_surname_length(students)

print("Интересы:", interests)              # вывод списка интересов
print("Общая длина фамилий:", length)      # вывод суммы длин фамилий



"""

import random

numbers = [random.randint(0, 100) for _ in range(10)]
print("Оригинальный список:", numbers)

pairs = [(numbers[i], numbers[i+1]) for i in range(0, len(numbers), 2)]
print("Новый список:", pairs)

