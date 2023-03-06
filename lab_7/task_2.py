# 2. В аккаунте социальной сети одного звезды прокомментировали
# фотографию. Некоторые посетители оставляли несколько комментариев.
# Требуется по списку комментариев определить уникальное число
# комментаторов. Комментарии поступают на вход программы в формате:
# имя 1: комментарий 1
# имя 2: комментарий 2
# ...
# имя N: комментарий N
# пока не будет введена пустая строка. Также полагается, что имена у разных
# комментаторов не совпадают. Вывести на экран общее число уникальных
# комментаторов.
# unique comment, username

comments_user_name = {"Hello": "seURICen"}
comments_user_name.update({"Hi": "seURICen"})
comments_user_name.update({"Hey": "seURICen"})
comments_user_name.update({"Bye": "SYmEdgyr"})
comments_user_name.update({"Anyway": "nhaNTrub"})

def _find_unique_commentators(comments: dict):
    temp = []
    updated = dict()
    for key, value in comments.items():
        if value not in temp:
            temp.append(value)
            updated[key] = value
    return updated

unique = _find_unique_commentators(comments_user_name)
print(f"unique commentators: {len(unique)}")