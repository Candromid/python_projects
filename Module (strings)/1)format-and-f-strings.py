"""

name_user = input("Введите имя должника: ")
duty = int(input("Введите сумму задолженности: "))
print("{name}! {name}, привет! Как дела, {name}? Где мои {duty_user} рублей? {name}! ".format
      (name = name_user,
       duty_user = duty)
      )

"""
"""

# Формирование IP адресса
while True:
    print("Каждый октет должен быть в диапазоне от 0 до 255 включительно!")
    octet_1 = int(input("Введите 1 октет: "))
    octet_2 = int(input("Введите 2 октет: "))
    octet_3 = int(input("Введите 3 октет: "))
    octet_4 = int(input("Введите 4 октет: "))

    if (0 <= octet_1 <=255) and (0 <= octet_2 <=255) and (0 <= octet_3 <=255) and (0 <= octet_4 <=255):
        break
    else:
        print("Введенный один из октетов имеет неправильный диапазон, введите заново!")


ip_address = "{oct1}.{oct2}.{oct3}.{oct4}".format(
    oct1 = octet_1,
    oct2 = octet_2,
    oct3 = octet_3,
    oct4 = octet_4
)

print(ip_address)
"""


# форматирование вывода (подстроки)

details_num = 5000000000
price = 23.25516184
increase = 0.0456124

print("На складе {:,d} деталей".format(details_num))  # разбивка целого большого числа на разрядный вид
print("Каждая деталь стоит {:.2f} рублей".format(price)) # округление числа до сотых
print("Цена увеличилась на {:.1%}".format(increase)) # представление числа в виде процента