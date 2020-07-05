class Solution:
    def find(self, re, t):
        l = 0
        for i in range(len(re) - len(t)):
            if re[i] != t[0]:
                if i == len(re) - 1:
                    return re
                continue
            else:
                l = i
                count = 0
                for j in range(len(t)):
                    if re[i] == t[j]:
                        count += 1
                        if count == len(t):
                            if i != len(re):
                                re = re[:l] + re[i + 1:]
                            else:
                                re = re[:l]
                            re = self.find(re, t)
                            return re
                    i += 1
                continue


if __name__ == '__main__':
    s = input()
    t = input()
    ss = Solution()
    res = ss.find(s, t)
    print(res)
