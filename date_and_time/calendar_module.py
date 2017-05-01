# Importing calendar
import calendar
# taking the month, day and year from the input string by split and map with int
month, day, year = map(int,input().strip().split())
# Getting the index of the week
dayOfWeekIndex = calendar.weekday(year, month, day)
# Getting the week of day by giving the index of week
dayOfWeekByName = calendar.day_name[dayOfWeekIndex]
# Printing the day in upper case.
print(dayOfWeekByName.upper())