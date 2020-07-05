tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    k=(int)(n/3)
    if(3*k==n):
        print((str)(k-1)+' '+(str)(k)+' '+(str)(k+1))
    else:
        print(-1)