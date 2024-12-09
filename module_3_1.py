# Функция count_calls как средство подсчёта всех вызовов остальных функций.
calls = 0
def count_calls():
    global calls
    calls += 1


# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки,
# строку в верхнем регистре, строку в нижнем регистре.

def string_info(string):
    count_calls()  # для подсчёта вызовов всех функций
    b = len(string)
    c = string.upper()
    d = string.lower()
    return b, c, d  # вернёт кортеж

# Функция is_contains принимает два аргумента: строку и список, и возвращает True,
# если строка находится в этом списке, False - если отсутствует. Регистром строки
# при проверке пренебречь: UrbaN ~ URBAN.

def is_contains (string,list_to_search):
    count_calls()  # для подсчёта вызовов всех функций
    for i in list_to_search:

        if type(i).__name__ == 'str': # проверяем является ли элемент списка строкой
            if i.lower() == string.lower():
                return True
    return False

# поверка работоспособности
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)












