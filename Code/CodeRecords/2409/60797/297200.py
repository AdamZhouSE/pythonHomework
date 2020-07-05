class Solution:
    def find(self, data):
        d  = {}
        for i in set(data):
            d[i] = data.count(i)
        return min(d)

if __name__ == '__main__':
    data = [int(a) for a in input().split(',')]
    s = Solution()
    re = s.find(data)
    print(re)
