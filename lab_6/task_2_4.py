# 4. Вводятся имена студентов в одну строчку через пробел. На их основе
# формируется кортеж. Отобразите на экране все имена из этого кортежа,
# которые содержат фрагмент "ва". Имена выводятся в одну строку через
# пробел.

students = {"Вавилов", "Вавилова", "Васильев", "Иванов", "Смирнов"}

for item in students:
    if(item.lower().__contains__("ва")):
        print(item)
