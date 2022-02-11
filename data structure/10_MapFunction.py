team = [
    ("aplayer1", 23),
    ("cplayer2", 45),
    ("bplayer3", 65),
    ("dplayer4", 11),
    ("eplayer5", 9),
]

# number = []
# for teams in team:
#     number.append(teams[1])

# print(number)

player_number = list(map(lambda teams: teams[1], team))

print(player_number)
