def check_tpl(obj):
    # проверяет все ли элементы кортежа являются числами
    return all(isinstance(x, (int, float)) for x in obj)


def selection_srt(obj):
    # Проверка на числовые элементы
    if not check_tpl(obj):
        return obj

    # Преобразуем кортеж в список,
    # чтобы можно было менять элементы местами
    arr = list(obj)
    n = len(arr)

    for i in range(n - 1):
        min_idx = i # назначаем 1 элемент как минимальный
        for j in range(i + 1, n):  # далее начиная со 2 элемента до последнего ищем минимальный
            if arr[j] < arr[min_idx]:  # найденный минимум сравниваем с самым 1 элементом
                min_idx = j # если он меньше, то назначаем его как минимум

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Возвращаем обратно как кортеж
    return tuple(arr)


# тест
tpl = (6, 3, -1, 8, 4, 10, -5)
print(selection_srt(tpl))
