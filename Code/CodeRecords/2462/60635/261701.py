nums=eval(input())
def search(start):
    if start==0:
        if nums[start]>nums[start+1]:
            return start
    if start==len(nums)-1:
        return start
    if nums[start-1]<nums[start] and nums[start]>nums[start+1]:
        return start
    return search(start+1)
print(search(0))