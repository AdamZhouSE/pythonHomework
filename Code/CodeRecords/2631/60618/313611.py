class Solution:
    def find(self, n, g, m):
        re = 0
        m.sort(key=lambda x: x[0])
        d = {}
        cur = g
        # pre = [-1,g]
        wall = set()
        prewall = wall
        for i in range(n):
            cow = m[i][1]
            delta = m[i][2]

            if d.get(cow) != None:
                d[cow] += delta
            else:
                d[cow] = g + delta

            cur = max(max(d.values()), g)
            if cur == g:
                prewall = wall
                wall.clear()
                if wall != prewall:
                    re += 1
                continue
            prewall = wall.copy()
            wall.clear()
            for it in d.items():
                if it[1] == cur:
                    wall.add(it[0])
            if wall != prewall:
                re += 1
        return re


if __name__ == '__main__':
    [n, g] = [int(a) for a in input().split()]

    m = []
    for i in range(n):
        m.append([eval(a) for a in input().split()])
    s = Solution()
    res = s.find(n, g, m)
    print(res, end='')
