res=[]

def printAns(currList, currSum, target, k):
    if currSum==target and len(currList)==k:
        res.append(currList)
        return
    elif currSum>target or len(currList)>k:
        return
    else:
        for i in range(currList[len(currList)-1], 9):
            t=currList[:]
            t.append(i)
            printAns(t, currSum+i, target, k)



s=input()
k=int(s[0])
target=int(s[3:])
printAns([], 0, target, k)
print(res)