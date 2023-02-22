# Напишите программу, используя минимум по 5 функции для работы с
# кортежем(tuple) и множествами(Set). В виде данных пусть каждый
# студент предложит свое резюме. И будет работать с этими данными.

_tuple = ("hello", 1, 2.0, "hello")

# count
print(_tuple.count(1))
print(_tuple.count("hello"))
print(_tuple.count("1"))

# index
index = _tuple.index("hello", 0, len(_tuple))
index_2 = _tuple.index("hello", 1, len(_tuple))
print(index)
print(index_2)

# __contains
is_contains = _tuple.__contains__("hello")
is_contains_2 = _tuple.__contains__("hello 2")
print(is_contains)
print(is_contains_2)

# __getitem value by index
item = _tuple.__getitem__(0)
print(item)

# len
len = _tuple.__len__()
print(len)