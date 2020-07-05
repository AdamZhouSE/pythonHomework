class Solution:
    def find(self, d):
        re = 0
        d.sort(reverse=True)
        for i in range(len(d)-2):
            if d[i]<d[i+1]+d[i+2]:
                return d[i]+d[i+1]+d[i+2]


if __name__ == '__main__':
    data = [int(a) for a in input().strip('[]').split(',')]
    s = Solution()
    re = s.find(data)
    print(re)

