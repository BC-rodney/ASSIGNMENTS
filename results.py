# A program to capture student name, coursework mark and exam score out of 100
#coursework mark is out of 40 and exam mark ot of 100
#compute final coursework mark out of 30 and exam mark out of 70
#determine the student grade basing on the final score as follows
'''final mark  80+  70-79  60-69  50-59  Below 50
   Grade       A     B      C      D       F     '''

student_name = input("ENTER STUDENT NAME: ")
course_work = int(input("ENTER COURSEWORK MARK: "))
exam_score = int(input("ENTER EXAM SCORE: "))

final_coursework = int(course_work / 40 * 30)
final_exam = int(exam_score / 100 * 70)

final_score = final_coursework + final_exam
print(f"FINAL COURSEWORK MARK = {final_coursework}\nFINAL EXAM MARK = {final_exam}\nFINAL SCORE = {final_score}")
if final_score >= 80 :
    print("Grade: A")
elif final_score >= 70 :
    print("Grade: B")
elif final_score >= 60 :
    print("Grade: C")
elif final_score >= 50 :
    print("Grade: D")
else :
    print("Grade: F")

