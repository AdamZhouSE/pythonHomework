arr1 = list(eval(input()))
arr2 = list(eval(input()))


def maxVal(arr1, arr2):
    n = len(arr1)
    ans = 0

    # four directions
    for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
        maxv = 0
        minv = 4000000
        # min and max manhaton distance
        for i in range(n):
            maxv = max(maxv, arr1[i] * dx + arr2[i] * dy + i)
            minv = min(minv, arr1[i] * dx + arr2[i] * dy + i)
        ans = max(ans, maxv - minv)
    return ans


print(maxVal(arr1, arr2))
