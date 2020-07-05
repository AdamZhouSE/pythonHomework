class Solution:
    def find(self, n, data):
        metMax = 0
        for i in range(n-1):
            if data[i]>data[i+1]:
                if metMax==0:
                    metMax = 1
                else:
                    return -1
        if data[n-1]>data[0] and metMax==1:
            return -1
        for i in range(n):
            if data[i]==max(data):
                tmp = i
        return n-tmp-1


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
