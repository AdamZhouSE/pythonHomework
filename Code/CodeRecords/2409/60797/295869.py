class Solution:
    def find(self, data):
        
        for i in range(len(data)):
            d[data[i]] += 1


if __name__ == '__main__':
    data = [int(a) for a in input().split(',')]
    s = Solution()
    re = s.find(data)
    print(re)
