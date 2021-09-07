"""add."""


def add(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def div(x, y):
    return x / y


def modulus(x, y):
    return x % y


def floor_div(x, y):
    return x // y


def exponent(x, y):
    return x ** y


def first_greater_or_equal(x, y):
    if x >= y:
        return True
    else:
        return False


def second_less_or_equal(x, y):
    if x >= y:
        return True
    else:
        return False


def x_is_y(x, y):
    if x == y:
        return True
    else:
        return False


def x_is_not_y(x, y):
    if x != y:
        return True
    else:
        return False


def if_else(a, b, c, d):
    sum1 = a * b
    sum2 = c / d
    if sum1 > sum2:
        return sum1
    if sum1 == sum2:
        return 0
    if sum1 < sum2:
        return sum2


def surface(a, b):
    return a * b


def volume(a, b, c):
    return a * b * c


print(add(1, -2))
print(sub(5, 5))
print(multiply(5, 5))
print(div(15, 5))
print(modulus(9, 3))
print(floor_div(3, 2))
print(exponent(5, 5))
print(first_greater_or_equal(1, 2))
print(second_less_or_equal(5, 5))
print(x_is_y(1, 2))
print(x_is_not_y(1, 2))
print(if_else(1, 3, 5, 99))
print(if_else(2, 1, 10, 5))
print(surface(1, 2))
print(volume(5, 5, 5))
