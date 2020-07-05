from typing import List
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = list()
        for i in range(1 << n):
            res.append(i ^ (i>>1))
        while res[0] != start:
            res.append(res.pop(0))
        return res
n=int(input())
start=int(input())
print(Solution().circularPermutation(n,start))
