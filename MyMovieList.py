def normalize(text: str) -> str:
    """Приводим строку к нижнему регистру и убираем пробелы по краям"""
    return text.strip().lower()


def check_movie(movie, film_list):
    """Проверка наличия фильма в списке (без учёта регистра и пробелов)"""
    movie = normalize(movie)
    normalized_list = [normalize(f) for f in film_list]
    return movie in normalized_list


def menu_of_command():
    print("\nДоступные команды: ")
    print("1 - Добавить")
    print("2 - Вставить")
    print("3 - Удалить")


films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

my_films = []

while True:
    print("\nВаш текущий список фильмов:", my_films)
    name_movie = input("Название фильма: ")

    if check_movie(name_movie, films):
        menu_of_command()
        try:
            command = int(input("Выберите команду: "))
        except ValueError:
            print("Ошибка! Введите число (1, 2 или 3).")
            continue

        if command == 1:  # Добавить
            if check_movie(name_movie, my_films):
                print("Данный фильм уже есть в списке!")
            else:
                my_films.append(name_movie)

        elif command == 2:  # Вставить
            choice = input("Вы хотите вставить фильм перед или после определенного фильма? ").strip().lower()
            choice_name = input("Введите название этого фильма: ")

            if not check_movie(choice_name, my_films):
                print("Такого фильма нет в вашем списке!")
                continue

            index_choice_film = [normalize(f) for f in my_films].index(normalize(choice_name))

            if choice == "перед":
                my_films.insert(index_choice_film, name_movie)
            elif choice == "после":
                my_films.insert(index_choice_film + 1, name_movie)
            else:
                print("Ошибка! Нужно ввести 'перед' или 'после'.")

        elif command == 3:  # Удалить
            if check_movie(name_movie, my_films):
                my_films = [f for f in my_films if normalize(f) != normalize(name_movie)]
            else:
                print("Данного фильма нет в вашем списке!")

        else:
            print("Неизвестная команда! Введите 1, 2 или 3.")

    else:
        print("Такого фильма нет на сайте!")

