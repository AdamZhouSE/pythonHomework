nums=eval(input())
start=0
end=len(nums)-1
for i in range(0,len(nums)-1):
    if(nums[i]>nums[i+1]):
        start=i
        break
for i in range(len(nums)-1,0,-1):
    if (nums[i] < nums[i - 1]):
        end = i
        break
print(end-start+1)