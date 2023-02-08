# 1.	Напишите программу, используя 10 функции и методы, связанные со строками

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


# separator
def join_method():
    separator = ".."
    output = separator.join("am")
    joined = separator.join(["Hello", "my", "dear", "friend"])
    print(f"{output} {joined} ", end=" ")


def capitalize_method(input: str):
    output = input.capitalize()
    print(output)


def count_method(input: str):
    # substring = "o"
    substring = ""
    # value = input.count(substring)
    value = input.count(substring)
    print(f"count of `{substring}` equal {value}, len of `{input}` is {len(input)}")


def split_method(input: str):
    splitted = input.split(sep=" ", maxsplit=-1)
    print(splitted)


def swapcase_method(input: str):
    output = input.swapcase()
    print(output)


def title_method(input: str):
    value = input.title()
    print(value)


def replace_method(input: str, old: str, value: str):
    replaced = input.replace(old, value)
    print(replaced)

# index_method()
# format_method()
# find_method()
# join_method()
# capitalize_method("if he cleaned the entire beach, more plastic would cover it the next day after the tide had come in. ")
# count_method("hello from python, hello")
# split_method("Lose away off why half led have near bed")
# swapcase_method("Lose away off why half led have near bed")
# title_method("Lose, away off why half led have near bed")
# replace_method("Dare as name just when with it body.", old="name", value="Deku")