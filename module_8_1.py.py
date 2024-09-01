def add_everything_up(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return str(a) + str(b)
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))