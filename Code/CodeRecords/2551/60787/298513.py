n,m=map(int,input().split())
lamp=[False for i in range(0,n)]
for step in range(0,m):
    c,a,b=map(int,input().split())
    if c==0:
        for i in range(a-1,b):
            lamp[i]=not lamp[i]
    else:
        temp=0
        for i in range(a-1,b):
            if lamp[i]:
                temp+=1
        print(temp)