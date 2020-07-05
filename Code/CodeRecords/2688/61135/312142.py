T=int(input())
def f(numlist,n,sum):
    if(sum==0):
        return 1
    if(n==0 and sum!=0):
        return 0
    if(numlist[n-1]>sum):
        return f(numlist,n-1,sum)
    return f(numlist,n-1,sum)+f(numlist,n-1,sum-numlist[n-1])
for a in range(T):
    n=int(input())
    nums=input().split(" ")
    sum=int(input())
    nums=list(int(x) for x in nums)
    print(f(nums,n,sum))