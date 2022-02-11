# one side is player number other side is their score get them sorted
# by their score

team = [
    ("dplayer1", 23),
    ("aplayer2", 45),
    ("cplayer3", 65),
    ("eplayer4", 11),
    ("bplayer5", 9),
]


"""
this funtion will check the number in the element 
"""


def take_player_number(number):
    return number[1]
# number [1] means index of tupple means position of element in tupple


"""
this will give parameter that will check the number only in function
'take_player_number' in side the list 'team'
"""
team.sort(key=take_player_number)
print(team)
