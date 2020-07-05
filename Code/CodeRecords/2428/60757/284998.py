t=int(input())
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    l1=[]
    l2=[]
    for i in range(len(li)):
        if li[i]%2==0:
            l2.append(li[i])
        else:
            l1.append(li[i])
    l1=sorted(l1)[::-1]
    l2=sorted(l2)
    for i in range(len(l2)):
        l1.append(l2[i])
    for i in range(len(l1)):
        print(l1[i],end=' ')
    print()