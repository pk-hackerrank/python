# Importing datetime module.
import datetime
# Getting the input of no of test cases to run
no_of_test_cases = int(input())
# Looping through the test cases.
for _ in range(no_of_test_cases):
    # Getting the first time string
    first_time_str = input().strip()
    # Getting the second time string
    second_time_str = input().strip()
    # Converting into datetime format 
    first_time = datetime.datetime.strptime(first_time_str, "%a %d %b %Y %H:%M:%S %z")
    second_time = datetime.datetime.strptime(second_time_str, "%a %d %b %Y %H:%M:%S %z")
    # Calculating the timedelta 
    time_diff_seconds = datetime.timedelta.total_seconds(first_time - second_time)
    # Converting to int and printing in absolute format.
    print(abs(int(time_diff_seconds)))