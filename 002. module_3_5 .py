def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        if first == 0: # если последняя цифра рана нулю, то вместо неё на 1 умножаем произведение предыдущих ненулевых цифр числа
            return 1

        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
