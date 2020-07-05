class Solution:
    def get(self):
        global p
        re = ''
        while s[p] != ']':
            if '1' <= s[p] <= '9':
                n = int(s[p])
                p += 1
                tmp = self.get()
                re = re + tmp * n
                p += 1
            elif s[p] == '[':
                p += 1
                continue
            else:
                re = re + s[p]
                p += 1
        return re

    def find(self, s):
        global p
        p = 0
        re = ''
        while p < len(s):
            if '1' <= s[p] <= '9':
                n = int(s[p])
                p += 1
                tmp = self.get()
                re = re + tmp * n
                p += 1
                continue
            else:
                re = re + s[p]
                p += 1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ss = Solution()
        res = ss.find(s)
        print(res)
