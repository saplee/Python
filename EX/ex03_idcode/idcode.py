def find_id_code(string):
    id_code = ""
    for number in string:
        if number.isdigit():
            id_code += number
    if len(id_code) < 11:
        return "Not enough numbers!"
    if len(id_code) > 11:
        return "Too many numbers!"
    else:
        return id_code


def is_valid_gender_number(year_number: int):
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if year_number > 6 or year_number <= 0:
        return False
    else:
        return True


def get_gender(number: int):
    if number == 2 or number == 4 or number == 6:
        return "Female"
    if number == 1 or number == 3 or number == 5:
        return "Male"


def is_valid_year_number(year_number: int):
    new_numbres=str(year_number)
    if len(new_numbres)>=3:
        return False
    else:
        return True
