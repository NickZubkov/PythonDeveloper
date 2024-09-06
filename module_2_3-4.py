my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
idx = 0
while idx < len(my_list):
    if my_list[idx] > 0:
        print(my_list[idx])
        idx += 1
        continue
    elif my_list[idx] == 0:
        idx += 1
        continue
    else:
        break

