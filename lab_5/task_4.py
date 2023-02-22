# 4. Напишите	 программу,	 которая,	 как	 и в предыдущем	 случае,
# будет	запрашивать	у пользователя	целые	числа	и сохранять	их	в виде
# списка.	Индикатором	окончания	ввода	значений	также	должен	служить
# ноль.	На	 этот	раз	необходимо	 вывести	на	 экран	 введенные	значения	 в
# порядке	убывания.

inputValues = []
while True:
    print("Input integer value for adding to list: ")
    value = input()
    if int(value) == 0:
        break
    else:
        inputValues.append(int(value))

sortedList = sorted(inputValues, reverse=True)
for item in sortedList:
    print(item, end=" ")
