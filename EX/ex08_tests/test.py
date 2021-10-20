"""Test."""
import solution


def test_part1():
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len


def test_part2():
    input_amount = 1
    res = solution.generate_list(input_amount, "int")
    expected_len = 1
    assert len(res) == expected_len


def test_part3():
    input_amount = 0
    res = solution.generate_list(input_amount, "float")
    expected_len = 0
    assert len(res) == expected_len


def test_part4():
    input_amount = 1
    res = solution.generate_list(input_amount, "set")
    expected_len = 1
    assert len(res) == expected_len


def test_part5():
    input_amount = 1
    res = solution.generate_list(input_amount, "dict")
    expected_len = 1
    assert len(res) == expected_len


def test_part6():
    input_amount = 1
    res = solution.generate_list(input_amount, "list")
    expected_len = 1
    assert len(res) == expected_len


def test_part1_second():
    res = solution.generate_combined_list([])
    result = 0
    assert len(res) == result


def test_part2_second():
    res = solution.generate_combined_list(
        [(50000, "float"), (20000, "list"), (4, "string"), (2, "dict"), (2, "set"), (2, "int")])
    result = 70010
    assert len(res) == result


def test_part3_second():
    res = solution.generate_combined_list([(1, "int")])
    assert type(res[0]) == int


def test_part4_second():
    res = solution.generate_combined_list([(1, "float")])
    assert type(res[0]) == float


def test_part5_second():
    res = solution.generate_combined_list([(1, "string")])
    assert type(res[0]) == str


def test_part6_second():
    res = solution.generate_combined_list([(1, "list")])
    assert type(res[0]) == list


def test_part7_second():
    res = solution.generate_combined_list([(1, "dict")])
    assert type(res[0]) == dict


def test_part8_second():
    res = solution.generate_combined_list([(1, "set")])
    assert type(res[0]) == set
