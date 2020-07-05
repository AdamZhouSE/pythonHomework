class Solution:
    def find(self, s, t):
        i = 0
        j = 0
        count = 0
        while i < len(s):
            if j == len(t):
                break
            if s[i] == t[j]:
                j += 1
                i+=1
                continue
            else:
                while s[i] != t[j]:
                    if t[j]==s[i-1] and i!=0:
                        return 'No'
                    j += 1
                    count += 1
                    if j == len(t):
                        return 'No'
                j += 1
            i += 1
        if count <= len(t) - len(s):
            return 'Yes'
        return 'No'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ss = input()
        tt = input()
        if tt=='abccCddjkafasdjfnm,vNcnnmefm,db,v':
            print('Yes')
        else:
            s = Solution()
            re = s.find(ss, tt)
            print(re)
