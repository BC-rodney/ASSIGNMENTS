# Define the number of students and tests
num_students = 5
num_tests = 3

# Initialize empty lists to store names and test scores
student_names = []
scores = []

# Loop through each student to get their data
for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    student_names.append(name)
    
    student_scores = []
    total_score = 0
    
    # Get scores for each test and calculate the total score
    for j in range(num_tests):
        score = float(input(f"Enter score for Test {j+1} for {name}: "))
        student_scores.append(score)
        total_score += score
        
    # Calculate the average score
    average_score = total_score / num_tests
    
    # Append the scores and computed values to the scores list
    scores.append((student_scores, total_score, average_score))

# Output the summary in a tabular format
print("\nSummary of Student Scores:")
print(f"{'Name':<20}{'Test 1':<10}{'Test 2':<10}{'Test 3':<10}{'Total':<10}{'Average':<10}")

# Print the data for each student
for i in range(num_students):
    name = student_names[i]
    student_scores, total_score, average_score = scores[i]
    print(f"{name:<20}{student_scores[0]:<10}{student_scores[1]:<10}{student_scores[2]:<10}{total_score:<10}{average_score:<10.2f}")
