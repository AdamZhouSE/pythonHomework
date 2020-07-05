size=int(input())
for k in range(size):
    l=int(input())
    list0=input().split()
    list0=[int(list0[i]) for i in range(l)]
    for i in range(l-1):
        isF=False
        for j in range(i+1,l):
            if list0[j]>=list0[i]:
                isF=True
                print(list0[j],end=' ')
                break
        if not isF:
            print(-1,end=' ')
    print(-1)