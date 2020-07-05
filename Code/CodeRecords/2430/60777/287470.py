case=int(input())
for i in range(case):
    n=int(input())
    temp=[int(x) for x in input().split(' ')]
    k=int(input())
    find=False
    for m in range(n):
        for n in range(m+1,n):
            if(temp[m]+temp[n]==k):
                find=True
                print(temp[m],temp[n],k)
    if(not find):
        print(-1)