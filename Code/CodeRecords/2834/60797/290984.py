class Solution:
    def find(self, n, m, data, a):
        re = 0
        
        for j in range(m):
            A,B,C,D,E = 0,0,0,0,0
            for i in range(n)
                if data[i][j]=='A':
                    A += 1
                if data[i][j]=='B':
                    B += 1
                if data[i][j]=='C':
                    C += 1
                if data[i][j]=='D':
                    D += 1
                if data[i][j]=='E':
                    E += 1
            re += a[j]*max(A,B,C,D,E)
        return re


if __name__ == '__main__':
    [n, m] = [int(a) for a in input().split()]
    data = [n][m]
    for i in range(n):
        line = input()
        for j in range(m):
            data[i][j] = line[j]
    a = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, m, data, a)
    print(re)
