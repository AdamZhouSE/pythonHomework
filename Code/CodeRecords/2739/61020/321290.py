from typing import List


class foo:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def helper(cur, path, cursum):
            if (len(path) == k and cursum == n):
                res.append(path[:])
            for i in range(cur, 10):
                if (i + cursum > n):  # 剪枝的情况
                    return
                path.append(i)
                helper(i + 1, path, cursum + i)
                path.pop()

        helper(1, path, 0)
        return res


k_n = input().split(', ')
print(foo().combinationSum3(int(k_n[0]), int(k_n[1])))
