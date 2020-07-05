import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
sli=s.split("\n")
n=nums[0]
del(nums[0])
player=[]
score=[]
del(sli[0])
winner=""
bestscore=0
for i in range(n):
    info=sli[i].split(" ")
    pl=info[0]
    point=nums[i]
    if pl not in player:
        player.append(pl)
        score.append(point)
    else:
        indx=player.index(pl)
        score[indx]+=point
    for j in range(len(score)):
        if score[j]>bestscore:
            bestscore=score[j]
            winner=player[j]
print(winner)