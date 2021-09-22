""""Lists."""
import random


def generate_list(amount: int, data_type: str) -> list:
    """Write a function that returns a list with amount elements of type data_type."""
    d = {"int": 0, "float": 3.14, "string": "kass", "list": [], "dict": {}, "set": set()}
    for key in d.keys():
        if key == data_type:
            return [d[data_type]] * amount


def generate_combined_list(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.
    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
    """
    data_list = {"int": 0, "float": 3.14, "string": "kass", "list": [], "dict": {}, "set": set()}
    book = {"string": 0, "int": 0, "set": 0, "list": 0, "dict": 0, "float": 0}
    result = []
    for element in inputs:
        amount = element[0]
        data_types = element[1]
        if book[data_types] < amount:
            book[data_types] = amount
    for data_type in data_list.keys():
        result += [data_list[data_type]] * book[data_type]
    return result


def generate_combined_list_unique(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
    Data types used in this function are 'int', 'float' and 'str' (string).
    The returned list can contain only unique elements.
    """
    book = {"string": 0, "int": 0, "float": 0}
    result = []
    for element in inputs:
        amount = element[0]
        data_type = element[1]
        if book[data_type] < amount:
            book[data_type] = amount
    for i in range(0, book["int"]):
        int_number = random.randint(0, 100000000)
        result += [int_number]
    for i in range(0, book["float"]):
        float_number = random.uniform(0, 10000000)
        result += [float_number]
    for i in range(0, book["string"]):
        random_number = random.randint(0, 10000000)
        random_string = str(random_number)
        result += [random_string]
    return result


def generate_combined_list_unique_advanced(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
    All the data types from the first function are used here.
    The returned list can contain only unique elements.
    """
    book = {"string": 0, "int": 0, "set": 0, "list": 0, "dict": 0, "float": 0}
    result = []
    for element in inputs:
        amount = element[0]
        data_type = element[1]
        if book[data_type] < amount:
            book[data_type] = amount
    for i in range(0, book["int"]):
        int_number = random.randint(0, 1000000000)
        result += [int_number]
    for i in range(0, book["float"]):
        float_number = random.uniform(0, 100000000)
        result += [float_number]
    for i in range(0, book["string"]):
        random_number = random.randint(0, 100000000)
        random_string = str(random_number)
        result += [random_string]
    return result


if __name__ == '__main__':
    # The given outputs are only some of possible outputs, for example for (3, 'string') in the first part an output of ["kass", "koer", "kana"] would also work.

    # Part 1
    print(generate_list(2, 'set'))  # [set(), set()]
    print(generate_list(3, 'string'))  # ["a", "kass", "a"]
    print(generate_list(1, 'list'))  # [[]]
    print(generate_list(5, 'int'))  # [1, 2, 3, 3, 3]
    print()

    # Part 2
    print(generate_combined_list([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
    print(generate_combined_list([(3, 'int'), (5, 'int')]))  # [0, 0, 0, 0, 0]
    print(generate_combined_list([(3, 'int'), (5, 'int'), (4, 'int')]))  # [100, 80, 60, 40, 20]
    print(generate_combined_list([(2, 'list'), (3, 'string')]))  # ["a", [], "a", [], "a"]
    print(generate_combined_list([(2, 'float'), (3, 'dict')]))  # [{}, {}, {}, 3.14, 3.14]
    print()
    # Part 3
    print(generate_combined_list_unique([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
    print(generate_combined_list_unique([(2, 'int'), (2, 'float'), (1, 'int')]))  # [43, 93, 4.3, 2.1]
    print()
    # Part 4
    print(generate_combined_list_unique_advanced([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
    print(generate_combined_list_unique_advanced([(2, 'list'), (3, 'string')]))  # ["a", [2], "asd", [], "abc"]
    print(generate_combined_list_unique_advanced([(2, 'float'), (3, 'dict')]))  # [{3: "abd"}, {"a": "a"}, {}, 3.14, 3.15]
    print()
