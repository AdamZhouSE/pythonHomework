cases=int(input())
for i in range(cases):
    n=int(input())
    nums=list(map(int,input().split()))
    k=int(input())
    pro=1
    for x in nums:
        pro*=x
    print(pro%k)