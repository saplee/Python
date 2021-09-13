"""Math."""


def ects(eap, weeks):
    """Implement a function to know how many hours are needed per week if each ECTS is 26 hours. If it's not possible in time then return a string "Impossible."""
    hours = eap * 26
    if weeks == 0:
        return "Impossible!"
    hours_per_week = hours / weeks
    if hours_per_week > 168:
        return "Impossible!"
    else:
        return hours_per_week


print(ects(30, 12))
print(ects(1, 1))
print(ects(1, 0))


def average(x, y, z, c):
    """Implement a function that has 4 numeric parameters. Each parameter must be multiplied by number of its position in the function (x, y, z = 1, 2, 3). Calculate and return the average."""
    sum1 = (x * 1 + y * 2 + z * 3 + c * 4) / 4
    return sum1


print(average(0, 0, 0, 4))
print(average(1, 2, 3, 4))
print(average(5, 0, 5, 1))


def clock(d, h, m, s, ):
    """Implement a function that has 4 numeric parameters. The values are: days, hours, minutes, seconds. Calculate how many minutes are in total and return the value."""
    days_to_minute = 24 * d * 60
    hours_to_minute = 60 * h
    second_to_minute = s / 60
    hours = days_to_minute + hours_to_minute + m + second_to_minute
    return hours


print(clock(1, 24, 60, 60))
print(clock(0, 0, 0, 60))
print(clock(0, 0, 1, 60))
