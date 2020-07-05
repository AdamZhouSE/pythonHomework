
n=input()[1:-1]
nums=n.split(',')
nums=[int(x) for x in nums]
answer=0
for i in range(nums.__len__()-1):
    for j in range(i+1,nums.__len__()):
        if nums[i]>2*nums[j]:
            answer+=1
print(answer)