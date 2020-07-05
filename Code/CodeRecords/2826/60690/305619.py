n=int(input())
medal=input().split(" ")
for i in range(n): medal[i]=int(medal[i])
medal.sort()
res=0
for i in range(n-1):
    if medal[i]==medal[i+1]:
        now=medal[i]
        while now in medal: now+=1
        res=res+(now-medal[i])
        medal[i]=now
print(res)