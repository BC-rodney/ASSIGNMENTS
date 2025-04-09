students = ["Peter", "Joy", "Umar", "Musa"]
subjects = ["Eng","Maths","Sci","Arts"]

average = 0
class_average = 0
for student in students:
    print(student)
    total = 0
    total_score = 0
    for subject in subjects:
        score = int(input(f"\t{subject}: "))
        total += score
        total_score += total

    average = total / 4  
        
    print(f"Total = {total}") 
    print(f"Average = {average}\n")

class_average = total_score / 4  
print(f"Class Average = {class_average}")       




