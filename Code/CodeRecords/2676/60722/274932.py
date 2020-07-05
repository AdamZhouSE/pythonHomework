T=int(input())
for m in range(T):
    string=input().split(" ")
    N,K=int(string[0]),int(string[1])
    nums=input().split(" ")
    for i in range(N):
        nums[i]=int(nums[i])
    result=0
    for i in range(N-K+1):
        result=max(result,sum(nums[i:i+K]))
    print(result)