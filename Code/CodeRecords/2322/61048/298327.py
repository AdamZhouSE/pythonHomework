import math
def numop31():
    L=int(input())
    R=int(input())
    res=0
    for i in range(L,R+1):
        if isparlin(i) and isSquare(i):
            tmp=int(math.sqrt(i))
            if(isparlin(tmp)):
                res+=1
    print(res)
    return 0

def isparlin(num):
    S=str(num)
    res=True
    for i in range(len(S)):
        if S[i]!=S[len(S)-1-i]:
            res=False
    return res

def isSquare(num):
    tmp=int(math.sqrt(num))
    return tmp**2==num

numop31()