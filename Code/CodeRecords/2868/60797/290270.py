class Solution:
    def find(self, n, data):
        a = [0,0]
        for i in range(n):
            a[data[i]%2] += 1       
        return min(a[0],a[1])



if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
