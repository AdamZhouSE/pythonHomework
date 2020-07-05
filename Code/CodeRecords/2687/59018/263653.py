import math

def change(n):
    S=[]
    ANSWER=[]
    a=n-1
    x=math.floor(math.log(a,2))
    y=math.floor(x+2/2)
    for i in range(1,y+1):
        s=int((math.pow(4,i)-1)/3)
        if s<=n:
            S.append(s)
        else:
            break
    for j in range(len(S)):
        ANSWER.append(S[j])
        if 2*S[j]<=n:
            ANSWER.append(2*S[j])
    info=[str(y) for y in ANSWER]
    info1=' '.join(info)
    return info1

T=int(input())
for i in range(T):
    n=int(input())
    print(change(n))
          

         







