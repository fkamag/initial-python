reproved_students = []

with open('file.txt') as filename:
    for line in filename:
        student = line
        student = student.split(' ')
        if int(student[1]) < 6:
            reproved_students.append(student[0] + '\n')

with open("reprovedStudents.txt", mode='w') as reprovedStudentFiles:
    reprovedStudentFiles.writelines(reproved_students)

with open("reprovedStudents.txt", mode='r') as reprovedStudents:
    for student in reprovedStudents:
        print(student)