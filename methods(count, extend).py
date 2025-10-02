"""

main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]

first_company = [0, 0, 0]

second_company = [1, 0, 0, 1, 1]

third_company = [1, 1, 1, 0, 1]

main.extend(first_company)
main.extend(second_company)
main.extend(third_company)

print(" Общий список задач: ", main)
print("Количество невыполненных задач: ", main.count(0))

"""

"""
str1 = list(input())
str2 = list(input())

print("Первое сообщение: ", "".join(map(str, str1)))  # конвертация списка в строку
print("Второе сообщение: ", "".join(map(str, str2)))

if str1.count("!") + str1.count("?") > str2.count("!") + str2.count("?"):  # подсчёт количества определенного элемента
    str1.extend(str2) # соединение двух списков
    print("Третье сообщение: ", "".join(map(str, str1)))
else:
    str2.extend(str1)
    print("Третье сообщение: ", "".join(map(str, str2)))
"""

pack = []
decode = []
bad_packets = 0

packet_count = int(input("Введите количество пакетов: "))

for i_packet_num in range(packet_count):
    print("\nПакет номер", i_packet_num + 1)
    for i_bit in range(4):
        print(i_bit + 1, " бит: ", end=" ")
        bit = int(input())
        pack.append(bit)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print("Много ошибок в пакете!")
        bad_packets += 1
    pack = []

print("\nПолученное сообщение: ", decode)
print("Количество ошибок в сообщении: ", decode.count(-1))
print("Количество потерянных пакетов: ", bad_packets)