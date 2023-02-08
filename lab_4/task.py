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


# index_method()
# format_method()
# find_method()
# join_method()
# capitalize_method("if he cleaned the entire beach, more plastic would cover it the next day after the tide had come in. ")
# count_method("hello from python, hello")
