# 2. Создайте кортеж-матрешку, в который поместите два элемента: целое
# число и вложенный кортеж, в который поместите еще два элемента:
# вещественное число и вложенный кортеж, в который поместите еще
# два элемента: комплексное число и вложенный кортеж, в который
# поместите еще два элемента: строку и пустой кортеж. Выведите на
# экран конечную строку

_tuple = (50, (0.5, (complex(3), ("hello", ()))))
print(_tuple)