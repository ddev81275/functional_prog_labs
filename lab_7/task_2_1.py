# 1. В первой строке содержится число N — число элементов в словаре. Дан
# список (словарь) стран и рек, протекающих в каждой стране. Затем даны
# названия рек (в виде списка). Выполните задания:
# 1) Для каждой реки укажите, в какой стране она протекает.
# 2) Проверьте, есть ли введенное название реки в словаре
# (вывести есть или нет)
# 3) Добавьте новую пару страна-река в словарь.

rivers_and_country = []

county_rivers_dictionary = {
    "Kz": ["Ile", "Ertis", "Syrdariya", "Ishim", "Zhem", "Aksy"],
    "China": ["Yangtze", "Yellow", "Menkong", "Lancang"],
    "USA": ["Missisipy", "Missury", "Gila", "Yellowstone"]
}

rivers = ["Ile", "Ertis", "Syrdariya", "Ishim", "Zhem", "Aksy", "Yangtze", "Yellow", "Menkong", "Lancang", "Missisipy",
          "Missury", "Gila", "Yellowstone"]


def _create_river_country_list(rivers: list, county_rivers_dist: dict, rivers_and_counry: list):
    for item in rivers:
        river_name = item
        for i in county_rivers_dist:
            river_location = county_rivers_dist.get(i)
            if river_location.__contains__(river_name):
                rivers_and_counry.append([river_name, i])

def _check_river_name_on_existing(rivers_dict: dict, river_name: str):
    rivers = rivers_dict.values()
    for item in rivers:
        for name in item:
            if name == river_name:
                print("ok")
_create_river_country_list(rivers, county_rivers_dictionary, rivers_and_country)
# for item in rivers_and_country:
#     print(item)

_check_river_name_on_existing(county_rivers_dictionary, "Ile")
