nums=input()
nums=sorted(nums)
num=nums[0]
l=int(len(nums)/2)
k=1
for i in range(1,len(nums)):
    if num==int(nums[i]):
        k=k+1
    else:
        if k>l:
            print(nums[i-1])
            k=0
            break
        else:
            k=1
            num=int(nums[i])
if k>l:
    print(nums[-1])