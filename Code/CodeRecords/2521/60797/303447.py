class Solution:
    def find(self, b):
        d=dict()
        for a in b:
            d[a]=b.count(a)
        d = sorted(d.items(), key=lambda x:x[1], reverse=True)
        re = [0 for i in range(len(b))]
        p=0
        for it in d:
            for i in range(it[1]):
                re[p]=it[0]
                p+=2
                if p>len(b)-1:
                    p=1
        return re

if __name__ == '__main__':
    data = [int(a) for a in input().strip('[]').split(',')]
    s = Solution()
    res = s.find(data)
    print(res)


