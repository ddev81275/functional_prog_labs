from datetime import date
import calendar
import random


# 1) Написать программу используя цикл for и while.
def months_between_current_and_last():
    current_month = date.today().month  # Feb
    print("current month is : "+calendar.month_name[current_month])

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

# months_between_current_and_last()
# create_int_list()
_random_()
