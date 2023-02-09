from datetime import date
import calendar
import random


# 1) Написать программу используя цикл for и while.
def months_between_current_and_last():
    current_month = date.today().month  # Feb
    print("current month is : " + calendar.month_name[current_month])

    print(f"from {calendar.month_name[current_month]} to December will be")
    month_from = current_month + 1
    month_to = 12
    for item in range(month_from, month_to):
        print(calendar.month_name[item], end=" ")


# 2) используя функцию range() сделать список.
# в функцию range() введите данные с разными типами и выведите на экран в разных примерах.
def create_int_list():
    ints = range(0, 10, 1)
    for item in ints:
        print(item, end=" ")


# 3) Используйте функции randint() randrange() random() enumerate()
# в своей программе
def _random_():
    _randint = random.randint(0, 9)
    _randrange = random.randrange(10)
    _random = random.random()
    _list = ["abc", 34, True, 40, "male"]

    print(list(enumerate(_list)))
    print(f"randint(0, 9) => {_randint}")
    print(f"random.randrange({10}) => {_randrange}")
    print(f"random.random() => {_random}")


# 4) Решите следующие задачи:
# 1. Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
def from_a_2_b(_from, _to):
    if _from <= _to:
        for item in range(_from, _to + 1):
            print(item, end=" ")
        print()
    else:
        print("not true condition A ≤ B")


# 2. Даны два целых числа A и В.
# Выведите все числа от A до B включительно, в порядке возрастания, 
# если A < B, или в порядке убывания в противном случае.
def ascending_descending(_from, _to):
    if _from <= _to:
        for item in range(_from, _to + 1, 1):
            print(item, end=" ")
        print("ascending")
    else:
        _list = range(_from, _to - 1, -1)
        for item in _list:
            print(item, end=" ")
        print("descending")


# 3. Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой задаче можно обойтись без инструкции if.
def _without_if(_from, _to):
    _list = list(range(_from, _to + 1))
    for item in _list:
        print(item % 2 == 1 and item or "", end=" ")


months_between_current_and_last()
create_int_list()
_random_()
from_a_2_b(10, 15)
from_a_2_b(15, 10)
ascending_descending(10, 15)
ascending_descending(15, 10)
_without_if(10, 15)
