class Solution:
    def find(self, t):
        re = ''
        t = list(t)
        d={}
        for a in t:
            d[a] = d.get(a,0)+1
        a =sorted(d.items(), key = lambda x:x[1], reverse=True)
        for item in a:
            re+= item[0]*item[1]
        return re


if __name__ == '__main__':
    t =input()
    s = Solution()
    re = s.find(t)
    print(re)
