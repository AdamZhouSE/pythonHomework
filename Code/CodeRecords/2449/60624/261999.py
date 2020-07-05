def func2():
    temp = input()
    nums = list(map(int, temp.split(",")))
    target = int(input())
    #nums = list(range(100))
    #target = 8
    #print(nums, target)
    #random_N = round(random.random()*len(nums))
    #print(random_N)
    #nums = nums[random_N:]+nums[0:random_N]
    print(search(nums, 0, len(nums)-1, target))
    return


def search(nums:list, low:int, high:int, target:int)->int:
    if low>high:
        return -1
    mid = (low+high)//2
    if nums[mid]==target:
        return mid
    if nums[mid]<nums[high]:
        if nums[mid]<target<=nums[high]:
            return search(nums,mid+1,high,target)
        else:
            return search(nums,low,mid-1,target)
    else:
        if nums[low]<=target<nums[mid]:
            return search(nums,low,mid-1,target)
        else:
            return search(nums,mid+1,high,target)
func2()