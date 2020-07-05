size=int(input())
for k in range(size):
    n=int(input())
    list0=input().split()
    list0=[int(list0[i]) for i in range(n)]
    list0.sort()
    index=0
    isC=False
    for i in range(n):
        if list0[i]!=i+1:
            index=i+1
            isC=True
            break
    if isC:
        for i in range(n):
            if list0[i]>i+1:
                isC=False
                print(i+2,end=' ')
                break
        if isC:
            print(list0[index-1],end=' ')
        print(index)
    else:
        print('0 0')