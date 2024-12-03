first = int(input("Введите целое положительное число: "))
second = int(input("Ещё одно: "))
third = int(input("Ещё: "))

if first==second==third :
    print("3 числа одинаковы")
elif first==second or second==third or first==third :
    print("2 числа одинаковы")
else:
    print("0, числа все разные")


"""Тот же оператор выбора, но в другом виде выполненный:
if first==second==third :
    print("3 числа одинаковы")
else:
    if first==second or second==third or first==third :
        print("2 числа одинаковы")
    else:
        print("0, числа все разные")
"""