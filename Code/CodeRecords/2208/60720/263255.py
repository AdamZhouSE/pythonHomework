size=int(input())
for k in range(size):
    l=int(input())
    list0=input().split()
    list0=[int(list0[i]) for i in range(l)]
    base=list0[0]
    print(-1,end=' ')
    for i in range(1,l):
        isF=False
        for j in range(i):
            if list0[i-j-1]<list0[i]:
                isF=True
                print(list0[i-j-1],end=' ')
                break
        if not isF:
            print(-1,end=' ')
    print()