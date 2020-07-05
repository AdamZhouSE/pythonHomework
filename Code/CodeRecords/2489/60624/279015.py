def func17():
    nums = list(map(int, input()[1:-1].split(",")))
    low = int(input())
    high = int(input())
    ans = 0
    length = 1
    while length <= len(nums):
        i = 0
        while i+length <= len(nums):
            if low <= sum(nums[i:i+length]) <= high:
                ans += 1
            i += 1
        length += 1

    print(ans)
    return
func17()