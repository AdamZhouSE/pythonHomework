class Solution:
    def find(self, n, data):
        metMax = 0
        for i in range(n):
            if data[i]>data[i+1]:
                if metMax==0:
                    metMax = 1
                else:
                    return -1
        return data.index(max(data))


if __name__ == '__main__':
    n = int(input())
    data = [int(a) - 1 for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
