def cal(b,k,nums):
    if(k==1):
        return("even")
    res=0
    for i in range(k):
        res+=(nums[i]*int(pow(b,(k-i-1))))
    if(res%2==1):
        return("odd")
    else:return("even")

inp=input().split(" ")
b=int(inp[0])
k=int(inp[1])
nums = input().split(" ")
for i in range(k):
    nums[i]=int(nums[i])
print (cal(b,k,nums))