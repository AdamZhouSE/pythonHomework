nums = input().split(',')
num = [int(nums[i]) for i in range(len(nums))]
n = int(input())
l, r = 0, len(nums) - 1
res = False

while l <= r:
    mid = (l + r) // 2
    if num[mid] == n:
        res = True
    if num[mid] > num[l]:
        if num[l] <= n < num[mid]:
            r = mid - 1
        else:
            l = mid + 1

    elif num[mid] < num[l]:
        if num[mid] < n <= num[r]:
            l = mid + 1
        else:
            r = mid - 1

    else:
        l += 1

if res:
    print("True")
else:
    print("False")
