k=int(input())
for i in range(0,k):
    x=int(input())
    if x%3==0:
        a=int(x/3-1)
        b=int(x/3)
        c=int(x/3+1)
        print(a,b,c)
    else:
        print(-1)