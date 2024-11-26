

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(number_1, number_2, number_3):
    return number_1 + number_2 + number_3

print(sum_three(2, 3, 2))