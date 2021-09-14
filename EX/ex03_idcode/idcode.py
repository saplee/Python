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

def is_valid_month_number(month_number: int):
    if month_number>12 or month_number<=0:
        return False
    else:
        return True

def is_valid_birth_number(birth_number: int):
    if birth_number<=0 or birth_number>=1000:
        return False
    else:
        return True















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