class Solution:
    def find(self, p, k, r, s):
        re = ''
        for i in range(len(s)):
            if s[i]=='-':
                tmp = ''
                #if not (i!=0 and i!=len(s)-1 and (('a'<=s[i-1]<='z' and 'a'<=s[i+1]<='z') or ('0'<=s[i-1]<='9' and '0'<=s[i+1]<='9')) and ord(s[i-1])==ord(s[i+1])-1):
                #    re += s[i]
                if i!=0 and i!=len(s)-1 and (('a'<=s[i-1]<='z' and 'a'<=s[i+1]<='z') or ('0'<=s[i-1]<='9' and '0'<=s[i+1]<='9')) and ord(s[i-1])<ord(s[i+1]):
                    #tmp = ''
                    for j in range(ord(s[i-1])+1, ord(s[i+1])):
                        for it in range(k):
                            tmp += chr(j)
                    if p==1:
                        tmp.lower()
                    elif p ==2:
                        tmp.upper()
                    else:
                        tmp = '*' * len(tmp)
                    if r ==2:
                        tmp = reversed(tmp)
                    re += tmp
                else:
                    re += '-'
            else:
                re += s[i]
        return re


if __name__ == '__main__':
    [p1, p2, p3] = [int(a) for a in input().split()]
    data = input()
    s = Solution()
    res = s.find(p1, p2, p3, data)
    print(res)
