"""#В IT-компании есть негласные правила именования текстовых документов:
#Название файла не может начинаться с одного из специальных символов: @, №, $, %, ^, &, *, ().
#Файл должен заканчиваться расширением .txt или .docx.
while True:
    file_name = input("Введите название файла: ")

    cant_start_with = ["@", "№", "$", "%", "^", "&", "*", "(", ")"]
    must_end_with = [".txt", ".docx"]

    # Проверяем окончание и начало
    if not any(file_name.endswith(ext) for ext in must_end_with):
        print("❌ Ошибка: файл должен оканчиваться на .txt или .docx")
    elif any(file_name.startswith(sym) for sym in cant_start_with):
        print("❌ Ошибка: имя файла не может начинаться с @, №, $, %, ^, &, *, (, )")
    else:
        print("✅ Файл верный")"""


#При регистрации на сайте, помимо логина, нужно придумать пароль.
# Этот пароль должен состоять минимум из восьми символов,
# содержать хотя бы одну большую букву и не менее трёх цифр. Тогда он будет считаться надёжным.
def count_digits(input_string):
    digits = [char for char in input_string if char.isdigit()]
    return len(digits)

def check_pass(password):
    count = count_digits(password)

    if len(password) < 8:
        print("❌ Пароль слишком короткий! Минимум 8 символов.")
    elif count < 3:
        print("❌ В пароле должно быть не менее 3 цифр.")
    elif not any(char.isupper() for char in password):
        print("❌ В пароле должна быть хотя бы одна заглавная буква.")
    else:
        print("✅ Пароль надёжный!")

while True:
    password = input("Придумайте пароль: ")
    check_pass(password)
