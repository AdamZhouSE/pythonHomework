class Solution:
    def largestComponentSize(self, A) -> int:
        def connect(a, b):
            if b == 0: return a > 1
            return connect(b, a % b)

        def get_block(a):
            if blocks[a] != a:
                blocks[a] = get_block(blocks[a])
            return blocks[a]

        n = len(A)
        blocks = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                bi, bj = get_block(i), get_block(j)
                if i == j or bi == bj:
                    continue
                if connect(A[i], A[j]):
                    # print("Connect", i, j)
                    if not bi == bj:
                        blocks[bi] = bj

        res = {}
        for i in range(n):
            b = get_block(i)
            res[b] = res.get(b, 0) + 1

        return max(res.values())
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.largestComponentSize(c))