from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        for i in range(len(words)):
            mask = 0
            for alp in words[i]:
                mask |= 1 << (ord(alp) - 97)
            lookup[mask] = max(lookup[mask], len(words[i]))
        #print(lookup)
        return max([lookup[x] * lookup[y] for x in lookup for y in lookup if not x & y] or [0])
    
a=eval(input())
#print(a)

s=Solution()
print(s.maxProduct(a))
