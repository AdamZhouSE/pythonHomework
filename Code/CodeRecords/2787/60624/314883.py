def func28():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    ans = 0
    while len(nums) > 0:
        Max = max(nums)
        ans += abs(Max-n)
        nums.remove(Max)
        n -= 1
    print(ans)
    return
func28()