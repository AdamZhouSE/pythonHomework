import math

t = int(input())
for j in range(t):
    l = list(map(int,input().split()))
    k = int(input())
    ans=[]
    start=int(math.pow(2,k))
    if start>=len(l):
        print("EMPTY")
    else:
        for i in range(start,len(l)):
            ans.append(str(l[i]))
        print(' '.join(ans))