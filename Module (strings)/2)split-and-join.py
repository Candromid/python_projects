"""

#Программа позволяющая ввести текст и затем список искомых слов в данном тексте
#затем выводит на экран каждое слово и сколько раз данное слово встречается в тексте
text = input("Введите текст: ").split()
finders = input("введите искомые слова в тексте через запятую: ").split(", ")

final_list = [[word, text.count(word)] for word in finders]

for word, count in final_list:
    print("слово: {w} — встречается в тексте: {c} раз(а)".format
          (w = word,
           c = count)
          )

"""

while True:
    grats_template = input("Введите шаблон поздравления, "
                           "в шаблоне можно использовать конструкцию {name} и {age}:")
    if '{name}' in grats_template and  '{age}' in grats_template: # Проверка на корректный ввод поздравления для метода format
        break
    else:
        print("Ошибка! Отсутствует одна или две конструкции!")

name_list = input("Введите список людей через запятую: ").split(", ")
ages_list = list(map(int, input("Введите возраст людей через пробел: ").split()))


for i in range(len(name_list)):  #Вывод поздравления для всех перечисленных именинников
    print(grats_template.format(
        name = name_list[i],
        age = ages_list[i]
    ))

# генерация списка people, где будет перечислен именинник и его возраст в качестве одного элемента списка
people = [
    " ".join([name_list[i], str(ages_list[i])])
    for i in range(len(name_list))
]
people_str = ", ".join(people)

print("Именинники: ", people_str)