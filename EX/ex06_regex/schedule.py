"""Create schedule from the given file."""
import re


def create_dictionary(input_string: str):
    my_dict = {}
    pattern = r'([\d]{1,2})[:.!,\w](\d{1,2})[\s]+(\w+)'
    match = re.findall(pattern, input_string)
    for word in match:
        hour = int(word[0])
        minutes = word[1]
        activity = word[2]
        if 0 > hour or hour > 24 or int(minutes) > 60 or int(minutes) < 0:
            activity is None
            time is None
        else:
            if int(minutes) < 10 and len(minutes) == 1:
                minutes = "0" + str(minutes)
            time = f"{hour}:{minutes}"
            if time not in my_dict:
                my_dict[time] = activity
            if activity not in my_dict[time]:
                my_dict[time] = my_dict[time] + ", " + activity
    return sorted(my_dict.items())


def new_clock_dict(tup_list):
    new_dict = {}
    for word in tup_list:
        clock = word[0]
        value = word[1]
        patter = r'(\d+):(\d+)'
        match = re.search(patter, clock)
        hour = int(match.group(1))
        minutes = match.group(2)
        if hour == 12:
            time = f"{hour}:{minutes} PM"
        if 12 < hour <= 24:
            time = f"{hour - 12}:{minutes} PM"
        if 0 < hour < 12:
            time = f"{hour}:{minutes} AM"
        if hour == 0:
            time = f"{hour + 12}:{minutes} AM"
        new_dict[time] = value
    return new_dict


def create_table(my_dict):
    """Create table."""
    word_list = []
    for key, value in my_dict.items():
        word_list.append(key + value)
    x = len((max(word_list, key=len))) + 7
    table = ""
    table += "-" * x
    y = x - len("| time | items") - 1
    table += f"\n| time | items{' ' * y}|\n"
    table += "-" * x
    for key, value in my_dict.items():
        table += f"\n| {key} | {value} |\n"
    table += "-" * x
    return table


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    pass


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    return create_table(new_clock_dict(create_dictionary(input_string)))


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
