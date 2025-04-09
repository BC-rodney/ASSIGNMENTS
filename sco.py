games = ["Networking","Coding","Repair","Quiz"]
groups = ["CYBER","SYNTAX","CODERS"]
group_scores = []
for group in groups :
    print(f"\n\t{group}")
    games_scores = []
    for game in games :
        game_score = int(input(f"\t\t{game} Score: "))
        games_scores.append(game_score)

    group_scores.append(games_scores)

    output = ""
    for group_score in group_scores:
        total = 0
        for score in group_score:
            total += score
        
    print(f"Total = {total}")

print(f"Groups \tnetworking\tcoding\trepair\tquiz")
index = 0
for groups in group_scores:
    output = f"\t{groups[index]}\t"


    