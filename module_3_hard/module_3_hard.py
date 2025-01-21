# 2023/10/10 00:00|Самостоятельная работа по уроку "Произвольное число параметров".

def Structure_calculate(*args):
    total_sum = 0

    for structure in args:
        if isinstance(structure, int):
            total_sum += structure
        elif isinstance(structure, str):
            total_sum += len(structure)
        elif isinstance(structure, (list, tuple, set)):
            total_sum += Structure_calculate(*structure)
        elif isinstance(structure, dict):
            total_sum += Structure_calculate(*structure.keys(), *structure.values())

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = Structure_calculate(data_structure)
print(result)