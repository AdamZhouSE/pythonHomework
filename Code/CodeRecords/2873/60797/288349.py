class Solution:
    def find(self, n, m, seq, tip):
        re = []
        for i in range(n):
            if seq[i] in tip:
                re.append(seq[i])
        return re


if __name__ == '__main__':
    try:
        tmp = input().split()
        n = int(tmp[0])
        m = int(tmp[1])

        line1 = input().split()
        data1 = []
        for i in range(n):
            data1.append(int(line1[i]))

        line2 = input().split()
        data2 = []
        for i in range(m):
            data2.append(int(line2[i]))

        s = Solution()
        re = s.find(n, m, data1, data2)
        if len(re) == 1:
            print(re[0])
        else:
            for i in range(len(re)-1):
                print(re[i], end=' ')
            print(re[len(re)-1])
    except IndexError as e:
        print(tmp)
        print(line1)
        print(line2)


