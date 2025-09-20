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


