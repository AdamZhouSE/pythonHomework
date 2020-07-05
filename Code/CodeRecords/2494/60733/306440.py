def reversePairs(nums) -> int:
    ans = 0

    def merge_sort(enum):
        nonlocal ans
        half = len(enum) // 2
        if half:
            left, right = merge_sort(enum[:half]), merge_sort(enum[half:])
            max_right = None
            l, r = len(left) - 1, len(right) - 1
            while l >= 0 and r >= 0:  # O(N)
                if left[l][1] > right[r][1] * 2:
                    ans += r + 1
                    l -= 1
                else:
                    r -= 1
            for i in reversed(range(len(enum))):
                if not right or (left and left[-1][1] > right[-1][1]):
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum

    res = [0] * len(nums)
    merge_sort(list(enumerate(nums)))
    return ans


arr = list(map(int, input().replace("[", "").replace("]", '').split(",")))
res=reversePairs(arr)
print(res)
