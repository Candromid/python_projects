def count_uppercase_lowercase(text):
    count_up = sum(1 for c in text if c.isupper())
    count_low = sum(1 for c in text if c.islower())
    return count_up, count_low

text = input("Введите строку для анализа: ")

uppercase, lowercase = count_uppercase_lowercase(text)

print(f"🔠 Количество заглавных букв: {uppercase}")
print(f"🔡 Количество строчных букв: {lowercase}")
