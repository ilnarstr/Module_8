def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        c = len(numbers)
        d = personal_sum(numbers)
        avg = d[0] / (c - d[1])
    except ZeroDivisionError:
        avg = 0
    except TypeError:
        avg = None
        print('В numbers записан некорректный тип данных (не является коллекцией)')
    return avg

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Еще строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')