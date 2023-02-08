# 2.Напишите программу, в которой предлагается вводить учащихся различных груп,
# посещающих секции по программированию. Требуется упорядочить список по возрастанию классов.
# Распечатать список фамилий и классов.

it = 0
common = []
while it < 2:
    print("Second name: ")
    second_name = input()
    print("Rang: ")
    rang = input()
    if rang.isdigit():
        common.append((second_name, rang))
        it += 1

print(common)
_sorted = sorted(common, key=lambda item: item[1], reverse=False)
print(_sorted)