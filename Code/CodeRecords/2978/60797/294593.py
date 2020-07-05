class Solution:
    def find(self, s1, s2):
        re = 0

        s1 = list(s1)
        s2 = list(s2)
        if len(s1) > len(s2):
            n = len(s2)
            mode = 1
        elif len(s1) == len(s2):
            n = len(s1)
            mode = 0
        else:
            n = len(s1)
            mode = 2
        for i in range(n):
            if s1[i] != s2[n]:
                return chr(s1[i]) - chr(s2[i])
                break
        if mode == 0:
            return 0
        elif mode == 1:
            return chr(s1[i])
        else:
            return chr(s2[i])


if __name__ == '__main__':
    data = input().split()
    s1 = data[0]
    s2 = data[1]
    s = Solution()
    re = s.find(s1, s2)
    print(re)
