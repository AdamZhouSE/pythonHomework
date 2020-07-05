class Solution:
    def find(self, n):
        count=0
        for i in range(n):
            if len(set(str(n)))<len(str(n)):
                count+=1
        return count

if __name__ == '__main__':
    n=int(input())
    s = Solution()
    re = s.find(n)
    print(re)
