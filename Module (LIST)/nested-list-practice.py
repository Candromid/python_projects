"""mattrix_team = [] # пустой список куда будут вноситься список команд
num = 1 # переменная для заполнения участниками каждую команду
players_count = int(input("Введите количество участников: "))  # общее количество участников
team_count = players_count // 3  # в каждой команде по 3 участника

for i_team in range(team_count): # цикл до количества команд
    mattrix_team.append(list(range(num, num + 3))) # Заполнение списка mattrix_team списком команд из участников
    num += 3 # увеличение параметра

for i in range(team_count):
    for j in range(team_count - 1):
        print(mattrix_team[i][j], end=" ")
    print()"""

def add_new_fruit(name, price, fruit_list):
    boofer = [name, price]
    return fruit_list.append(boofer)

def price_increase(value, fruit_list):
    for price in fruit_list:
        price[1] += (price[1] * value) / 100

    return fruit_list



goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]


while True:
    print("Текущий ассортимент: ", goods)
    fruit_name = input("Введите имя фрукта, который хотите добавить в ассортимент: ")
    fruit_price = int(input("Введите стоимость фрукта: "))
    add_new_fruit(fruit_name, fruit_price, goods)

    new_price = int(input("Укажите на сколько процентов увеличилась цена фруктов? "))
    price_increase(new_price, goods)
