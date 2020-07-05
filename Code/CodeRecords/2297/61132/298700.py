import math

m=input()
l = list(map(int,input().split()))
k = int(input())
ans=[]
start=int(math.pow(2,k))
end=int(math.pow(2,k+1))
if start>=len(l):
    print("EMPTY")
else:
    for i in range(start,min(len(l),end)):
        ans.append(str(l[i]))
    print(' '.join(ans))