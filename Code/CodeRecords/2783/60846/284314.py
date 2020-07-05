t=int(input())
scores={}
maxscore=0
winner=""
for i in range(t):
    line=[x for x in input().split()]
    name=line[0]
    score=int(line[1])
    if name not in scores:
        scores[name]=score
    else:
        scores[name]+=score
    if scores[name] > maxscore:
        maxscore = scores[name]
        winner = name
print(winner)