n=int(input())
numList=input().split()
odds=[]
evens=[]
for c in numList:
    if int(c)%2==0:
        evens.append(int(c))
    else:
        odds.append(int(c))

res=0
for even in evens:
    res+=even

odds.sort()
for odd in odds:
    res += odd
if len(odds)%2!=0:
    res-=odds[0]
print(res)