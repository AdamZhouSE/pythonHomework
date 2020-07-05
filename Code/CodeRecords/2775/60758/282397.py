k=int(input())
for i in range(0,k):
    x=int(input())
    if x%3==0:
        a=x/3-1
        b=x/3
        c=x/3+1
        print(a,b,c)
    else:
        print(-1)