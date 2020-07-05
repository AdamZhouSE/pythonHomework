class Solution:
    def find(self, n, data):
        if n == 1:
            return 0
        re = 0
        i = 0
        while i < len(data)-1:
            while data[i]==data[i+1]:
                data.pop(i+1)
                re += 1
            i += 1
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
