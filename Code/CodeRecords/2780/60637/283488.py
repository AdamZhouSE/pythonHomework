tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    arr=list(map(int,input().split(' ')))
    k=(int)(input())
    sum=1
    for i in arr:
        sum*=i
    print(sum%k)
