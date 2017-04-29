# Importing namedtuple from collections
from collections import namedtuple
# Initializing counter, total_count
counter,total_count = int(input()), 0
# Initializing the student_list namedtuple
student_list = namedtuple('student_list',input().split())
# Looping through the counter
for _ in range(counter):
    # Creating student object of the namedtuple
    student = student_list(*input().split())
    # Accessing marks from student namedtuple
    total_count += int(student.MARKS)
# corrected to 2 decimal places.
print("{:.2f}".format(total_count/counter))