def do():
    n=int(input())
    list=input().split()
    list=[int(x) for x in list]
    answer=0
    left=list[0]
    right=list[n-1]
    limit=left
    if right<left:
        limit=right
    for i in range(1,n-1):
        if list[i]<limit:
            answer+=limit-list[i]
    print(answer)
times=int(input())
for i in range(times):
    do()