def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [54.32, 'Строка', False]
values_list_2 = ['Hello', -5]
values_dict = {"a" : True, "b" : False, "c" : None}
print_params()
print_params(True, 3, "string")
print_params(values_list)
print_params(*values_list)
print_params(values_list_2)
print_params(*values_list_2)
print_params(*values_list_2, 43)
print_params(values_dict, 5)
print_params(*values_dict)
print_params(**values_dict)