def check_key_on_existing(_dict: dict, _key: str):
    keys = _dict.keys()
    for item in keys:
        if item == _key:
            return True
    return False


contactBook = {"Tom": 78, "Anne": 45, "Jhone": 7845}

# while True:
#     print("Input contact name: ", end=" ")
#     name = input()
#     if len(name) == 0 or name == "":
#         break
#     print("Input contact phone number: ")
#     phoneNumber = input()
#     try:
#         phone = int(phoneNumber)
#         contactBook.update([(name, phone)])
#     except ValueError:
#         print("This is not a number")

print(contactBook)


def search_contact_nubmer_by_name(notebook: dict):
    print("Input contact name: ")
    name = input()
    for item in notebook:
        if name == item:
            return f"{name} phone nubmer is {notebook.get(item)}"
    return "Нет в телефонной книге"

nubmer = search_contact_nubmer_by_name(contactBook)
print(nubmer)