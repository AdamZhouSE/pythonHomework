def func40():
    arr = list(map(int, input().split()))
    n, q = arr[0], arr[1]
    arr = sorted(list(map(int, input().split())))
    nums = [0 for i in range(0, n)]
    for _ in range(0, q):
        t = list(map(int, input().split()))
        for i in range(t[0] - 1, t[1]):
            nums[i] += 1
    nums = sorted(nums)
    ans = 0
    for i in range(0, n):
        ans += nums[i] * arr[i]
    print(ans)


func40()
