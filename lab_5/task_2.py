# 2.	 Напишите	 программу которая	 возвращает	 список. Заранее
# подготовьте	 список	 предметов	 и	 оценок	 учащихся. Когда вы	 вводите
# имя	учащегося,	то	должны отображаться оценки	этого	учащегося.

_alex = [["Alex"], ["Math", [2, 3, 5, 4]], ["History", [3, 4, 4, 4]]]

_tom  = [["Tom"], ["Math", [4, 4, 3, 4]], ["History", [3, 3, 4, 5]]]

_anna = [["Anna"], ["Bio", [5, 4, 3, 3]], ["Geo", [3, 2, 5, 5]]]

common = []
common.append(_alex)
common.append(_tom)
common.append(_anna)

print(common)
print("Input name: ", end=" ")
name = input()
for item in common:
    if name.lower() == item[0][0].lower():
        print(item)