n=int(input())
need=[]
money=[]
res=0
for i in range(n):
    m=list(map(int,input().split()))
    need.append(m[0])
    money.append(m[1])
count=0
while count<n:
    counter=count+1
    res+=need[count]*money[count]
    while counter<n and money[count]<=money[counter]:
        res+=need[counter]*money[count]
        counter+=1
    count=counter
print(res)