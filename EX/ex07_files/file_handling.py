""""File."""
import csv
import datetime
import re


def read_file_contents(filename: str) -> str:
    """Read file contents into string.In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename) as f:
        data = f.read()
        f.close()
    return data


def read_file_contents_to_list(filename: str) -> list:
    """Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.

    List elements should not contain new line.

    :param filename: File to read.
    :return: List of lines.
    """
    my_list = []
    with open(filename) as f:
        for row in f:
            my_list.append(row.strip())
    return my_list


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    my_list = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            my_list.append(row)
        return my_list


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file exists, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w") as f:
        f.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w") as f:
        f.write("\n".join(lines))


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in data:
            csv_writer.writerow(row)


def merge_dates_and_towns_into_csv(dates_file: str, towns_file: str, csv_output: str) -> None:
    """
    Merge information from two files into one CSV file.

    dates_file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    towns_file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_file: Input file with names and dates.
    :param towns_file: Input file with names and towns.
    :param csv_output: Output CSV-file with names, towns and dates.
    :return: None
    """
    my_list = []
    my_dict = {}
    other_list = [["name", "town", "date"]]
    with open(dates_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        for row in csv_reader:
            my_list.append(row)
        for word in my_list:
            key = word[0]
            value = word[1]
            my_dict[key] = ["-", value]
    with open(towns_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        for row in csv_reader:
            key = row[0]
            value = row[1]
            if key in my_dict:
                my_dict[key][0] = value
            else:
                my_dict[key] = [value, "-"]
    for key, value in my_dict.items():
        new_list = []
        if value[0] == "":
            value[0] = "-"
        if value[1] == "":
            value[1] = "-"
        new_list.append(key)
        new_list.append(value[0])
        new_list.append(value[1])
        other_list.append(new_list)
    return write_csv_file(csv_output, other_list)


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """Read csv file into list of dictionaries.Header line will be used for dict keys.

    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:

    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    if read_csv_file(filename) == []:
        return []
    else:
        result = []
        read_file = read_csv_file(filename)
        keys = read_file.pop(0)
        for row in read_file:
            row_dict = {}
            for key, column_number in zip(keys, range(len(keys))):
                row_dict[key] = row[column_number]
            result.append(row_dict)
    return result


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    if data == []:
        with open(filename, "w") as f:
            f.write("")
    else:
        fields = []
        for word in data:
            for key in word.keys():
                if key not in fields:
                    fields.append(key)
        with open(filename, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fields)
            writer.writeheader()
            writer.writerows(data)


def new_list(filename):
    """"Making new list."""
    new_dict = []
    date_count = 0
    pattern = r'\d{2}[.]\d{2}[.]\d{4}'
    read_list = read_csv_file_into_list_of_dicts(filename)
    for dicts in read_list:
        for key, value in dicts.items():
            match = re.search(pattern, value)
            match2 = re.search(r'date[0-9]?', key)
            if match2 is not None and match is None and value != "-":
                date_count += 1
    for dicts in read_list:
        for key, value in dicts.items():
            if value == "-":
                dicts[key] = None
            if value.isdigit():
                dicts[key] = int(value)
            match = re.search(pattern, value)
            if match is not None and date_count == 0:
                dicts[key] = datetime.datetime.strptime(value, "%d.%m.%Y").date()
        new_dict.append(dicts)
    return new_dict


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,01.01.2020

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    age_count = 0
    result = []
    for dicts in new_list(filename):
        for key, value in dicts.items():
            if key == "age" and isinstance(value, str) and not value.isdigit() and value != "-":
                age_count += 1
    for my_dict in new_list(filename):
        for key, value in my_dict.items():
            if age_count > 0:
                if key == "age":
                    my_dict[key] = str(value)
        result.append(my_dict)
    return result
