team = [
    ("aplayer1", 23),
    ("cplayer2", 45),
    ("bplayer3", 65),
    ("dplayer4", 11),
    ("eplayer5", 9),
]
"""
here lambda funtion is key which is inbuit takes as many parameters
here it is taking number as parameter in the list 'team'
"""
(team.sort(key=lambda number: number[1]))
print(team)
"""
example 2 for number[0]
"""

(team.sort(key=lambda number: number[0]))
print(team)
