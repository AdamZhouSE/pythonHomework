num=input().strip().split(' ')
n=int(num[0])
m=int(num[1])
vote=[]
winner=0
candidate=[0 for _ in range(n)]
for i in range(m):
    temp=input().strip().split(' ')
    temp=[int(j) for j in temp]
    vote.append(temp)
for i in range(m):
    maxn=0
    for j in range(n):
        if vote[i][j]>vote[i][maxn]:
            maxn=j
    candidate[maxn]+=1
for i in range(n):
    if candidate[i]>candidate[winner]:
        winner=i
print(winner+1)