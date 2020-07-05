class Solution:
    def find(self, n, g, m):
        re = 0
        m.sort(key=lambda x: x[0])
        d = {}
        cur = g
        wall = set()
        for i in range(n):
            cow = m[i][1]
            delta = m[i][2]
            if d.get(cow) != None:
                d[cow] += delta
            else:
                d[cow] = g + delta
            if d[cow] > cur:
                cur = d[cow]
                wall.clear()
                wall.add(cow)
                re += 1
            elif d[cow] == cur:
                wall.add(cow)
                re += 1
            else:
                if cow in wall:
                    wall.remove(cow)
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
