firstLine=input()
n=int(firstLine)
scoreList=[]
for i in range(n):
    score=input().split()
    scoreList.append(int(score[0])+int(score[1])+int(score[2])+int(score[3]))
smith=scoreList[0]
scoreList.sort(reverse=True)
for i in range(n):
    if scoreList[i]==smith:
        print(i+1)
        break