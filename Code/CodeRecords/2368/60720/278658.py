size=int(input())
for k in range(size):
    n=int(input())
    list0=input().split()
    s=0
    e=n-1
    isW=True
    while(s<=e):
        if isW:
            print(list0[e],end=' ')
            isW=False
            e-=1
        else:
            print(list0[s],end=' ')
            isW=True
            s+=1
    print()
            