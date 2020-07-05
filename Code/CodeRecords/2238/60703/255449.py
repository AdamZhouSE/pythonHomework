answers = [int(x) for x in input().split(",")]
answersSET = set(answers)
answerDict = {}
outOfList = 0
for i in answersSET:
    if i in answerDict:
        continue
    if(i==0):
        answerDict[0] = True

    else:
        answerDict[i] = True
        times = 0
        for j in answers:
            if i==j:
                times+=1
        t = times%(i+1)
        if(t!=0):
            outOfList+=(1+i-t)

print(outOfList+len(answers))