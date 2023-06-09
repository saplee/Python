"""Test."""
import solution


def test_part1():
    """Test."""
    input_amount = 1000
    res = solution.generate_list(input_amount, "string")
    expected_len = 1000
    assert len(res) == expected_len


def test_part2():
    """Test."""
    input_amount = 1
    res = solution.generate_list(input_amount, "int")
    expected_len = 1
    assert len(res) == expected_len


def test_part3():
    """Test."""
    input_amount = 0
    res = solution.generate_list(input_amount, "float")
    expected_len = 0
    assert len(res) == expected_len


def test_part4():
    """Test."""
    input_amount = 1
    res = solution.generate_list(input_amount, "set")
    expected_len = 1
    assert len(res) == expected_len


def test_part5():
    """Test."""
    input_amount = 1
    res = solution.generate_list(input_amount, "dict")
    expected_len = 1
    assert len(res) == expected_len


def test_part6():
    """Test."""
    res = solution.generate_list(2, "dict")
    result = 2
    assert len(res) == result
    assert type(res[0]) == dict


def test_part7():
    """Test."""
    input_amount = 1
    res = solution.generate_list(input_amount, "list")
    expected_len = 1
    assert len(res) == expected_len


def test_part8():
    """Test."""
    res = solution.generate_list(2, "set")
    result = 2
    assert len(res) == result
    assert type(res[0]) == set


def test_part9():
    """Test."""
    res = solution.generate_list(2, "int")
    result = 2
    assert len(res) == result
    assert type(res[0]) == int


def test_part10():
    """Test."""
    res = solution.generate_list(2, "list")
    result = 2
    assert len(res) == result
    assert type(res[0]) == list


def test_part11():
    """Test."""
    res = solution.generate_list(1, "string")
    assert type(res[0]) == str


def test_part12():
    """Test."""
    res = solution.generate_list(2, "float")
    result = 2
    assert len(res) == result
    assert type(res[0]) == float


def test_par13():
    """Test."""
    res = solution.generate_list(2, "tuple")
    result = 2
    assert len(res) == result
    assert type(res[0]) == tuple


def test_part1_second():
    """Test."""
    res = solution.generate_combined_list([])
    result = 0
    assert len(res) == result


def test_part2_second():
    """Test."""
    res = solution.generate_combined_list(
        [(50000, "float"), (20000, "list"), (4, "string"), (2, "dict"), (2, "set"), (2, "int")])
    result = 70010
    assert len(res) == result


def test_part3_second():
    """Test."""
    res = solution.generate_combined_list([(1, "int")])
    assert type(res[0]) == int


def test_part4_second():
    """Test."""
    res = solution.generate_combined_list([(1, "float")])
    assert type(res[0]) == float


def test_part5_second():
    """Test."""
    res = solution.generate_combined_list([(1, "string")])
    assert type(res[0]) == str


def test_part6_second():
    """Test."""
    res = solution.generate_combined_list([(1, "list")])
    assert type(res[0]) == list


def test_part7_second():
    """Test."""
    res = solution.generate_combined_list([(1, "dict")])
    assert type(res[0]) == dict


def test_part8_second():
    """Test."""
    res = solution.generate_combined_list([(1, "set")])
    assert type(res[0]) == set


def test_part9_second():
    """Test."""
    res = solution.generate_combined_list([(8, "int")])
    result = 8
    assert len(res) == result


def test_part1_third():
    """Test."""
    res = solution.generate_combined_list_unique([(2, "int"), (3, "float"), (1, "string")])
    result = 6
    assert len(res) == result


def test_part2_third():
    """Test."""
    res = solution.generate_combined_list_unique([(2, "int")])
    assert res[0] != res[1]


def test_part3_third():
    """Test."""
    res = solution.generate_combined_list_unique([(2, "float")])
    assert res[0] != res[1]


def test_part4_third():
    """Test."""
    res = solution.generate_combined_list_unique([(5, "string")])
    assert len(res) == len(set(res))


def test_part5_third():
    """Test."""
    res = solution.generate_combined_list_unique([])
    result = []
    assert len(res) == len(result)


def test_part6_third():
    """Test."""
    res = solution.generate_combined_list_unique([(5, "int")])
    assert len(set(res)) == len(res)


def test_part7_third():
    """Test."""
    res = solution.generate_combined_list_unique([(5, "float")])
    assert len(res) == len(set(res))


def test_part8_third():
    """Test."""
    res = solution.generate_combined_list_unique([(1, "string"), (1, "float"), (1, "int")])
    assert (type(res[2]), type(res[1]), type(res[0])) == (str, float, int)


def test_part9_third():
    """Test."""
    res = solution.generate_combined_list_unique([(0, "string"), (0, "float"), (0, "int")])
    result = 0
    assert len(res) == result


def test_part10_third():
    """Test."""
    res = solution.generate_combined_list_unique([(20, "string"), (10, "float"), (40, "int")])
    result = 70
    assert len(res) == result
