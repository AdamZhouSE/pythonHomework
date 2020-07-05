a=str(input())
b=str(input())

from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        t = Counter(t)
        res = None

        l, r = 0, 0

        tmp = {}
        while l < len(s):
            tmp[s[r]] = tmp.get(s[r], 0) + 1
            r += 1

            if all([k in tmp for k in t]) and all([tmp[k] >= t[k] for k in t]):
                if res == None:
                    res = s[l:r]
                else:
                    res = min(res, s[l:r], key=len)

                tmp[s[l]] -= 1
                l += 1
                r -= 1
                tmp[s[r]] -= 1

            if r == len(s): break

        return res if res else ""
c=Solution()
print(c.minWindow(a,b))