import solution


def test_part1():
    for number in range(18, 26):
        first_result = solution.students_study(number, False)
        result = True
        assert first_result == result
    for number in range(18, 26):
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
