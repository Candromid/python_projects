people_count = int(input("Введите количество человек в игре: "))
kick_out_number = int(input("Введите номер на выбывание из игры: "))

print(f"Значит, выбывает каждый {kick_out_number} игрок")
circle_of_people = list(range(1, people_count + 1))

pos = 0  # начальная позиция

while len(circle_of_people) > 1:  # пока больше одного
    pos = (pos + kick_out_number - 1) % len(circle_of_people)  # формула, чтобы двигаться по кругу начиная со следующего человека после выбывшего
    print("Текущий круг людей: ", circle_of_people)
    print(f"Выбывает: {circle_of_people[pos]}")
    del circle_of_people[pos]

print("Победитель:", circle_of_people[0])





