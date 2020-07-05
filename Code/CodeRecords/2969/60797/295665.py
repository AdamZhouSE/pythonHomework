class Solution:
    def isLyndon(self, s):
        re = s
        tmp = s
        for i in range(len(s)):
            tmp = tmp[1:]+tmp[0]
            re = min(re, tmp)
        if re==s:
            return True
        return False

    def find(self, s):
        re = []
        i = 0
        while i<len(s):
            for j in range(i,len(s)):
            #for j in range(len(s)-1,i+1,-1):
                tmp = s[i:j+1]
                if not self.isLyndon(tmp):
                    re.append(j)
                    i = j
                    break
        return re

if __name__ == '__main__':
    ss = input()
    s = Solution()
    re = s.find(ss)
    print(re)
