def ects(ects, weeks):
    hours = ects * 26
    hours_per_week = hours / weeks
    if hours_per_week > 168:
        return "Impossible"
    else:
        return hours_per_week


print(ects(30, 12))
print(ects(1, 1))
print(ects(1, 0))


def average(x, y, z, c):
    sum1 = (x * 1 + y * 2 + z * 3 + c * 4) / 4
    return sum1


print(average(0, 0, 0, 4))
print(average(1, 2, 3, 4))
print(average(5, 0, 5, 1))


def clock(d, h, m, s, ):
    day_minute = 24 * d * 60
    hours_minute = 60 * h
    sekund_minute = s / 60
    sum1 = day_minute + hours_minute + m + sekund_minute
    return sum1


print(clock(1, 24, 60, 60))
print(clock(0, 0, 0, 60))
print(clock(0, 0, 1, 60))