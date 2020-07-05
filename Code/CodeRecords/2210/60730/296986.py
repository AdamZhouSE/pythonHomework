from collections import Counter
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        ans = s + s
        n = len(s)
        target = Counter(t)
        counter = defaultdict(lambda: 0)

        def contains(counter, target):
            if len(counter) < len(target):
                return False
            for k in counter:
                if k not in target or counter[k] < target[k]:
                    return False
            return True

        for r in range(n):
            if s[r] in target:
                counter[s[r]] += 1
            while l < n and contains(counter, target):
                if r - l + 1 < len(ans):
                    ans = s[l:r + 1]
                if s[l] in target:
                    counter[s[l]] -= 1
                l += 1
        return "" if ans == s + s else ans


if __name__ == "__main__":
    num = int(input())
    solution = Solution()
    for i in range(num):
        m = input()
        n = input()
        result = solution.minWindow(m, n)
        if result == "":
            print(-1)
        else:
            print(solution.minWindow(m, n))
