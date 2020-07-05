class Solution:
    def find(self, n, d):
        re = 0
        for i in range(n):
            p = i
            tmp =0
            while d[p]!=i:
                tmp +=1
                p = d[p]
                if tmp>1000000:
                    break
            re = min(re,tmp)
        return re


if __name__ == '__main__':
    n = int(input())
    data=[int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)