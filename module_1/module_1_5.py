immutable_var = 1, True, "Hello", [1, True, "Hello"]
print(immutable_var)
immutable_var[-1][-1] = False
print(immutable_var)
tmp_list = [*immutable_var]
tmp_list[0] = "I can change it"
immutable_var = tuple(tmp_list)
print(f"Changed tuple value {immutable_var}")
mutable_list = [1, True, "Hello", [1, True, "Hello"]]
print(mutable_list)
mutable_list[0] = False
print(mutable_list)
