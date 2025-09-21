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
