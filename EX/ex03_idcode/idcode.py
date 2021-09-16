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


def is_valid_gender_number(gender_number: int):
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if gender_number > 6 or gender_number <= 0:
        return False
    else:
        return True


def get_gender(gender_number: int):
    if gender_number == 2 or gender_number == 4 or gender_number == 6:
        return "female"
    if gender_number == 1 or gender_number == 3 or gender_number == 5:
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
    else:
        return False


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
    if 711 <= birth_number <= 999:
        return "undefined"


def is_valid_control_number(id_code: str):
    first_number = int(id_code[0])
    second_number = int(id_code[1])
    third_number = int(id_code[2])
    fourth_number = int(id_code[3])
    fifth_number = int(id_code[4])
    sixth_number = int(id_code[5])
    seventh_number = int(id_code[6])
    eight_number = int(id_code[7])
    ninth_number = int(id_code[8])
    tenth_number = int(id_code[9])
    last_number = int(id_code[10])
    sum = 1 * first_number + 2 * second_number + 3 * third_number + 4 * fourth_number + 5 * fifth_number + 6 * sixth_number + 7 * seventh_number + 8 * eight_number + 9 * ninth_number + 1 * tenth_number
    if sum % 11 == last_number:
        return True
    else:
        return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int):
    for month in range(1, 8, 2):
        if month == month_number and day_number > 31:
            return False
    for pair_month in range(4, 7, 2):
        if pair_month == month_number and day_number > 30:
            return False
    if month_number == 8 and day_number > 31:
        return False
    if month_number == 9 and day_number > 30:
        return False
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

    full_year = int(first_numbers + second_numbers)
    if month_number == 2 and full_year % 400 == 0 and day_number > 29:
        return False
    if month_number == 2 and full_year % 4 == 0 and full_year % 100 != 0 and day_number > 29:
        return False
    if month_number == 2 and full_year % 100 == 0 and full_year % 4 != 0 and day_number > 28:
        return False
    if month_number == 2 and full_year % 100 != 0 and full_year % 4 != 0 and day_number > 28:
        return False
    else:
        return True


def is_id_valid(id_code: str):
    gender_number = int(id_code[0])
    is_valid_gender_number(gender_number)
    if is_valid_gender_number(gender_number) == False:
        return False
    year_number = int(id_code[1:3])
    if year_number > 99:
        return False
    month_number = int(id_code[3:5])
    if month_number > 12:
        return False
    day_number = int(id_code[5:7])
    if is_valid_day_number(gender_number, year_number, month_number, day_number)==False:
        return False
    if is_valid_control_number(id_code)==False:
            return False
    if len(id_code)>11 or len(id_code)<11:
        return False
    else:
        return True

def get_data_from_id(id_code: str):
    gender_number = int(id_code[0])
    year_number = int(id_code[1:3])
    day_number = id_code[5:7]
    month_number = id_code[3:5]
    birth_number = int(id_code[7:10])
    birth_place = get_birth_place(birth_number)
    if is_id_valid(id_code)==False:
        return "Given invalid ID code!"
    else:
        return f"This is a {get_gender(gender_number)} born on {day_number}.{month_number}.{str(get_full_year(gender_number, year_number))} in {birth_place}."




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
print("\nControl number:")
print(is_valid_control_number("49808270244"))  # -> True
print(is_valid_control_number("60109200187"))  # -> False, it must be 6
print("\nDay number:")
print(is_valid_day_number(4, 5, 12, 25))  # -> True
print(is_valid_day_number(3, 10, 8, 32))  # -> False
print("\nFebruary check:")
print(is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
print(is_valid_day_number(4, 8, 2, 29))  # -> True
print("\nMonth contains 30 or 31 days check:")
print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
print(is_valid_day_number(4, 18, 10, 31))  # -> True
print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)
print("\nOverall ID check::")
print(is_id_valid("49808270244"))  # -> True
print(is_id_valid("12345678901"))  # -> False
print("\nFull message:")
print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
