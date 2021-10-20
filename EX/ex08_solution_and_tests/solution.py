def students_study(time: int, coffee_needed: bool) -> bool:
    """Return True if students study in given circumstances."""
    if 5 <= time <= 17 and coffee_needed is True:
        return True
    if 18 <= time <= 24:
        return True
    else:
        return False
