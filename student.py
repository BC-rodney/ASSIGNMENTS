scores = []
def add_score(score):
    if score > 0:
        scores.append(score)
    else:
        print("Score should be above zero (0)")

    return None


def sum_scores(total,score):
    for score in scores:
      total += score

    return total

#def add_scores(scores)


def list_scores(scores):
    for score in scores:
        print(score)

    return None

'''def highestscore(scores):
    scores.sort()
    scores.reverse()
    highest_score = scores[0]

    return highest_score'''

def highestscore(scores):
    highest_score = 0
    for score in scores:
        if score > highest_score:
            highest_score = score

    return highest_score

while True:
    score = input("Enter Score or Q to Quit: ")
    if score.upper()== "Q":
        break

    add_score(int(score))

list_scores(scores)
total = 0 
print(scores)
print(f"Total: {sum_scores(total,score)}")
print(f"Highest Score: {highestscore(scores)}")
