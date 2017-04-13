# In this we learn about the dictionary
if __name__ == '__main__':
    n = int(input())
    student_marks = {} # Initiailizing a dictionary
    for _ in range(n): # if temporary variable to be created for name sake we can use _
        name, *line = input().split() # which assigns first value to 'name' and rest of them to *line in list format
        scores = list(map(float, line))
        student_marks[name] = scores # Assigning values for dictionary
    query_name = input()
    marks = student_marks[query_name]
    avg = (marks[0] + marks[1] + marks[2])/3
    print('{0:.2f}'.format(round(avg,2))) # Round to n decimal places and format to the same n decimal places.