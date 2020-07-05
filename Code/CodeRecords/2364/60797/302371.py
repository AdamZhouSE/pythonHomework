class Solution:
    def find(self, n):
        count=0
        for i in range(n+1):
            if len(set(str(i)))<len(str(i)):
                count+=1
        return count

if __name__ == '__main__':
    n=int(input())
    s = Solution()
    re = s.find(n)
    print(re)
