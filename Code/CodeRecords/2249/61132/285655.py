n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split(','))))
sum=0
for i in range(n):
    sum += max(l[i])
    sum+=max([l[j][i] for j in range(n)])
    for j in l[i]:
        if j>0:
            sum+=1
print(sum)