immutable_var = 1, True, "Hello", [1, True, "Hello"]
print(immutable_var)
immutable_var[-1][-1] = False
print(immutable_var)
mutable_list = [1, True, "Hello", [1, True, "Hello"]]
print(mutable_list)
mutable_list[0] = False
print(mutable_list)
