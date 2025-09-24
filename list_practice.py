'''
Здесь будут храниться все практические задачи связанные со списками ( list )
'''

"""

books_ID = [50, 34, -1, -1, 2, 23, -1]
new_book_ID = []

for _ in range(5):
    input_book_ID = int(input("Введите ID книги: "))
    new_book_ID.append(input_book_ID)

books_ID.extend(new_book_ID)
print(books_ID)

while -1 in books_ID:
    books_ID.remove(-1)

print(books_ID)

"""
# задача на поиск сотрудников
"""
count_of_employees = int(input("Введите количество сотрудников: "))
ID_of_employees = []
flag = False

for _ in range(count_of_employees):
    ID = int(input("Введите ID сотрудника: "))
    ID_of_employees.append(ID)

searched_ID = int(input("Введите ID сотрудника, которого хотите найти: "))


for i in ID_of_employees:
    if i == searched_ID:
        flag = True

if flag:
    print("Сотрудник на месте!")
else:
    print("Сотрудник с таким ID не работает в данной компании! ")
    
"""


# задача на кратность

"""
def num_list ():
    number = int(input("Введите количество чисел в списке: "))
    list_of_number = []
    for i in range(number):
        print(f"Введите {i + 1} число: ", end="")
        digit = int(input())
        list_of_number.append(digit)

    return list_of_number

def multiplicify (number):
    list_of_number = num_list()
    summ_of_index = 0
    for i in range(len(list_of_number)):
        if list_of_number[i] % number == 0:
            print(f"Индекс числа {list_of_number[i]} = {i}")
            summ_of_index += i
    print("Сумма индексов: ", summ_of_index)




multiplicify(10)
"""

# обращение по индексу к элементу списка

"""
dog_count = int(input("Введите количество собак в списке: "))
dog_scores = []

for _ in range(dog_count):
    print(f"Очков за сезон у {_ + 1} собаки: ", end='')
    score = int(input())
    dog_scores.append(score)

print("Списков очков у собак: ", dog_scores)

min_score = dog_scores[0]
min_index = 0
max_score = 0
max_index = 0
for i_dogs in range(dog_count):
    if min_score > dog_scores[i_dogs]:
        min_score = dog_scores[i_dogs]
        min_index = i_dogs
    if max_score < dog_scores[i_dogs]:
        max_score = dog_scores[i_dogs]
        max_index = i_dogs

dog_scores[min_index], dog_scores[max_index] = dog_scores[max_index], dog_scores[min_index]
print("Итоговый списков очков у собак: ", dog_scores)
"""

# Генерация списка нечетных чисел от 1 до N
"""def odd_num(number):
    if number % 2 == 0:
        number -= 1
        return number
    else:
        return number

num = int(input("Введите число N: "))
num = odd_num(num)
number_list = []
for i in range(num):
    if (i + 1) % 2 == 0:
        continue
    number_list.append(i + 1)

print(number_list)"""

# Задача на список фильмов где пользователь может добавить из данного списка в свои Закладки для просмотра позже

"""films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
bookmark = []
flag = False
films_count = int(input("Сколько фильмов хотите добавить ? "))


for _ in range(films_count):
    film_name = input("Введите название фильма: ")
    for i_film in range(len(films)):
        if film_name == films[i_film]:
            flag = True
    if flag:
        bookmark.append(film_name)
    else:
        print("Такого фильма нет в списке")

    flag = False
    
print("ваш список сохраненных фильмов: ", bookmark)  
    """



#Задача "Контейнеры" (суть в том чтобы элемент вставить в определенное место по убыванию

container_count = int(input("Введите количество контейнеров "))
containers = []

for _ in range(container_count):
    container = int(input("Введите вес контейнера: "))
    containers.append(container)

x = int(input("Введите массу нового контейнера "))
while x <= 200:
    
    break
else:
    print("некорректный ввод")