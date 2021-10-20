def students_study(time: int, coffee_needed: bool) -> bool:
    """Return True if students study in given circumstances."""
    if 5 <= time <= 17 and coffee_needed is True:
        return True
    if 18 <= time <= 24:
        return True
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """Return Lottery victory result 10, 5, 1, or 0 according to input values."""
    if a == b == c == 5:
        return 10
    if a == b == c != 5:
        return 5
    if b != a and c != a:
        return 1
    if b == a or c == a:
        return 0
