"""tuple_1 = (0, 1, 2, 3, 4, 5)
tuple_2 = (-5, -4, -3, -2, -1, 0)

tuple_2 += tuple_1 # можно объединять 2 кортежа как и списки (но метод extend не работает)
print("Количество нулей в кортеже: {}".format(tuple_2.count(0)))
print(tuple_2)

"""
"""# нахождение площадей 
import math
def square(ran, high):
    side = 2 * math.pi * ran * high # площадь боковой поверхности
    full = side + 2 * (math.pi * pow(ran, 2)) # полная площадь

    return side, full  # при возврате нескольких значений возвращается кортеж 

r, h = int(input("Введите радиус: ")), int(input("Введите высоту: "))

side_and_full_square = square(r, h)
print("Площадь боковой поверхности: {}".format(side_and_full_square[0])) # вывод значений кортежа в отдельных строках
print("Вся площадь поверхности: {}".format(side_and_full_square[1]))

"""

