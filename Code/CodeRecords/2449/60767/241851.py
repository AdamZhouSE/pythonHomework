def search(nums,target):
    left = 0
    right = len(nums)-1
    while(left<=right):
        mid = int((right + left) / 2)
        if(nums[mid] == target):
            return mid
        if(nums[mid]<target):
            if(nums[mid]<nums[left]):#mid<left说明左端为旋转区间,右端为递增区间
                if(nums[right]<target):#说明target在左端区间
                    right = mid - 1
                else:#target在右端区间
                    left = mid + 1
            else:#左端为递增区间，右端为旋转区间,由于前提是target>nums[mid],故此时target只能在右端
                left = mid + 1
        else:
            if(nums[mid]<nums[left]):#mid<left说明左端为旋转区间,右端为递增区间
                right = mid - 1
            else:
                if(nums[left]<=target):
                    right = mid - 1
                else:
                    left = mid + 1
    return -1

inp = input().split(",")
nums = []
for i in inp:
    nums.append(int(i))
target = int(input())
res = search(nums,target)
print(res)