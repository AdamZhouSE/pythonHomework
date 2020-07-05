def func42():
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        nums = list(map(int, input().split(" ")))
        k = int(input())
        nums.sort()
        print(nums[k-1])
    return
func42()