"""order = {'apple': 2,
         'banana': 3,
         'pear': 1,
         'watermelon': 10,
         'chocolate': 5}

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

total = 0 # переменная для хранения суммы

#. for product, amount in order.items():
# Цикл проходит по словарю order.
# order.items() возвращает пары:
# product — название товара (ключ)
# amount — количество (значение)

# for product, amount in order.items():
# Цикл проходит по словарю order.
# order.items() возвращает пары:
# product — название товара (ключ)
# amount — количество (значение)

for product, amount in order.items():
    price = incomes.get(product, 0)  # если нет товара, вернёт 0
    total += price * amount

print("Общая выручка по имеющимся товарам:", total)
"""

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

# Получаем список имён игроков команды A, которые отдыхают
team_A_members = [
    player["name"]                      # берём имя игрока
    for player in players_dict.values() # перебираем всех игроков словаря (только значения без ключа)
    if player["team"] == "A" and player["status"] == "Rest" # фильтруем по команде и статусу
]

# Получаем список имён игроков команды B, которые тренируются
team_B_members = [
    player["name"]
    for player in players_dict.values()
    if player["team"] == "B" and player["status"] == "Training"
]

# Получаем список имён игроков команды C, которые путешествуют
team_C_members = [
    player["name"]
    for player in players_dict.values()
    if player["team"] == "C" and player["status"] == "Travel"
]

# Выводим результаты, объединяя имена через запятую
print("Команда A, отдыхают:", ", ".join(team_A_members))
print("\nКоманда B, тренируются:", ", ".join(team_B_members))
print("\nКоманда C, путешествуют:", ", ".join(team_C_members))


