def generate_list(amount: int, data_type: str) -> list:
    """Write a function that returns a list with amount elements of type data_type."""
    if data_type == "int":
        return [1] * amount
    if data_type == "string":
        return ["kass"] * amount
    if data_type == "set":
        return [set()] * amount
    if data_type == "list":
        return [[]] * amount
    if data_type == "float":
        return [3.14] * amount
    if data_type == "dict":
        return [{1}]
    if data_type == "tuple":
        return [(1)]
# Part 1
print(generate_list(2, 'set'))  # [set(), set()]
print(generate_list(3, 'string'))  # ["a", "kass", "a"]
print(generate_list(4, 'list'))  # [[]]
print(generate_list(5, 'int'))  # [1, 2, 3, 3, 3]
