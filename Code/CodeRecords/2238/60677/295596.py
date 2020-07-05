nums=input().split(",")
nums=[int(x) for x in nums]
nums=list(set(nums))
answer=nums.__len__()
for i in nums:
    answer+=i
print(answer)