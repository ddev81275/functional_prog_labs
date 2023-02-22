# 1. Заполните один кортеж десятью случайными целыми числами от 0 до 5
# включительно. Также заполните второй кортеж числами от -5 до 0. Для
# заполнения кортежей числами напишите одну функцию. Объедините
# два кортежа с помощью оператора +, создав тем самым третий кортеж.
# С помощью метода кортежа count() определите в нем количество
# нулей. Выведите на экран третий кортеж и количество нулей в нем.

def fill_values_to_tuple(_from: int, _to: int):
    _list = range(_from, _to + 1)
    _tuple = tuple(_list)
    return _tuple

_tuple = fill_values_to_tuple(0, 5)
_tuple_2 = fill_values_to_tuple(-5, 0)
_tuple_3 = _tuple_2 + _tuple
zero_counter = _tuple_3.count(0)
print(f"third tuple: {_tuple_3}")
print(f"zero numbers: {zero_counter}")
