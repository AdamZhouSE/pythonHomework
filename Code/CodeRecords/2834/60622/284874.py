l=list(map(int,input().split()))
table=[]
for i in range(l[0]):
    p=list(input())
    table.append(p)
marks=list(map(int,input().split()))
sum=0
for i in range(l[1]):
    tem=[]
    for j in range(l[0]):
        tem.append(table[j][i])
    s=list(set(tem))
    times=[]
    for t in range(len(s)):
        times.append(tem.count(s[t]))
    times.sort()
    sum+=marks[i]*times[-1]
print(sum)