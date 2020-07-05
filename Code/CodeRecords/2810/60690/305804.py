num=input()
res=[]
numBs=[]
for i in range(len(num)):
    numBs.append(int(num[i]))

def isZero(numBs):
    for i in range(len(numBs)):
        if numBs[i]!=0:
            return False
    return True

while isZero(numBs)!=True:
    thisBin=0
    for i in range(len(numBs)):
        if numBs[i]>0:
            thisBin=thisBin*10+1
            numBs[i] -= 1
        else:
            thisBin=thisBin*10
    res.append(thisBin)
print(len(res))
for i in range(len(res)-1):
    print(res[i],end=" ")
print(res[-1])
