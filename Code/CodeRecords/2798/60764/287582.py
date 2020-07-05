a=int(input())
nums=list(map(int,input().split()))
s=int(sum(nums)/3)
if sum(nums)%3!=0 or a<3:
    print(0)
else:
    res=0
    for i in range(1,a-1):
        sum1=sum(nums[0:i])
        if sum1!=s:
            continue
        for j in range(i+1,a):
            sum2=sum(nums[i:j])
            sum3=sum(nums[j:a])
            if sum2!=s or sum3!=s:
                continue
            res=res+1
    print(res)