students = []

noofstudents = 3

nooftests = 3
for student in range(noofstudents):
    student_name =input(f"Student {student + 1} : ")
    students.append(student_name)
    
    total = 0
    for score in range(nooftests):
        scores = []
        test_score = int(input(f"Test{score + 1}: "))
        scores.append(test_score)
        total += test_score

    print(f"Total = {total}")
    average = total / 3
    print(f"Average = {average}")
     
