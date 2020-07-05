import math
x=int(input())
y=int(input())
bound=int(input())
N=math.ceil(math.log(bound,min(x,y)))
ans=set()
temp=0
for i in range(N):
    for j in range(N):
        temp = int(math.pow(x, i) + math.pow(y, j))
        if temp<=bound:
            ans.add(temp)
        else:
            break
print(sorted(list(ans)))