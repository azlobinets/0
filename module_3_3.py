def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(4)
print_params(2,3)
print_params(5, 6, 7)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# 2.Распаковка параметров:

values_list = [2, "world", True]
values_dict = {"b": 10, "a": "stroka2", "c": False }

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [2, 'opa']
print_params(*values_list_2, 42)