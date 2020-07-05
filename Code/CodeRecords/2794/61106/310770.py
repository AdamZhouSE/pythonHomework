floor=int(input())
eachnum=list(map(int,input().split()))
need=int(input())
neednum=list(map(int,input().split()))
result=[]
for i in range(need):
    for n in range(floor):
        if neednum[i]<=eachnum[n]:
            result.append(n+1)
            break
        else:
            neednum[i] -= eachnum[n]
for i in range(len(result)):
    print(result[i])