lists = eval(input())


def binaryFind(start, end, nums):
    print("此时start和end为"+str(start)+" "+str(end))
    mid = round((start + end) / 2)

    if nums[start] == nums[end]:
        print(nums[start])
        return

    if nums[mid] != nums[mid + 1] and nums[mid]!= nums[mid-1]:
        print(nums[mid])
        return

    if nums[mid] != nums[mid+1]:
        if (end-mid)%2==0:
            binaryFind(start, mid, nums)
        else:
            binaryFind(mid+1, end, nums)
    if nums[mid] != nums[mid - 1]:
        if (mid-start)%2==0:
            binaryFind(mid, end, nums)
        else:
            binaryFind(start,mid-1,nums)


binaryFind(0, len(lists)-1, lists)
