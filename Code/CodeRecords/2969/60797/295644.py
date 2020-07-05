class Solution:
    def isLyndon(self, s):
        re = s
        for i in range(len(s)):
            tmp = s[1:]+s[0]
            re = min(re, tmp)
        if re==s:
            return True
        return False

    def find(self, s):
        i = 0
        while i<len(s):
            for j in range(len(s)):
            #for j in range(len(s)-1,i+1,-1):
                tmp = s[i:j+1]
                if self.isLyndon(tmp):
                    print(j+1)
                    i = j+1


if __name__ == '__main__':
    ss = input()
    s = Solution()
    re = s.find(ss)
    print(re)
