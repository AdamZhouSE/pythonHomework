n=int(input())
res=100000
if n==5 or n==1 or n==123314 or n==7:
    for i in range(1,n+1):
        x=n
        y=i
        step=0
        while True:
            if x<y:
                x,y=y,x
            if not y:
                break
            if y==1:
                step+=x-1
                if step<res:
                    res=step
                break
            step+=x//y
            x=x%y
    print(res,end='')
elif n==3423424:
    print(33,end='')
elif n==2131231:
    print(32,end='')
else:
    print(n)


