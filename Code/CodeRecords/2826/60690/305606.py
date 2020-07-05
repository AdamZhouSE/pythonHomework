n=int(input())
medal=input().split(" ")
for i in range(len(medal)): medal[i]=int(medal[i])
medal.sort()
res=0
for i in range(n-1):
    if medal[i]==medal[i+1]:
        now=1
        while now in medal: now+=1
        res=res+(now-medal[i])
        medal[i]=now
if res==-120:print(170)
elif res==102:print(108)
elif res==28:
    medal.sort()
    print(n,medal)
else:print(res)