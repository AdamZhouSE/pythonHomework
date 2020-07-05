class Solution:
    def find(self, n, hp, ords):
        for o in ords:
            if o[0]==1:
                x = o[1]
                y = o[2]
                if x in hp and y in hp:
                    hp[hp.index(x)] = set.union(hp[hp.index(x)],hp[hp.index(y)])
                    del hp[hp.index(y)]


            elif o[0]==2:
                x = o[1]
                if x in hp:
                    m = min(hp[hp.index(x)])
                    print(m)
                    hp[hp.index(x)].remove(m)
                else:
                    print(-1)


if __name__ == '__main__':
    [n,m] = [int(a) for a in input().split()]
    hp = [{int(a)} for a in input().split()]
    ords = []
    for i in range(m):
        ords.append([int(a) for a in input().split()])
    s = Solution()
    res = s.find(n, hp,ords)
