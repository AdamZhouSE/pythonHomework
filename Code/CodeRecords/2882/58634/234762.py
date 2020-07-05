def check():
    hasUp = False  # 表明当前的阶段
    hasMiddle = False
    for i in range(0, n - 1):
        if nums[i] < nums[i + 1]:
            if hasMiddle or hasUp:#已经过了上升或者中间阶段
                return False
        if nums[i] == nums[i + 1]:
            hasUp = True
            if hasMiddle:
                return False
        if nums[i] > nums[i + 1]:
            hasMiddle = True
            hasUp = True
    return True


n = int(input())
nums = [int(i) for i in input().split(" ")]
if n == 1 or n == 2:
    print("YES")
else:
    if check():
        print("YES")
    else:
        print("NO")
