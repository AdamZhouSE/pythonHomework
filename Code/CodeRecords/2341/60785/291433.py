t=int(input())
for te in range(t):
    x,y=[int(i) for i in input().split()]
    xlist=[int(i) for i in input().split()]
    ylist=[int(i) for i in input().split()]
    tmp=xlist+ylist
    tmp.sort()
    strlist=[str(i) for i in tmp]
    print(' '.join(strlist),end=' ')
    print()