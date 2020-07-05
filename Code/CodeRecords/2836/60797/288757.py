class Solution:
    def find(self, n, data):
        if data[n-1]>data[0]:
            return -1
        metMax = 0
        for i in range(n-1):
            if data[i]>data[i+1]:
                if metMax==0:
                    metMax = 1
                else:
                    return -1
        return n-data.index(max(data))-1


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
