def caesar_cipher(input_message, user_step):
    russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё',
                        'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                        'н', 'о', 'п', 'р', 'с', 'т', 'у',
                        'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
                        'ы', 'ь', 'э', 'ю', 'я']

    # формируем сразу шифрованное слово
    word = ''.join(
        russian_alphabet[(russian_alphabet.index(char.lower()) + user_step) % len(russian_alphabet)]
        if char.lower() in russian_alphabet else char
        for char in input_message
    )

    print(word)


text = list(input("Введите сам текст: "))
step = int(input("Введите сдвиг: "))

caesar_cipher(text, step)
