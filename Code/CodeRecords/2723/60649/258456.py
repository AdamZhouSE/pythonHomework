T=int(input())
for i in range(T):
    n=int(input())
    tmp=str(n)
    sum=n
    while sum>=10:
        sum=0
        for i in tmp:
            sum+=int(i)
        tmp=str(sum)
    print(sum)