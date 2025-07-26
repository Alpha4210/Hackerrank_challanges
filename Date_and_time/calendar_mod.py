import calendar

x = list(map(int, input().split()))

day = calendar.weekday(x[2], x[0], x[1])
day_names = list(calendar.day_name)

print(day_names[day].upper())