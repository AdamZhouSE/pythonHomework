size=int(input())
for i in range(size):
    n=int(input())
    list0=input().split()
    list0=[int(list0[m]) for m in range(n) ]
    
    for j in range(len(list0)-1):
        isF=False
        for m in range(j+1,len(list0)):
            if list0[j]<list0[m]:
                isF=True
                break
        if not isF:
            print(list0[j],end=' ')
    print(list0[len(list0)-1])
            