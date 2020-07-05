def func32():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    res = []
    for i in range(1,len(nums)):
        if nums[i] == 1:
            res.append(nums[i-1])
    if nums[len(nums)-1] == 1 or nums[len(nums)-2] >= 1:
        res.append(nums[len(nums)-1])
    print(len(res))
    for i in range(0,len(res)-1):
        print(res[i],end=" ")
    print(res[len(res)-1])
    return

func32()