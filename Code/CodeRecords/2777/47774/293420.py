t=int(input())
for nn in range(t):
    n=int(input())
    b=list(eval(input().replace(' ',',')))
    b.sort()
    if n%2!=0:
        print(b[int(n/2)])
    else:
        a=int(n/2)
        res=int((b[a]+b[a-1])/2)
        print(res)