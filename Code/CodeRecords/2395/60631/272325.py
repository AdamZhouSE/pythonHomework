t=int(input())
for ti in range(t):
    n=int(input())
    l=input().split(' ')
    li=[]
    for j in l:
        li.append(int(j))
    for i in range(n-1):
        if li[i]==li[i+1]:
            li[i]=2*li[i]
            li[i+1]=0
    out=[]
    for k in li:
        if k!=0:
            out.append(k)
    for k in range(n-len(out)):
        out.append(0)
    li=out
    
    
    for k in range(n-1):
        print(li[k],end=' ')
    print(li[-1],end='')
    print()