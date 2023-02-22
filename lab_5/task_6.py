# 6.	 Напишите	 функцию,	 показывающую,	 отсортирован	 ли
# переданный	 ей	 в качестве	 параметра	 список	 (по	 возрастанию	 или
# убыванию).	 Функция	 должна	 возвращать	 True,	 если	 список
# отсортирован,	 и False	 в противном	 случае.	 В основной	 программе
# запросите	 у пользователя	 последовательность	 чисел	 для	 списка,	 после
# чего	 выведите	 сообщение	 о том,	 является	 ли	 этот	 список
# отсортированным	изначально
def sortList(input: list):
    input.sort()


def isSorted(listCopy: list, sortedList: list):
    if listCopy == sortedList:
        print(f"Initial list were created sorted\n{True}")
    else:
        print(f"Initial list is not sorted\n{False}")
listSize = 5
initial = []
for item in range(0, listSize):
    print("Input value for adding to list")
    value = int(input())
    initial.append(value)
# initial = [10, 4, 5, 6, 7]
# initial = [1, 2, 3, 4, 5, 6]
initialCopy = initial.copy()
print(f"initial list {initial}")

sortList(initial)
sortedList = initial.copy()
print(f"sorted list {sortedList}")

isSorted(initialCopy, sortedList)
