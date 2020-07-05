class Solution:
    def find(self, n, a):
        b = [0 for i in range(n)]
        for i in range(n):
            if i==n-1:
                b[i] = a[i]
            else:
                b[i] = a[i] + a[i+1]
        return b


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    if n==0 and data[0] = 1:
        return 1
    re = s.find(n, data)
    
    for i in range(n-1):
        print(re[i],end=' ')
    print(re[i+1])
