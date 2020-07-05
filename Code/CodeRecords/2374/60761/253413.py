def countnum(numlist,n):
    numset=list(set(numlist))
    numset.sort()
    countlist=[[] for i in range(n)]
    for num in numset:
        countlist[numlist.count(num)-1].append(num)
    countlist.reverse()
    result=[]
    for i in range(n):
        for j in countlist[i]:
            for k in range(n-i):
                result.append(j)
    return result
t=int(input())
for i in range(t):
    n=int(input())
    numlist=list(map(int,input().split(" ")))
    result=countnum(numlist,n)
    for i in range(n):
        print(result[i],end=" ")
    print()
         