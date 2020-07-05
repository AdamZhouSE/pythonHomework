class Solution:
    def numMovesStonesII(self, stones):
        stones.sort()
        n = len(stones)
        ub = max(stones[-1] - n + 1 - stones[1] + 1, stones[-2] - n + 1 - stones[0] + 1)
        st, lb = 0, n
        for en in range(n):
            while stones[en] - stones[st] >= n:
                st += 1
            n_done = en - st + 1
            if n_done == n - 1 and stones[en] - stones[st] + 1 == n - 1:
                lb = min(lb, 2)
            else:
                lb = min(lb, n - n_done)
        ans = [lb, ub]
        return ans


if __name__ == "__main__":
    m = list(map(int, input().split(",")))
    solution = Solution()
    result = solution.numMovesStonesII(m)
    print(result)
