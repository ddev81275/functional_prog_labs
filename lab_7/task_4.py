# 4. Составьте словарь «График отпусков» для специалиста отдела кадров. По
# известному графику отпусков научитесь определять, у кого отпуск в
# заданном месяце.
# В первой строчке записано целое число – количество сотрудников. В
# следующих N строчках записана информация о дате их отпуска. Каждая
# строчка состоит из трёх частей, разделённых пробелом – фамилии
# сотрудника, дня и месяца его отпуска.
# В следующей строке записан запрос — это название месяца. Выведите через
# пробел фамилии всех сотрудников, у которых отпуск в указанном месяце.
# Если в заданном месяце никто не идет в отпуск, оставьте строку ответа
# пустой
import calendar
import datetime
import random


def generate_month():
    value = random.randrange(1, 13)
    month_name = calendar.month_name[value]
    return month_name


def show_list_vacation_by_month(vacation: dict):
    month = "June"
    items = vacation.items()

    print(f"Employees vacation in {month}")
    for name, day_month in items:
        m = list(day_month)
        if month == m[1]:
            print(name)


# second_name, day, month
vacation = {
    "Smith": {1, "June"},
    "Jones": {25, "June"},
    "Williams": {17, "July"},
    "Brown": {1, "October"}
}

print(vacation)
show_list_vacation_by_month(vacation)
