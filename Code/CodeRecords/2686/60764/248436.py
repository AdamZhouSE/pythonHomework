def evalProfit(nums,begin,k,profit):
    if k==0 or begin==len(nums)-1:
        return profit
    p=0
    for i in range(begin,len(nums)):
        if nums[i]>nums[begin]:
            tem=nums[i]-nums[begin]+evalProfit(nums,i+1,k-1,0)
            if tem>p:
                p=tem
    return p+profit

T=int(input())
for t in range(T):
    k=int(input())
    n=int(input())
    nums=list(map(int,input().split()))
    profit=0
    for i in range(n-1):
        tem=evalProfit(nums,i,k,0)
        if tem>profit:
            profit=tem
    print(profit)