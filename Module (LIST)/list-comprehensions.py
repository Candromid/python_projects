"""# Генерация списков
A_digit = int(input("Введите число А: "))
B_digit = int(input("Введите число B: "))


# x ** 3 - выражение которое возвращает значение
# x - переменная цикла for
# range(A, B) - итерируемый объект

first_list = [x ** 3 for x in range(A_digit, B_digit + 1)]
second_list = [x ** 2 for x in range(A_digit, B_digit + 1)]

print("Левая граница: ", A_digit)
print("Правая граница: ", B_digit)


print(f"Список кубов чисел в диапазоне от {A_digit} до {B_digit}: ", first_list)
print(f"Список кубов чисел в диапазоне от {A_digit} до {B_digit}: ", second_list)"""
from operator import index

"""
#Программа которая учитывая список текущих цен и вводится ежегодный процент увеличения , вывод новых увеличенных цен
# функция которая принимает процент и саму цену, возвращает уже окончательную цену с прибавленным процентом к ней
def get_higher_price(percent, price):
    return ((percent * price) / 100) + price

prices_now = [53.5, 29.8, 30, 16.3, 52] # Список цен на сегодняшний день
first_percent = int(input("Введите увеличение цен на процент за 1 год: ")) #Процент на который цены увел-ся за 1 год
second_percent = int(input("Введите увеличение цен на процент за 2 год: ")) #Процент на который цены увел-ся за 2 год

#генерация списков , где функция подсчитывает новую цену с учетом повышенного процента и заполняет этими ценами новый список
# get_higher_price(first_percent, i_price) - считает новую цену с учетом процента
# i_price - переменная цикла которая берет цену для функции из списка старых цен
# prices_now - список старых цен который необходимо увеличить
prices_first = [get_higher_price(first_percent, i_price) for i_price in prices_now]
prices_second = [round(get_higher_price(second_percent, i_price), 2) for i_price in prices_first]

print("Список старых цен", prices_now)
print("Cписок цен с учетом повышения цен за 1 год ",prices_first)
print("Cписок цен с учетом повышения цен за 2 год ",prices_second)"""


"""
# Генерация списков с условиями 
A_digit = int(input("Введите число А: "))
B_digit = int(input("Введите число B: "))


# Если идёт фильтрация вывода то условие просто ставится в конец как even_numbers
# Если идёт выбор элемента с блоком else то условия ставится в начало!

even_numbers = [x for x in range(A_digit, B_digit) if x % 2 == 0] #
odds_cube_numbers = [(x if x % 2 == 0 else x ** 2) for x in range(A_digit, B_digit)]

print("Левая граница: ", A_digit)
print("Правая граница: ", B_digit)


print(f"Список четных чисел в диапазоне от {A_digit} до {B_digit}: ", even_numbers)
print(f"Список четных чисел и нечетных чисел в квадрате в диапазоне от {A_digit} до {B_digit}: ", odds_cube_numbers)"""

"""
# Замена всех отрицательных цен на 0 в новом списке цен
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_original_prices = [(int(price == 0) if price < 0 else price) for price in original_prices]

print(new_original_prices)
"""
"""
# Задача "Монстр" проверка выжил ли или погиб!
import random
# первые два списка заполняются рандомно уроном монстров в разных диапозонах 
# если атака первых двух отрядов суммарно выше 100 то монстр 3 отряда погибает, иначе выживает
squad_1 = [random.randint(50, 80) for _ in range(10)] 
squad_2 = [random.randint(30, 60) for _ in range(10)]
squad_3_conditional = ["Погиб" if squad_1[i_dmg_monster] + squad_2 [i_dmg_monster] > 100
                       else "Выжил"
                       for i_dmg_monster in range(10)]

print("Урон первого отряда:", squad_1)
print("Урон второго отряда:", squad_2)
print("Состояние третьего отряда:", squad_3_conditional)
"""


import random
original_prices = [random.randint(-50, 100) for _ in range(10)]

boofer = [x if x > 0 else int(x == 0) for x in original_prices]

print(sum(original_prices))
print(sum(boofer))
print("\nМы потеряли: ",  sum(original_prices) - sum(boofer))



