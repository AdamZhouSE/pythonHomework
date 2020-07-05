import bisect
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        l, r, ans = 0, max(arr), -1
        while l <= r:
            mid = (l + r) // 2
            it = bisect.bisect_left(arr, mid)
            cur = prefix[it] + (n - it) * mid
            if cur <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        def check(x):
            return sum(x if num >= x else num for num in arr)

        choose_small = check(ans)
        choose_big = check(ans + 1)
        return ans if abs(choose_small - target) <= abs(choose_big - target) else ans + 1


if __name__ == "__main__":
    arr = list(map(int, input().split(",")))
    target = int(input())
    solution = Solution()
    result = solution.findBestValue(arr, target)
    print(result)
