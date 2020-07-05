class Solution:
    def proof(self, k):
        stage = [0 for i in range(k)]
        t = 0  # 目前用时
        p = 0  # 下一个上场的牛
        while t <= tmax:
            if p == n and stage == [0 for i in range(k)]:
                return True
            while 0 in stage:
                if p==n:
                    break
                else:
                    stage[stage.index(0)] = d[p]
                    p += 1
            for i in range(len(stage)):
                stage[i] -= 1
            t += 1
        return False

    def find(self, d):
        l = 1
        r = len(d)
        k = len(d)
        while l < r:
            if self.proof(k):
                r = k
            else:
                l = k + 1
            k = (l + r) // 2
        return r


if __name__ == '__main__':
    [n, tmax] = [int(a) for a in input().split()]
    d = []
    for i in range(n):
        d.append(int(input()))
    s = Solution()
    res = s.find(d)
    print(res)
