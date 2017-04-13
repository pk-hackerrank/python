if __name__ == '__main__':
    student_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])
    
    scoreList = list(set([x[1] for x in student_list])) # set with remove duplicates, then convert to list
    scoreList.sort() # Sort the list to find out the second smallest number
    lowest_grade = scoreList[1] # Retrieve the second smallest number i.e. grade
    final_student_list = [x[0] for x in student_list if x[1] == lowest_grade] # Retrieving only names of students who have got the second smallest grade
    final_student_list.sort() # Sort the list since the problem statement wanted to print in alphabetical order.
    for x in final_student_list:
        print(x)
