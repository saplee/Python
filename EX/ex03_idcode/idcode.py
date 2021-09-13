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


print(find_id_code(""))
print(find_id_code("123456789123456789"))
print(find_id_code("ID code is: 49403136526"))
print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))

