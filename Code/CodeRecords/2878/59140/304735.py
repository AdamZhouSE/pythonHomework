s=input()
n,k=int(s.split(" ")[0]),int(s.split(" ")[1])
ai=[int(x) for x in input().split(" ")]
minTime=k
for i in ai:
    if k%i==0:minTime=min(minTime,k//i)
print(minTime)