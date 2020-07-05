nums = eval(input())
D = int(input())
bound = sum(nums) // D
while True:
    flag = False
    count = 1
    i = 0
    this_day = 0
    while i < len(nums):
        if nums[i] > bound:
            flag = True
            break
        this_day += nums[i]
        if this_day > bound:
            this_day = 0
            count += 1
            continue
        i += 1
    if flag:
        bound += 1
        continue
    if count <= D:
        print(bound)
        break
    bound += 1
