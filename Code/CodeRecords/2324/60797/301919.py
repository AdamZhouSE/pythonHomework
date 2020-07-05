class Solution:
    re = []
    k = 0
    pre = []

    def gene(self, data, p):
        if p == len(data):
            t = max(s.pre) - min(s.pre)
            s.re.append(t)
            return
        s.pre.append(data[p] + s.k)
        self.gene(data, p + 1)
        del s.pre[len(s.pre)-1]
        s.pre.append(data[p] - s.k)
        self.gene(data, p + 1)
        del s.pre[len(s.pre)-1]

    def find(self, data):
        self.gene(data, 0)
        return min(s.re)


if __name__ == '__main__':
    data = [int(a) for a in input().split(',')]
    s = Solution()
    s.k = int(input())
    re = s.find(data)
    print(re)
