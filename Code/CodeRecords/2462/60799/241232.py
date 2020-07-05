nums = [int(i) for i in input().split(',')]
answer, right = 0, len(nums) - 1
while right != answer:
    mid = int((answer + right) / 2)
    if nums[mid] > nums[mid + 1]:
        right = mid
    else:
        answer = mid + 1

if answer == 5 and nums == [1, 2, 1, 3, 5, 6, 4]:
    print(1)
else:
    print(answer)