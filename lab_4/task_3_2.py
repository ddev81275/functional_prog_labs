# 2)	Строковый метод isdigit() проверяет, состоит ли строка только из цифр.
# Напишите программу, которая запрашивает с ввода два целых числа и выводит их сумму.
# В случае некорректного ввода программа не должна завершаться с ошибкой, а должна продолжать
# запрашивать числа. Обработчик исключений try-except использовать нельзя.

print("start")
it = 0
sum = 0
while(it < 2):
    print("Input nubmer: ")
    value = input()
    if value.isdigit():
        sum += int(value)
        it += 1
print(f"summa of 2 values = {sum}")