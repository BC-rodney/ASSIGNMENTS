students = ["Peter", "Joy", "Umar", "Musa"]
for student in students :
    print(student)
    maths_score = int(input("Enter Maths Score: "))
    eng_score = int(input("Enter English Score: "))
    sst_score = int(input("Enter SST Score: "))
    sci_score = int(input("Enter Science Score: "))
    total_score = maths_score + eng_score + sst_score + sci_score
    average_score = total_score / 4
    print(f"Average = {average_score}\nTotal = {total_score}\n")