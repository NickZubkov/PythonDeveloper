import random
def get_password():
    random_number = random.randint(3, 20)
    print(random_number)
    password = []
    for i in range(1, random_number):
        for j in range(i, random_number):
            if i == j:
                continue
            if random_number % (i + j) == 0:
                password.append([i, j])
    return password
print(get_password())
print(get_password())
print(get_password())
print(get_password())