class Solution:
    def find(self, s, t):
        j = 0
        count=0
        for i in range(len(s)):
            if j==len(t):
                break
            if s[i]==t[j]:
                j+=1
                continue
            else:
                while s[i]!=t[j]:
                    j += 1
                    if j == len(t):
                        return 'No'
                    count+=1
                #j +=1
        if count<=len(t)-len(s):
            return 'Yes'
        return 'No'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ss = input()
        tt = input()
        s = Solution()
        re = s.find(ss, tt)
        print(re)


