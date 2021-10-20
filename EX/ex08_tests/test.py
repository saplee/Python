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
    res = solution.generate_combined_list([(3, "int"), (2, "dict")])
    result = 5
    assert len(res) == result


def test_part2_second():
    res = solution.generate_combined_list([])
    result = 0
    assert len(res) == result


def test_part3_second():
    res = solution.generate_combined_list([(3, "float"), (5, "list"), (4, "string"), (2, "dict"), (2, "set")])
    result = 16
    assert len(res) == result

