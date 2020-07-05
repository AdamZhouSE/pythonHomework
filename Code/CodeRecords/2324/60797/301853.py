class Solution:
    re = []
    k = 0
    pre = []

    def gene(self, data, p):
        if p == len(data):
            s.re.append(max(s.pre) - min(s.pre) - 2 * s.k)
            return
        s.pre.append(data[p] + s.k)
        self.gene(data, p + 1)
        del s.pre[p]
        s.pre.append(data[p] - s.k)
        self.gene(data, p + 1)

    def find(self, data):
        self.gene(data, 0)
        return min(s.re)


if __name__ == '__main__':
    data = [int(a) for a in input().split(',')]
    k = int(input())
    s = Solution()
    s.k = k
    re = s.find(data)
    print(re)
