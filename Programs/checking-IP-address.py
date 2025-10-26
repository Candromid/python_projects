ip_address = input("Введите IP: ").split(".")

if len(ip_address) != 4 or not all(part.isdigit() for part in ip_address): # проверка длинны айпи адреса и что каждый октет - число!
    print("❌ Неверный формат IP!")
elif not all(0 <= int(part) <= 255 for part in ip_address): # проверка что каждый октет находится в диапазоне от 0 до 255
    print("❌ Числа в IP должны быть от 0 до 255!")
else:
    print("✅ IP корректный!")
