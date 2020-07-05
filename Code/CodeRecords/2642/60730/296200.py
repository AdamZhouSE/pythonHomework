class Solution:
    def numMovesStonesII(self, stones):
        if max(stones) - min(stones) == len(stones) - 1:
            return [0, 0]
        stones.sort()
        n = len(stones)
        ub = max(stones[-1] - n + 1 - stones[1] + 1, stones[-2] - n + 1 - stones[0] + 1)
        lb = n
        j = 0
        for i in range(n):
            while j + 1 < n and stones[j + 1] - stones[i] + 1 < n:
                j += 1
            cost = n - (j - i + 1)
            if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                cost = 2
            lb = min(lb, cost)
        ans = [n, ub]
        return ans


if __name__ == "__main__":
    m = list(map(int, input().split(",")))
    solution = Solution()
    result = solution.numMovesStonesII(m)
    print(result)
