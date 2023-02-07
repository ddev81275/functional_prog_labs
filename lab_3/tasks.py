# 1) Написать программу используя цикл for и while.
from datetime import date
import calendar


def months_between_current_and_last():
    current_month = date.today().month  # Feb
    print("current month is : "+calendar.month_name[current_month])

    print(f"from {calendar.month_name[current_month]} to December will be")
    month_from = current_month + 1
    month_to = 12
    for item in range(month_from, month_to):
        print(calendar.month_name[item], end=" ")


months_between_current_and_last()
