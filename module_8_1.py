def add_everything_up(a, b):
    try:
        result = a + b
        print(result)

    except TypeError:
        result = str(a) + str(b)
        print(result)

add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)