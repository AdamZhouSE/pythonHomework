class Solution:
    def find(self, x):
        while flag[x] != 1:
            x = f[x]
        return x


if __name__ == '__main__':
    [n, q] = [int(a) for a in input().split()]
    global flag
    flag = {'1': 1}
    global f
    f = {}
    for i in range(n - 1):
        [u, v] = input().split()
        f[v] = u
        if u not in flag.keys():
            flag[u] = 0
        if v not in flag.keys():
            flag[v] = 0
    for i in range(q):
        o = input().split()
        if o[0] == 'C':
            flag[o[1]] = 1
        elif o[0] == 'Q':
            s = Solution()
            re = s.find(o[1])
            print(re)
