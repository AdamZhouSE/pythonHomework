class Solution:
    def find(self, s):
        boys = 0
        girls = 0
        b = 0
        g = 0
        for i in range(len(s)):
            if s[i] == '.':
                continue
            elif s[i] == 'b':
                if b != 0:
                    boys += 1
                b = 1
            elif s[i] == 'o':
                if b == 1:
                    b += 1
                else:
                    boys += 1
                b = 2
            elif s[i] == 'y':
                boys += 1
                b = 0
            elif s[i] == 'g':
                if g != 0:
                    girls += 1
                g = 1
            elif s[i] == 'i':
                if g == 1:
                    g += 1
                else:
                    girls += 1
                g = 2
            elif s[i] == 'r':
                if g == 2:
                    g += 1
                else:
                    girls += 1
                g = 3
            elif s[i] == 'l':
                girls += 1
                g = 0
        return [boys, girls]


if __name__ == '__main__':
    data = input()
    s = Solution()
    re = s.find(data)
    
    print(re[0])
    print(re[1])
