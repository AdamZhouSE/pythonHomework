# 滑动窗口

import collections


def characterReplacement(s: str, k: int) -> int:
    res, m, maxl = 0, collections.Counter(), 0
    for i in range(len(s)):
        m[s[i]] += 1
        maxl = max(maxl, m[s[i]])
        if res - maxl < k:
            res += 1
        else:
            m[s[i - res]] -= 1
    return res


s, k = input(), int(input())
print(characterReplacement(s, k))

