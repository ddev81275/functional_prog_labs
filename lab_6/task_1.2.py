_set = {"hello", 5, True, 0.5}

# copy
copy_set = _set.copy()
print(f"origin: {_set}")
print(f"copy: {copy_set}")

# add new item
_set.add("bye")
print(f"added new item: {_set}")

# difference
_difference = _set.difference({"hello", False, 0.5})
print(f"difference: {_difference}")

# pop
_set.pop()
print(f"pop {_set}")

# clear
_set.clear()
print(f"clear set: {_set}")
