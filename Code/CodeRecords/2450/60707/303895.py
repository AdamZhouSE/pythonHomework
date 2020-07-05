def searchRange(nums, target):

    """

    :type nums: List[int]

    :type target: int

    :rtype: List[int]

    """

    if not nums:
        return [-1, -1]

    if nums[0] <= target <= nums[-1]:

        mid = 0

        l = 0

        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if target == nums[mid]:

                #print(mid)

                l = mid

                r = mid

                while l - 1 >= 0 and nums[l - 1] == nums[l]:
                    l -= 1

                    #print(l)

                while r + 1 <= len(nums) - 1 and nums[r] == nums[r + 1]:
                    r += 1

                return [l, r]

            if nums[mid] < target:

                l = mid + 1

            else:

                r = mid - 1

    return [-1, -1]




inp = input().split(",")
k = int(input())
for i in range(len(inp)):
    inp[i] = int(inp[i])

print(searchRange(inp, k))