n=int(input())
for i in range(n):
    number=int(input())
    nums=list(map(int,input().split(" ")))
    K=int(input())
    res=1
    
    for i in nums:
        res=res*i
    print(res%K)