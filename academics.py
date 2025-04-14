students = []
while True:
    student_name = input("Enter Student Name Or 'Q' To Terminate: ")
    if student_name.upper() == 'Q':
        break

    students_course =input("Enter Student's Course: ")
    reg_no = input("Enter Student's Registration Number: ")
    gender = input("Enter Student's Gender: ")
    age = int(input("Enter Student's Age: "))

    scores = []
    for index in range(4):
        score = int(input("Enter Student's Score: "))
        scores.append(score)
    
    studentdict = {
        "name": student_name,
        "reg_number":reg_no,
        "course":students_course,
        "gender":gender,
        "age":age,
        "scores":scores
    }

    students.append(studentdict)

def display_students():
    for student in students:
        print(f'{student.get("name")}\t{student.get("reg_number")}\t{student.get("course")}\t{student.get("gender")}\t{student.get("age")}')

#print(display_students())
def studentlist_by_course():
    for student in students:
        if student["course"] == "BIT":
            print(student["name"])


print(studentlist_by_course())


