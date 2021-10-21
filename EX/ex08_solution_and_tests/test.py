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
    res = solution.lottery(5, 5, 5)
    result = 10
    assert res == result


def test_part3():
    res = solution.lottery(1, 1, 1)
    result = 5
    assert res == result


def test_part4():
    res = solution.lottery(1, 2, 3)
    result = 1
    assert res == result


def test_part5():
    res = solution.lottery(1, 1, 2)
    result = 0
    assert res == result


def test_part6():
    res = solution.lottery(1, 2, 1)
    result = 0
    assert res == result


def test_part7():
    res = solution.lottery(1, 2, 2)
    result = 1
    assert res == result


def test_part8():
    res = solution.lottery(0, 0, 0)
    result = 5
    assert res == result


def test_part9():
    res = solution.lottery(-5, -5, -5)
    result = 5
    assert res == result


def test_part10():
    res = solution.fruit_order(1, 2, 3)
    assert res == -1


def test_part11():
    res = solution.fruit_order(3, 2, 3)
    assert res == 3


def test_part12():
    res = solution.fruit_order(0, 0, 0)
    assert res == 0
