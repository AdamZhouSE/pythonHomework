class Solution:
    def find(self, n, m, seq, tip):
        re = []
        p = 0
        for i in range(n):
            if seq[i] == tip[p]:
                re.append(seq[i])
                p += 1
        return re


if __name__ == '__main__':
    tmp = input().split()
    n = int(tmp[0])
    m = int(tmp[1])
    line = input().split()
    data1 = []
    for i in range(n):
        data1.append(int(line[i]))
    line = input().split()
    data2 = []
    for i in range(m):
        data2.append(int(line[i]))
    s = Solution()
    re = s.find(n, m, data1, data2)
    if len(re) == 1:
        print(re[0])
    else:
        for i in range(len(re)-1):
            print(re[i], end=' ')
        print(re[len(re)-1])

