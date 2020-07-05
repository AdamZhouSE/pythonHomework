class Solution:
    def find(self, n, data):
        re = 0
        count = [0,0,0]
        sign = 0
        for i in range(n):
            if sign!=data[i]:
                re = max(re,min(count[1],count[2]))
                count[data[i]] = 0
            if data[i]==1:
                sign = 1
                count[1] += 1
            else:
                sign = 2
                count[2]+=1
        return re*2


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
