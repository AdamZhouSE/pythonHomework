round=int(input())
winner=""
highscore=0
scorecounter={}
for i in range(round):
    result=input().split()
    result[1]=int(result[1])
    if result[0] not in scorecounter:
        scorecounter[result[0]]=result[1]
    else:
        scorecounter[result[0]]+=result[1]
    if scorecounter[result[0]]>highscore:
        highscore=scorecounter[result[0]]
        winner=result[0]
print(winner)