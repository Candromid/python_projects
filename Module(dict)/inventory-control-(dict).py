# Внизу представлен сложный код попытки работать со структурой данных - словарь, путем обращения к словарю, потом к списку и т.д
# после данного кода я прикреплю еще 1 вариант - более питоновского подхода)

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
# мой усложненный вариант
"""
total_value = 0
total_count = 0

for name_i, code in goods.items():
    if code in store:

        for index_list in range(len(store[code])):
            value = store[code][index_list]["quantity"] * store[code][index_list]["price"]
            total_value += value
            count_i = store[code][index_list]["quantity"]
            total_count += count_i

    print("{name_item} — {count_item} штук, стоимость {total_price} рубля.".format(
        name_item=name_i,
        count_item=total_count,
        total_price=total_value
    )
    )
    total_value = 0
    total_count = 0
"""
# более короткий и более питоновский вариант кода

# Проходим по словарю goods и сразу получаем:
# good_name — название товара (например, 'Стол')
# code — его код (например, '23456')
for good_name, code in goods.items():

    # Проверяем, есть ли этот код товара в складе store
    if code in store:

        # Инициализируем счётчики для количества и общей стоимости
        total_count = 0
        total_value = 0

        # Проходим по каждому элементу списка в store[code]
        # item — это словарь вида {'quantity': ..., 'price': ...}
        for item in store[code]:
            # Прибавляем количество товара к общему количеству
            total_count += item["quantity"]

            # Прибавляем к общей стоимости: количество * цену
            total_value += item["quantity"] * item["price"]

        # Выводим результаты по товару
        # f-строка позволяет вставлять переменные внутрь текста
        print(f"{good_name} — {total_count} штук, стоимость {total_value} рублей.")




