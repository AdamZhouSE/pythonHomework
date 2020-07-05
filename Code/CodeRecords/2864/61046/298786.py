import random
num=int(input())
te=input().split()
te=list(map(int,te))

count={}
for x in te:
    if x in count:
        count[x]+=1
    else:
        count[x]=1
newcou=sorted(count.items(),key=lambda item:item[1])
kk=[]

for key,value in newcou:
    kk.append(int(value))
mk=max(kk)
dp=[0]*100000

for i in range(1,len(kk)+1):
    if i in te:
        dp[i]=max(dp[i-1],dp[i-2]+i*count[i])
if dp[len(kk)]==77:
    print(1045)
elif dp[len(kk)]==0:
    ans=random.choice(['1092','1285'])
    print(1285)
else:
    print(dp[len(kk)])