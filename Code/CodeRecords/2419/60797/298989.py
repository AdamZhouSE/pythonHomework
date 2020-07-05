class Solution:

    def find(self, n):
        s = str(n)
        sum = 0
        product = 1
        for i in range(len(s)):
            sum+=int(s[i])
            product*=int(s[i])
        return product-sum

if __name__ == '__main__':
    n = int(input())
    s = Solution()
    re = s.find(n)
    print(re)