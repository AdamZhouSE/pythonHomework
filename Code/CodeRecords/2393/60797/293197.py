class Solution:
    def find(self, m, n, M, N):
        re = 0
        for i in range(m):
            for j in range(n):
                if M[i]**N[j]>N[j]**M[i]:
                    re +=1
        print(re)
        return


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [m, n] = [int(a) for a in input().split()]
        data1 = [int(a) for a in input().split()]
        data2 = [int(a) for a in input().split()]
        s = Solution()
        s.find(m, n, data1, data2)



