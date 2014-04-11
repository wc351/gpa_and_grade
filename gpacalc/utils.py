
def GetGPA(user):
    student_data = user
    grades = [(row.grade, row.credit_hours) for row in student_data]
    quality_hours = 0
    credit_hours = 0
    for grade, hours in grades:
        if grade == 'A' or grade == 'a':
            quality_hours += (4 * hours)
        elif grade == 'B' or grade == 'b':
            quality_hours += (3 * hours)
        elif grade == 'C' or grade == 'c':
            quality_hours += (2 * hours)
        elif grade == 'D' or grade == 'd':
            quality_hours += (1 * hours)
        credit_hours += hours
    gpa = round(quality_hours / credit_hours, 2)
    return gpa
