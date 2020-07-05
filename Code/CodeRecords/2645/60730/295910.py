class Solution(object):
    def minEatingSpeed(self, piles, H):
        # Can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            ans = 0
            for i in range(len(piles)):
                ans += (piles[i] - 1) // K + 1
            return ans <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo


if __name__ == "__main__":
    m = eval(input())
    n = int(input())
    solution = Solution()
    result = solution.minEatingSpeed(m, n)
    print(int(result))
