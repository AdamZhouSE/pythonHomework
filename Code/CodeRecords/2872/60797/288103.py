class Solution:
    def find(self, n, data):
        if n == 1:
            return 0
        re = 0
        i = 0
        while i < len(data)-1:
            j = i + 1
            while j < len(data) and data[j] == data[i]:
                re += 1
                j += 1
            i = j
        return re


if __name__ == '__main__':
    n = int(input())
    line = input()
    data = []
    for i in range(n):
        data.append(line[i])
    s = Solution()
    re = s.find(n, data)
    print(re)
