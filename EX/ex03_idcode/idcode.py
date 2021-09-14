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
        return "female"
    if number == 1 or number == 3 or number == 5:
        return "male"


def is_valid_year_number(year_number: int):
    if year_number < 0 or year_number >= 100:
        return False
    else:
        return True


def is_valid_month_number(month_number: int):
    if month_number > 12 or month_number <= 0:
        return False
    else:
        return True


def is_valid_birth_number(birth_number: int):
    if birth_number <= 0 or birth_number >= 1000:
        return False
    else:
        return True


def is_leap_year(year: int):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True


def get_full_year(gender_number: int, year_number: int):
    if gender_number == 1 or gender_number == 2:
        first_numbers = "18"
    if gender_number == 3 or gender_number == 4:
        first_numbers = "19"
    if gender_number == 5 or gender_number == 6:
        first_numbers = "20"
    if year_number < 10:
        x = "0"
        second_numbers = x + str(year_number)
    else:
        second_numbers = str(year_number)
    return int(first_numbers + second_numbers)


def get_birth_place(birth_number: int):
    if birth_number <= 0 or birth_number > 999:
        return "Wrong input!"
    if 0 < birth_number <= 10:
        return "Kuressaare"
    if (10 < birth_number <= 20) or (271 <= birth_number <= 370):
        return "Tartu"
    if (21 <= birth_number <= 220) or (471 <= birth_number <= 710):
        return "Tallinn"
    if 371 <= birth_number <= 420:
        return "Narva"
    if 421 <= birth_number <= 470:
        return "Pärnu"
    if 221 <= birth_number <= 270:
        return "Kohtla-Järve"
    if 771 <= birth_number <= 999:
        return "undefined"


print("\nFind ID code:")
print(find_id_code(""))  # -> "Not enough numbers!"
print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

print("\nGender number:")
for i in range(9):
    print(f"{i} {is_valid_gender_number(i)}")
    # 0 -> False
    # 1...6 -> True
    # 7...8 -> False

print("\nGet gender:")
print(get_gender(2))  # -> "female"
print(get_gender(5))  # -> "male"
print("\nYear number:")
print(is_valid_year_number(100))  # -> False
print(is_valid_year_number(50))  # -> true
print("\nMonth number:")
print(is_valid_month_number(2))  # -> True
print(is_valid_month_number(15))  # -> False

print("\nBorn order number:")
print(is_valid_birth_number(0))  # -> False
print(is_valid_birth_number(1))  # -> True
print(is_valid_birth_number(850))  # -> True

print("\nLeap year:")
print(is_leap_year(1804))  # -> True
print(is_leap_year(1800))  # -> False
print("\nGet full year:")
print(get_full_year(1, 28))  # -> 1828
print(get_full_year(4, 85))  # -> 1985
print(get_full_year(5, 1))  # -> 2001
print("\nChecking where the person was born")
print(get_birth_place(0))  # -> "Wrong input!"
print(get_birth_place(1))  # -> "Kuressaare"
print(get_birth_place(273))  # -> "Tartu"
print(get_birth_place(220))  # -> "Tallinn"
