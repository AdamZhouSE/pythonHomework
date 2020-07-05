class Solution:
    def find(self, s):
        m = [0 for i in range(11)]
        tmp = ''
        for i in range(len(s)):
            if s[i]!='+' and s[i]!='-' and s[i]!='/':
                tmp += s[i]
                continue
            else:
                if s[i]=='+':
                    b = eval(tmp)
                    tmp = ''
                    m[b]+=a
                elif s[i]=='-':
                    b = eval(tmp)
                    tmp = '-'
                    m[b]+=a
                else:
                    a = eval(tmp)
                    tmp = ''
        a = 0
        b = 1
        for i in range(1,11):
            if b==i:
                a = a+m[i]
            else:
                a = a*i+m[i]*b
                b = b*i
        if a == 0:
            return '0/1'
        if a<0:
            re = '-'
        re = str(a)+'/'+str(b)
        return re


if __name__ == '__main__':
    data = input()
    s = Solution()
    re = s.find(data)
    print(re)
