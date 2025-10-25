"""num = int(input("Введите целое число: ")) # число до которого будет заполнен словарь

num_dict = {} # объявление словаря

for i in range(1, num + 1): # цикл от 1 до num
    num_dict[i] = i ** 2  # ключ: число, значение: число в квадрате

print(num_dict)
"""
"""
student_info = input(
    "Введите информацию о студенте через пробел\n"
    "Имя Фамилия Город Место учёбы Оценки: "
).split()   # Заполнение информации о студенте и конвертация в список с разделением по пробелу

student_dict = {"Имя": student_info[0], "Фамилия": student_info[1], "Город": student_info[2],
                "Место учёбы": student_info[3], "Оценки": []}   # заполнение словаря о данных о студенте

for i_grade in student_info[4:]:
    student_dict["Оценки"].append(i_grade)       # заполнение ключа ОЦЕНКИ через список оценок

for index in student_dict:
    print(index, " - ", student_dict[index])    # Вывод словаря в привычном формате (столбиком для удобства)
"""


# Добавление в словарь "Контакты" имени и номер телефона!
def check_phone_number(number: str) -> bool:
    # 1️⃣ Убираем пробелы в начале и конце
    number = number.strip()

    # 2️⃣ Убираем все пробелы, дефисы, скобки и прочие символы
    cleaned = ''.join(ch for ch in number if ch.isdigit())

    # 3️⃣ Проверяем длину (обычно телефон 10–15 цифр по стандарту ITU E.164)
    if len(cleaned) < 10 or len(cleaned) > 15:
        return False

    # 4️⃣ Проверяем, что номер начинается с цифры (не с '+', '-', и т.д.)
    if not cleaned[0].isdigit():
        return False

    # Если все проверки пройдены — номер валидный
    return True


contacts = {}

while True:
    print("Текущие контакты:\n", contacts)
    name = input("Введите имя: ").strip()   # ← убираем пробелы в начале и конце
    phone_number = input("Введите номер телефона: ").strip()


    if name in contacts:
        print(f"❌ Контакт с именем '{name}' уже существует!")
        continue
    elif not check_phone_number(phone_number):
        print("Введен некорректный номер телефона, попытайтесь заново! ")
        continue
    else:
        contacts[name] = phone_number
        print(f"✅ Контакт {name} добавлен!")
