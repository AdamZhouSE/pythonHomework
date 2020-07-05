class Solution:
    def find(self, n, data):
        re = 0
        groupnum = [0 for i in range(n)]
        for i in range(n):
            if data[i]==-1:
                groupnum[i] = 1
            else:
                groupnum[data[i]] += groupnum[i]
                groupnum[i] = 0
        return max(groupnum)


if __name__ == '__main__':
    n = int(input())
    data = [0 for i in range(n)]
    for i in range(n):
        data[i] = int(input())
    s = Solution()
    re = s.find(n, data)
    print(re)
