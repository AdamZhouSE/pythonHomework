nums = []
target = 0


def find(start, end):
    if start == end:
        return start
    mid = int((start+end)/2)
    if nums[start] < nums[end]:
        if target < nums[start] or target > nums[end]:
            return -1
        if target <= nums[mid]:
            return find(start, mid)
        else:
            return find(mid+1, end)
    else:
        if nums[mid] > nums[start]:
            if nums[start] <= target <= nums[mid]:
                return find(start, mid)
            else:
                return find(mid+1, end)
        else:
            if target > nums[end]:
                return find(start, mid-1)
            else:
                return find(mid, end)
        

if __name__ == '__main__':
    nums = [int(i) for i in input().split()]
    target = int(input())
    print(find(0, len(nums)-1))