t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split(' ')))
    a.sort()
    x=0
    y=0
    a.insert(0,0)
    n+=1
    if n==2:
        if a[0]==a[1]:
            if a[0]==1:
                x=2
                y=1
            else:
                x=1
                y=2
        print(str(y) + ' ' + str(x))
        continue
    for j in range(n-1):
        if a[j+1]-a[j]==2:
            x=a[j]+1
            break
    for j in range(n - 1):
        if a[j]==a[j+1]:
            y=a[j]
            break
    print(str(y)+' '+str(x))