temp=input().split(" ")
n=int(temp[0])
visit=[0 for i in range(n)]
m=int(temp[1])
money=list(map(int,input().split(" ")))
res=[]

for i in range(m):
    temp=input().split(" ")
    fromWho=int(temp[0])
    toWho=int(temp[1])

    judge=False
    for j in range(len(res)):
        if(fromWho in res[j]):
            res[j].append(toWho)
            judge=True
        elif(toWho in res[j]):
            if(res[j][0]==toWho):
                res[j].reverse()
                res[j].append(fromWho)
                res[j].reverse()
            else:
                res[j].append(fromWho)
            judge=True
    if(judge==False):
        res.append([fromWho,toWho])
for i in res:
   for j in range(len(i)):
       if j==0:
           continue
       visit[i[j]-1]=1
sum=0
for i in range(n):
    if(visit[i]==0):
        sum+=money[i]
print(sum)