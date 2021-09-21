def generate_list(amount: int, data_type: str) -> list:
    """Write a function that returns a list with amount elements of type data_type."""
    d = {"int": 0, "float": 3.14, "string": "kass", "list": [], "dict": {}, "set": set()}
    for keys in d.keys():
        if keys == data_type:
            return [d[data_type]] * amount

def generate_combined_list(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
    """
    d = {"int": 0, "float": 3.14, "sting": "kass", "list": [], "dict": {}, "set": ()}











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
    print(generate_combined_list([(2, 'float'), (3, 'dict')]))  # [{}, {}, {}, 3.14, 3.15]
    print()
