"""Primes identifier."""


def is_prime_number(number):
    """Check if the parameter number is a prime number.Conditions:
    1. If number is a prime number then return boolean True
    2. If number is not a prime number then return boolean False
    :param number: the number for check.
    :return: boolean True if number is a prime number or False if number is not a prime number.
    """
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
