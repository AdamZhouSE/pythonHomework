firstLine=input()
n=int(firstLine)
nameList=[]
scoreList=[]
highestScore=0
champion=""
for i in range(n):
    x=input().split()
    name=x[0]
    score=int(x[1])
    if name in nameList:
        scoreList[nameList.index(name)]+=score
        if scoreList[nameList.index(name)]>highestScore:
            highestScore=scoreList[nameList.index(name)]
            champion=name
    else:
        nameList.append(name)
        scoreList.append(score)
        if score>highestScore:
            highestScore=score
            champion=name
print(champion)