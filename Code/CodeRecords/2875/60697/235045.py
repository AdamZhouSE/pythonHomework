num=int(input())
s=""
sizes=list(map(int,input().split(' ')))
res=[0 for i in range(num+1)]
for i in range(num):
    res[sizes[i]]=i+1
for i in range(1,num+1):
    s=s+str(res[i])
    if(i!=num):
        s=s+" "
print(s)