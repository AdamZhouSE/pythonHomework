t=int(input())
for ti in range(t):
    n=int(input())
    s=input().split(' ')
    li=[]
    for i in s:
        li.append(int(i))
    li=sorted(li)
    for j in range(n-1):
        if j%2!=0:
            continue
        s=li[j]
        li[j]=li[j+1]
        li[j+1]=s
    #print(li)
    for k in range(n-1):
        print(li[k],end=' ')
    print(li[-1],end='')
    print()