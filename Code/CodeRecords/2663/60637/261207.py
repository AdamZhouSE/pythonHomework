tests=(int)(input())
for i in range(0,tests):
    n=(int)(input())
    k=7
    sum=3
    for j in range(0,n-1):
        sum+=k
        k+=4
    print(sum)