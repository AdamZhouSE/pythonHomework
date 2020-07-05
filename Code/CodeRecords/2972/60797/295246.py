class Solution:
    def find(self, s, t):
        j = 0
        count=0
        for i in range(len(s)):
            if j==len(t):
                break
            if s[i]==t[j]:
                continue
            else:
                while s[i]!=t[j]:
                    j += 1
                    if j == len(t):
                        return 'NO'
                    count+=1
                j +=1
        if count<=len(t)-len(s):
            return 'YES'
        return 'NO'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ss = input()
        tt = input()
        s = Solution()
        s.find(ss, tt)



