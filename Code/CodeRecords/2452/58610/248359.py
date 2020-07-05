a = [eval(input()) for i in range(eval(input()))]
target = eval(input())
for nums in a:
    if nums[-1] < target or nums[0] > target:
        continue
    elif nums[0] < target < nums[-1]:
        for num in nums:
            if num == target:
                print(True)
                exit()
        print(False)
        break