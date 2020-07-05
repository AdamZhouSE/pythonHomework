arr = input()[1:-1]
nums = [int(i) for i in arr.split(',')]


def find(start, end):
    mid = int((start + end)/2)
    if mid>=start+1 and nums[mid-1]==nums[mid]:
        if (end-mid)%2 == 0:
            find(start, mid-2)
        else:
            find(mid+1,end)
    elif mid+1<=end and nums[mid] == nums[mid + 1]:
        if (mid - start)%2 == 0:
            find(mid+2,end)
        else:
            find(start, mid-1)
    else:
        print(nums[mid])
        exit()


find(0, len(nums)-1)