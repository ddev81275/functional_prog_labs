# 1. Напишите программу, используя минимум по 5 функции для работы со
# словарем (dict). В виде данных пусть каждый студент предложит свое
# резюме. И будет работать с этими данными.

_values = {
    "first_name": "Tom",
    "age": 18,
    "second_name": "Jhon",
    "hobbie": ["workout", "cycle", "books", "movie"]
}
# 1
print(f"values: {_values.values()}")

# 2
print(f"items: {_values.items()}")

# 3
print(f"keys: {_values.keys()}")

# 4
print(f"get value by key: {_values.get('age')}")

# 5
print(f"len of dictionary: {_values.__len__()}")