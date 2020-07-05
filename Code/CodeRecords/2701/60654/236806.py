def game(play):
    if ("0,0" in play) & ("1,0" in play) & ("2,0" in play):
        return True
    if ("0,1" in play) & ("1,1" in play) & ("2,1" in play):
        return True
    if ("0,2" in play) & ("1,2" in play) & ("2,2" in play):
        return True
    if ("0,0" in play) & ("0,1" in play) & ("0,2" in play):
        return True
    if ("1,0" in play) & ("1,1" in play) & ("1,2" in play):
        return True
    if ("2,0" in play) & ("2,1" in play) & ("2,2" in play):
        return True
    if ("0,0" in play) & ("1,1" in play) & ("2,2" in play):
        return True
    if ("0,2" in play) & ("1,1" in play) & ("2,0" in play):
        return True
    return False
way = input().strip("[[").strip("]]").split("],[")
play1 = []
play2 = []
for i in range(way.__len__()):
    if i%2==0:
        play1.append(way[i])
    else:
        play2.append(way[i])
if game(play1):
    print("A")
elif game(play2):
    print("B")
elif way.__len__() < 9:
    print("Pending")
else:
    print("Draw")
