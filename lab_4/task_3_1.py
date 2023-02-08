# 1)	Вводится строка, включающая строчные и прописные буквы.
# Требуется вывести ту же строку в одном регистре, который зависит от того, каких букв больше.
# При равном количестве преобразовать в нижний регистр. Например, вводится строка "HeLLo World",
# она должна быть преобразована в "hello world", потому что в исходной строке малых букв больше.
# Необходимо свой пример привести. В коде используйте цикл for, строковые методы upper()
# (преобразова	ние к верхнему регистру) и lower() (преобразование к нижнему регистру),
# а также методы isupper() и islower(), проверяющие регистр строки или символа.


def lower_counter(input: str):
    lower = 0
    for item in input:
        if item.islower():
            lower += 1
    return lower

def upper_counter(input: str):
    upper = 0
    for item in input:
        if item.isupper():
            upper += 1
    return upper

def do(input: str):
    upper = upper_counter(input)
    lower = lower_counter(input)
    if lower > upper:
        updated = ""
        for item in input:
            updated += item.lower()
        print(updated)
        return
    elif upper > lower:
        updated = ""
        for item in input:
            updated += item.upper()
        print(updated)
        return
    else:
        print(input)

do("HeLLo World")
do("HELLO World")