import solution


def test_part1():
    for number in range(18-26):
        first_result = solution.students_study(number, False)
        result = True
        assert first_result == result
    for number2 in range(1-5):
        res = solution.students_study(number2)
        result = False
        assert res == result