def func43():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        nums = list(map(int, input().split(" ")))
        nums.sort()
        flag = False
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                flag = True
                print(i+1)
                break
        if not flag:
            print(-1)
    return
func43()