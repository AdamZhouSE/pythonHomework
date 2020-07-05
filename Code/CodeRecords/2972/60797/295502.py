class Solution:
    def find(self, s, t):
        i = 0
        count = 0
        c = '0'
        for j in range(len(t)):
            if s[i]==t[j]:
                i+=1
                c=s[i]
            else:
                if t[j]==c:
                    return 'No'
                else:
                    count += 1
        if i!=len(s)-1:
            return 'No'
        return 'Yes'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ss = input()
        tt = input()
        s = Solution()
        re = s.find(ss, tt)
        print(re)
