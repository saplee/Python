"""Create schedule from the given file."""
import re


def create_dictionary(input_string: str):
    """making dict."""
    my_dict = {}
    pattern = r'\s([0-9]{1,2})[^0-9](\d{1,2})[\s]+([A-Za-z]+)'
    match = re.findall(pattern, input_string.lower())
    for word in match:
        hour = word[0]
        minutes = word[1]
        activity = word[2]
        if 0 <= int(hour) < 24 and 0 <= int(minutes) < 60:
            if int(minutes) < 10 and len(minutes) == 1:
                minutes = "0" + str(minutes)
            if len(hour) == 1:
                hour = "0" + hour
            time = f"{hour}:{minutes}"
            if time not in my_dict:
                my_dict[time] = activity
            if activity not in my_dict[time]:
                my_dict[time] = my_dict[time] + ", " + activity
    return sorted(my_dict.items())


def new_clock_dict(tup_list):
    """making new dict."""
    new_dict = {}
    for word in tup_list:
        clock = word[0]
        value = word[1]
        patter = r'(\d+):(\d+)'
        match = re.search(patter, clock)
        hour = int(match.group(1))
        minutes = match.group(2)
        if int(hour) == 12:
            time = f"{hour}:{minutes} PM"
        if 12 < int(hour) < 24:
            time = f"{hour - 12}:{minutes} PM"
        if 0 < int(hour) < 12:
            time = f"{hour}:{minutes} AM"
        if hour == 0:
            time = f"{int(hour) + 12}:{minutes} AM"
        new_dict[time] = value
    return new_dict


def create_table(my_dict):
    """Create table."""
    num_a = 0
    num_b = 0
    table = ""
    word_list = []
    other_list = []
    if my_dict == {}:
        table += "-" * (len("No items found") + 4)
        table += f"\n|  time | items  |\n"
        table += "-" * (len("No items found") + 4)
        table += "\n| No items found |\n"
        table += "-" * (len("No items found") + 4)
    else:
        for key in my_dict.keys():
            if len(key) == 7:
                num_a += 1
            if len(key) == 8:
                num_b += 1
        if num_b == 0:
            for key, value in my_dict.items():
                word_list.append(key + value)
            x = len((max(word_list, key=len))) + 7
            table += "-" * x 
            for value in my_dict.values():
                other_list.append(value)
            y = len(max(other_list, key=len))
            table += f"\n|    time | items {' ' * (y - len('items'))}|\n"
            table += "-" * x
            for key, value in my_dict.items():
                table += f"\n| {str(key)} | {str(value.lower())}{' ' * (y - len(value))} |"
            table += f"\n{'-' * x}\n"
        if num_b > 0:
            for key, value in my_dict.items():
                word_list.append(key + value)
            x = max(word_list, key=len)
            m = re.search(r'\d{1,2}:\d{1,2}', x)
            if len(m.group()) == 4:
                f = len(x) + 8
            else:
                f = len(x) + 7
            table += "-" * f
            for value in my_dict.values():
                other_list.append(value)
            y = len(max(other_list, key=len))
            table += f"\n|     time | items {' ' * (y - len('items'))}|\n"
            table += "-" * f
            for key, value in my_dict.items():
                if len(str(key)) == 7:
                    table += f"\n|  {str(key)} | {str(value.lower())}{' ' * (y - len(value))} |"
                else:
                    table += f"\n| {str(key)} | {str(value.lower())}{' ' * (y - len(value))} |"
            table += f"\n{'-' * f}\n"
    return table


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    with open(input_filename) as f:
        file = f.read()
        f.close()
        print(f.closed)

    with open(output_filename, "w") as f:
        f.write(create_schedule_string(file))
        print(f.closed)


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    return create_table(new_clock_dict(create_dictionary(input_string)))


if __name__ == '__main__':
    print(create_schedule_string("tere 1:1 f 13:14 gfdgdgdg"))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
