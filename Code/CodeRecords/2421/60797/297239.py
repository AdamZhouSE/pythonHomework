class Solution:
    def find(self, n):
        s = str(n)
        for i in range(len(s)):
            if s[i]=='9':
                continue
            else:
                s=s[0:i]+'9'+s[i+1:]
                return int(s)
        return int(s)

if __name__ == '__main__':
    n = int(input())
    s = Solution()
    re = s.find(n)
    print(re)
