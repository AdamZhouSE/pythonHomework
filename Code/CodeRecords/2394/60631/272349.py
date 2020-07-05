t=int(input())
for ti in range(t):
    n=int(input())
    l=input().split(' ')
    li=[]
    for j in l:
        li.append(int(j))
    out=[]
    for k in li:
        if k!=0:
            out.append(k)
    for k in range(n-len(out)):
        out.append(0)
    li=out
    #print(li)
    for k in range(n-1):
        print(li[k],end=' ')
    print(li[-1],end=' ')
    print()