tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    soldiers = []
    for j in range(int(nums[i])):
        soldiers.append(j+1)
    lp = 1  # 左指针，指向下一个死者；若指向执剑人会在条件判断上麻烦一点
    rp = int(nums[i])  # 右指针，指向当前幸存者末尾
    while len(soldiers) > 1:
        if lp == rp:
            lp = 0
        if lp > rp:
            lp = 1
        soldiers.pop(lp)
        lp += 1
        rp -= 1
    print(soldiers.pop())
