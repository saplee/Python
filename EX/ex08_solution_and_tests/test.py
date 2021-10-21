"""Tests."""
import solution


def test_part1():
    for number in range(18, 25):
        first_result = solution.students_study(number, False)
        result = True
        assert first_result == result
    for number in range(18, 25):
        first_result = solution.students_study(number, True)
        result = True
        assert first_result == result
    for number2 in range(1, 5):
        res = solution.students_study(number2, False)
        result = False
        assert res == result
    for number3 in range(1, 5):
        res = solution.students_study(number3, True)
        result = False
        assert res == result
    for number4 in range(5, 18):
        res = solution.students_study(number4, True)
        result = True
        assert res == result
    for number4 in range(5, 18):
        res = solution.students_study(number4, False)
        result = False
        assert res == result


def test_part2():
    """Test."""
    res = solution.lottery(5, 5, 5)
    result = 10
    assert res == result


def test_part3():
    """Test."""
    res = solution.lottery(1, 1, 1)
    result = 5
    assert res == result


def test_part4():
    """Test."""
    res = solution.lottery(1, 2, 3)
    result = 1
    assert res == result


def test_part5():
    """Test."""
    res = solution.lottery(1, 1, 2)
    result = 0
    assert res == result


def test_part6():
    """Test."""
    res = solution.lottery(1, 2, 1)
    result = 0
    assert res == result


def test_part7():
    """Test."""
    res = solution.lottery(1, 2, 2)
    result = 1
    assert res == result


def test_part8():
    """Test."""
    res = solution.lottery(0, 0, 0)
    result = 5
    assert res == result


def test_part9():
    """Test."""
    res = solution.lottery(-5, -5, -5)
    result = 5
    assert res == result


def test_part10():
    """Test."""
    res = solution.fruit_order(1, 2, 3)
    assert res == -1


def test_part11():
    """Test."""
    res = solution.fruit_order(3, 2, 3)
    assert res == 3


def test_part12():
    """Test."""
    res = solution.fruit_order(0, 0, 0)
    assert res == 0


def test_part13():
    """Test."""
    res = solution.fruit_order(0, 1, 70)
    assert res == -1


def test_part14():
    """Test."""
    res = solution.fruit_order(900, 0, 900)
    assert res == 900


def test_part15():
    """Test."""
    res = solution.fruit_order(45, 0, 50)
    assert res == -1


def test_part16():
    """Test."""
    res = solution.fruit_order(45, 10, 95)
    assert res == 45


def test_part17():
    """Test."""
    res = solution.fruit_order(1, 5, 25)
    assert res == 0


def test_part18():
    """Test."""
    res = solution.fruit_order(45, 10, 95)
    assert res == 45


def test_part19():
    """Test."""
    res = solution.fruit_order(100, 5, 7)
    assert res == 2


def test_part20():
    """Test."""
    res = solution.fruit_order(45, 0, 30)
    assert res == 30


def test_part21():
    """Test."""
    res = solution.fruit_order(0, 10, 5)
    assert res == 0


def test_part22():
    """Test."""
    res = solution.fruit_order(7, 0, 10)
    assert res == -1


def test_part23():
    """Test."""
    res = solution.fruit_order(0, 10, 0)
    assert res == 0


def test_part24():
    """Test."""
    res = solution.fruit_order(8, 0, 0)
    assert res == 0


def test_part25():
    """Test."""
    res = solution.fruit_order(50, 50, 5665656565)
    assert res == -1


def test_part26():
    """Test."""
    res = solution.fruit_order(3, 3, 0)
    assert res == 0


def test_part27():
    """Test."""
    res = solution.fruit_order(50, 50, 270)
    assert res == 20


def test_part28():
    """Test."""
    res = solution.fruit_order(2000, 1000, 6100)
    assert res == 1100


def test_part29():
    """Test."""
    res = solution.fruit_order(0, 5, 4)
    assert res == -1


def test_part30():
    """Test."""
    res = solution.fruit_order(0, 5, 25)
    assert res == 0


def test_part31():
    """Test."""
    res = solution.fruit_order(2, 2000, 1008)
    assert res == -1
