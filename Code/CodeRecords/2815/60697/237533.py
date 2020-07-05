size=int(input())
nums=list(map(int,input().split(' ')))
nums.sort()
neint=[]
point=[]
for i in nums:
    if i<=0:
        neint.append(i)
    else:
        point.append(i)
posum=0
nesum=0
for i in point:
    posum=posum+i-1

if(neint.__contains__(0)) or (len(neint)%2==0):
    for i in neint:
        nesum=nesum+abs(-1-i)
else:
    l=len(neint)
    for i in range(l-1):
        nesum=nesum+abs(-1-neint[i])
    nesum=nesum+1-neint[l-1]
print(posum+nesum)