# 5.	 Для	 выигрыша	 главного	 приза	 необходимо,	 чтобы	 шесть
# номеров	на	лотерейном	билете	совпали	с шестью	 числами,	 выпавшими
# случайным	образом	в диапазоне	от	1	до	49	во	время	очередного	тиража.
# Напишите	 программу,	 которая	 будет	 случайным	 образом	 подбирать
# шесть	 номеров	 для	 вашего	 билета.	 Убедитесь	 в том,	 что	 среди	 этих
# чисел	 не	 будет	 дубликатов.	 Выведите	 номера	 билетов	 на	 экран	 по
# возрастанию.
import random


def generate_random_value(_from: int, _to: int):
    num = random.randint(_from, _to)
    return num


def is_existing_value_in_list(input: list, item: int):
    for i in input:
        if i == item:
            return True
        else:
            return False


values = []
it = 0
while it < 7:
    num = generate_random_value(1, 49)
    if len(values) == 0:
        values.append(num)
        it += 1
    elif len(values) == 1:
        if num != values[0]:
            values.append(num)
            it += 1
    else:
        isExist = is_existing_value_in_list(values, num)
        if not isExist:
            values.append(num)
            it += 1

values.sort(reverse=False)
for i in values:
    print(i, end=" ")