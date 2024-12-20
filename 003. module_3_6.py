
b=0
def calculate_structure_sum(a):
    global b

    if isinstance(a, (int, float)):
        b += a
    if isinstance(a, str):
        b += len(a)
    if isinstance(a, dict): # cловарь
        for c, d in a.items():
            calculate_structure_sum(c)
            calculate_structure_sum(d)
    if isinstance(a, (tuple, set, list)):
        for c in a:
            calculate_structure_sum(c)


    return b

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
