#https://www.hackerrank.com/contests/assessment-23-2-1676278643/challenges/grading/submissions/code/1406763107

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i]< 38:
            continue
        dist = 5-grades[i]%5
        if dist <= 2:
            grades[i] = grades[i]+dist
    return grades
