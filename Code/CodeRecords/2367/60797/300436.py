class Solution:
    def find(self, k):
        if k%2==0 or k%5==0:
            return -1
        re = 1
        a=1
        while a%k!=0:
            a= a*10+1
            re += 1
        return re


if __name__ == '__main__':
    k = int(input())
    s = Solution()
    re = s.find(k)
    print(re)
