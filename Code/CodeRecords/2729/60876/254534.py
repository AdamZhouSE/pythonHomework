nums=eval(input())
for i in range(0,len(nums),2):
    item=nums[i]
    nums[i]="#"
    if item not in nums:
        print(item)
        break