T=int(input())
for t in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    pairs=0
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]==nums[j]:
                pairs+=1
    print(pairs)