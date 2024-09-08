﻿from math import trunc

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    elif i == 2:
        primes.append(i)
    elif i % 2 == 0:
        not_primes.append(i)
    else:
        is_prime = True
        for j in range(1, i):
            divider = j * 2 + 1
            if divider < i and i % divider == 0:
                not_primes.append(i)
                is_prime = False
                break
        if is_prime:
            primes.append(i)
print(f'primes {primes}')
print(f'not_primes {not_primes}')