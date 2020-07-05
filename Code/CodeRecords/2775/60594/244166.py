n=(int)(input())
for index in range(0,n):
    x=(int)(input())
    if (x/3)-(int)(x/3)>0:
        print(-1)
    else:
        k=(int)(x/3)
        print(k-1,end=' ')
        print(k,end=' ')
        print(k+1)