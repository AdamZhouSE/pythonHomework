n=int(input())
race={}
score={}
for x in range(0,n):
    y=input().split(" ")
    y[1]=int(y[1])
    if y[0] in race:
        race[y[0]]=race[y[0]]+y[1]
    else:
        race[y[0]]=y[1]
    if race[y[0]] not in score:
        score[race[y[0]]]=y[0]
value=max(race.values())
for key in score.keys():
    if key>=value:
        print(score[key])
        break