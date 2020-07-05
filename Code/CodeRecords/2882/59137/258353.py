def s4():
    n = int(input())
    nums = list(input().split())
    for i in range(n):
        nums[i] = int(nums[i])

    flag = True
    stage = 1
    for i in range(1, n):
        if stage == 1:
            if nums[i] < nums[i-1]:
                stage = 3
            elif nums[i] == nums[i-1]:
                stage = 2
        elif stage == 2:
            if nums[i] > nums[i-1]:
                flag = False
            elif nums[i] < nums[i-1]:
                stage = 3
        else:
            if nums[i] >= nums[i-1]:
                flag = False

        if not flag:
            print("NO")
            return

    print("YES")


s4()