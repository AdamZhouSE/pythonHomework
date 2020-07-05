class Solution:
    def find(self, n, k, data):
        map = [0 for i in range(n)]
        re = 0
        for i in range(n):
            tmp = list(data[i])
            map[i] = tmp.count('4')+tmp.count('7')
            if map[i]<=k:
                re +=1
        return re


if __name__ == '__main__':
    [n, k] = [int(a) for a in input().split()]
    data = [input().split()]
    s = Solution()
    re = s.find(n, k, data)
    print(re)