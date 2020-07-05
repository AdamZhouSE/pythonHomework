sum=int(input())
nums=list(map(int,input().split(',')))
add=0
index=0
start=0
if sorted(nums)[len(nums)-1]>=sum:print(1)
else:
    while add<sum:
        if index==len(nums):
            print(0)
            break
        add+=nums[index]
        index+=1
    if index!=len(nums):
            while index<len(nums) and add-nums[start]+nums[index]>sum:
                add=add-nums[start]-nums[start+1]+nums[index]
                index+=1
                start+=2
    print(index-start)