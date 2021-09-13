"""Primes identifier."""


def is_prime_number(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    if number <= 1:
        return False
    return True


print(is_prime_number(1))
print(is_prime_number(89))
print(is_prime_number(23))
print(is_prime_number(4))
print(is_prime_number(7))
print(is_prime_number(88))
