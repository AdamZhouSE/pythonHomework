def func2():
    res = list(map(int, input().split()))
    k = res[1]
    res = list(map(int, input().split()))
    left = 0
    right = len(res) - 1
    while left < len(res) and res[left] <= k:
        left += 1
    while right >= 0 and right >= left and res[right] <= k:
        right -= 1
    print(len(res) - (right - left + 1))


func2()