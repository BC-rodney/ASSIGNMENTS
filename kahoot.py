quiz = [
    {
        "question": "How many bits are in a byte?",
        "options":["A. 10","B. 8","C. 6","D. 4"],
        "answer": "B"
    },
    {
        "question":"A collection of items is referred to as: ",
        "options":["A. List","B. Dictionary","C. Variable","D. Turple"],
        "answer": "A"

    },
    {
        "question":"Which component is considered as the brain of a computer? ",
        "options":["A. RAM","B. CMOS","C. CPU","D. Motherboard"],
        "answer": "C"

    },
    {
        "question":"Which of the following is not a datatype? ",
        "options":["A. Numeric","B. String","C. Boolean","D. Logical"],
        "answer": "D"

    },
    {
        "question":"What is the importance of the 'f'string ? ",
        "options":["A. To improve readability and less code","B. To store values","C. To skip to the next line","D. To make operations on values"],
        "answer": "A"

    }
]
correct = 0
wrong = 0
score = 0
for question in quiz:
    print(question["question"])
    for option in question["options"]:
        print(option)

    answer = input("Select Option: ")


    
    if answer == question["answer"]:
        print("Correct")
        correct += 1
        score += 5
    else:
        wrong += 1
        print(f"Wrong\nCorrect Answer is {question["answer"]}")

print(f"\nScore : {score}")
print(f"Correct Answers: {correct} \nWrong Answers: {wrong}")
