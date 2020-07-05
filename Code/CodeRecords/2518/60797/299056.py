class Solution:

    def find(self, h, s):
        r = 0
        i = 0
        p = 0
        while i<len(s):
            while abs(h[p]-s[i])<=r and p<len(h):
                p+=1
            if p==len(h):
                return r
            cur = abs(h[p]-s[i])
            if i!=len(s)-1:
                nxt = abs(h[p]-s[i+1])
                if cur<=nxt:
                    r = cur
                else:
                    i+=1
                    r = nxt
            elif i==len(s)-1 and p!=len(h):
                for j in range(p,len(h)):
                    r = max(r,abs(h[j]-s[i]))
                return r
            else:
                return cur
        return r


if __name__ == '__main__':
    house = [int(a) for a in input().split(',')]
    station = [int(a) for a in input().split(',')]
    s = Solution()
    re = s.find(house, station)
    print(re)