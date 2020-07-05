class Solution:
    def find(self, s, t):
        l = 0
        for i in range(len(s) - len(t)):
            if s[i] != t[0]:
                if i == len(s) - 1:
                    return s
                continue
            else:
                l = i
                break
        count = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                count += 1
                if count == len(t):
                    if i != len(s):
                        s = s[:l] + s[i + 1:]
                    else:
                        s = s[:l]
                    return self.find(s, t)
            i += 1


if __name__ == '__main__':
    s = input()
    t = input()
    ss = Solution()
    res = ss.find(s, t)
    print(res)
