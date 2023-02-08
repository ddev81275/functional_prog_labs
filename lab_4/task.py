# 1.	Напишите программу, используя 10 функции и методы, связанные со строками
# 19Hvu5ANdm
# JWKhvwtL6I
# kOmThMTuZD
# Snrq4iwXoc
# y2ZUp5ys2z
# IcJDqp96uy
# Cz86JMlj09
# u5CnolwILz
# RJvxncyvhM
# JIlFWNh46C
def index_method():
    value = "JWKhvwtL6I, 19Hvu5ANdm"
    index = value.index("K")
    print(index, end=" ")


def format_method():
    value = "# RJvxncyvhM {0} # JIlFWNh46C {1}"
    output = value.format("u5CnolwILz", "JIlFWNh46C")
    print(output)


# full income
def find_method():
    value = "Cz86JMlj09"
    output = value.find("j0", 0, len(value) - 1)
    print(output)


index_method()
format_method()
find_method()
