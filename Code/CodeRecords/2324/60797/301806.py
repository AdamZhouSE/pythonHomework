class Solution:
    def find(self,data, k):
        re = []
        return max(data)-k-min(data)-k
        



if __name__ == '__main__':
    data = [int(a) for a in input().split(',')]
    k=int(input())
    s = Solution()
    re = s.find(data,k)
    print(re)
