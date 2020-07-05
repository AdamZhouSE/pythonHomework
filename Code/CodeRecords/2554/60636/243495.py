from itertools import combinations
num=int(input())
source=[]
for i in range(num):
    source.append(input().split(" "))
lists=list(combinations(source,num-1))
times=[]
for i in lists:
    all=[]
    for a in range(1000+1):
        all.append(0)
    for x in i:
        for y in range(int(x[0]),int(x[1])):
            all[y]=1
    time=all.count(1)
    times.append(time)
print(max(times),end="")