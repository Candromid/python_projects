"""def find_item_in_dict(string, storage_dict):   # функция проверки на наличие искомого товара на складе
    if string not in storage_dict:
        print("❌ Ошибка поиска! Такого товара нет на складе!")
        return None
    else:
        return storage_dict[string]

small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage) # объединение двух словарей

find_item = input("Введите название товара, который вы ищете: ").lower()
output_from = find_item_in_dict(find_item, big_storage)

if output_from is not None:
    print(f"📦 На складе {find_item}: {output_from} шт.")
"""


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

total_income = sum(incomes.values())  # сумма всех значений
print("Общий доход за год составил {t_i} рублей ".format(
    t_i = total_income
))

price_item = min(incomes.values()) # нахождение минимального значения в словаре
name_item = min(incomes, key = incomes.get) # нахождение ключа по значению (минимальному)
print("Самый маленький доход у {n_i}. Он составляет {p_i} рублей".format(
    n_i = name_item,
    p_i = price_item
))

incomes.pop(name_item) # удаление из словаря
print("Итоговый словарь: ",incomes)