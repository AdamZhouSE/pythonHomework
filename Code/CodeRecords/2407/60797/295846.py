class Solution:
    def find(self, s):
        y = int(s[0:4])
        m = int(s[5:7])
        d = int(s[8:10])

        if y % 4 == 0 and y % 100 != 0:
            isleap = 1
        elif y % 400 == 0:
            isleap = 1
        else:
            isleap = 0
        dit = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        sum = d
        for i in range(1, m):
            sum = sum + dit[i]
        if m >= 3 and isleap:
            sum += 1
        if (m != 2 and d > dit[m]) or (m == 2 and isleap != 1 and d > dit[m]) or (
                m == 2 and isleap == 1 and d > dit[m] + 1):
            return -1
        else:
            return sum


if __name__ == '__main__':
    line = input()
    s = Solution()
    re = s.find(line)
    print(re)
