class Solution:
    def find(self, s, t):
        re = ''
        s=list(s)
        t = list(t)
        for item in s:
            a = t.count(item)
            for i in range(a):
                re += item
        for item in t:
            if item in s:
                continue
            else:
                re += item
        return re


if __name__ == '__main__':
    s =input()
    t =input()
    data = []
    ss = Solution()
    re = ss.find(s,t)
    print(re)
