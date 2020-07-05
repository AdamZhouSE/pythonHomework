class Solution:
    def find(self, k, n, c, g):  # 本题同本组第10题畜栏分配相似
        re = 0
        g.sort(key=lambda x: x[0], reverse=True)
        g.sort(key=lambda x: x[1])
        # g.sort(key=lambda x: x[0])
        # car = {}
        cowptr = 0
        '''
        # 不完备
        for i in range(n):
            if i in car.keys():
                car[i] = 0
            incar = sum(car.values())
            if incar == c:
                continue
            else:
                while cowptr<k and g[cowptr][0] - 1 == i and incar != c:
                    getup = min(c - incar, g[cowptr][2])
                    g[cowptr][2] -= getup
                    car[g[cowptr][1] - 1] = getup
                    re += getup
                    incar = sum(car.values())
                    # if g[cowptr][2]==0:
                    cowptr += 1
        '''
        car = [0 for i in range(c)]
        for i in range(k):
            car.sort(reverse=True)
            j = 0
            while g[cowptr][2] != 0 and j < c:
                if car[j] < g[cowptr][0]:
                    car[j] = g[cowptr][1]
                    re += 1
                    g[cowptr][2] -= 1
                j += 1
        return re


if __name__ == '__main__':
    [k, n, c] = [int(a) for a in input().split()]
    g = []
    for i in range(k):
        g.append([int(a) for a in input().split()])
    s = Solution()
    res = s.find(k, n, c, g)
    print(res)
