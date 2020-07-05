nums=list(map(int,input().split(",")))
sum=0
for item in nums:
    sum+=item
if sum%2==1:
    print(False)
else:
    target=sum//2
    nums.sort()
    if nums[len(nums)-1]>target:
        print(False)
    else:
        print(True)