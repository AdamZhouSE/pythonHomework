n=int(input())
for i in range(n):
    number=int(input())
    res=[1]
    j=1
    times=1
    while j<number:
        k=0
        next=res[-1]+1
        while k<=times and j<number:
            res.append(next)
            next=next+2
            k=k+1
            j=j+1
        times=times+1
    for i in res:
        if i!=1:
            print(" ",end="")
        print(i,end="")
    print()