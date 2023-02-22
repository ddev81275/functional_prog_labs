# 3. Напишите	программу,	которая	будет	запрашивать	у пользователя
# целочисленные	 значения	 и сохранять	 их	 в виде	 списка.	 Индикатором
# окончания	 ввода	 значений	 должен	 служить	 ноль.	 Затем	 программа
# должна	 вывести	 на	 экран	 все	 введенные	 пользователем	 числа	 (кроме
# нуля)	 в порядке	 возрастания – по	 одному	 значению	 в строке.
# Используйте	для	сортировки	либо	метод	sort,	либо	функцию	sorted.

inputValues = []
while True:
    print("Input integer value for adding to list: ")
    value = input()
    if int(value) == 0:
        break
    else:
        inputValues.append(int(value))

inputValues.sort(reverse=False)

for item in inputValues:
    print(item, end=" ")
