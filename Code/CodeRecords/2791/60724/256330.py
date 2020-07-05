number=int(input())
numlist=input().split()
res=[]
t=0
for i in numlist:
    if int(i)==1:
        t=t+1
for j in range(len(numlist)-1):
    if int(numlist[j+1])==1:
        res.append(int(numlist[j]))
print(t)
for i in res:
    print(i,end=' ')
print(int(numlist[len(numlist)-1]))