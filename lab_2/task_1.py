class Person : 
    name = "Almas"
    second_name = "Mendybayev"
    age = 23
    # age = 22

student = Person
print(student.name)
print(student.second_name)
print(student.age)

print("Input text:")
text = input()
print("Inputed text: " + text)

if student.age < 10:
    print("if block student age < than 10")
elif student.age == 22:
    print("elif block " + str(student.age))
else:
    print("else block " + str(student.age))

# Что должна включать программа:
# - ФИО студента и любая дополнительная информация про студента 
# - использовать функцию print() 
# - условные операторы (if else elif)
# - ввод данных
# - комментарий
