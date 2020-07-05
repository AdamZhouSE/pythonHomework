res=[]

def printAns(currList, currSum, target, k):
    if currSum==target and len(currList)==k:
        res.append(currList)
        return
    elif currSum>target or len(currList)>k:
        return
    else:
        if len(currList)==0:
            start=1
        else:
            start=currList[len(currList)-1]+1
        for i in range(start, 9):
            t=currList[:]
            t.append(i)
            printAns(t, currSum+i, target, k)



s=input()
k=int(s[0])
target=int(s[3:])
printAns([], 0, target, k)
print(res)