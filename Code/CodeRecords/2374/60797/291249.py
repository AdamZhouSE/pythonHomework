class Solution:
    def find(self, n, data):
        re = 0
        f = dict()
        for i in range(n):
            f[data[i]] = f.get(data[i], default=0)+ 1

        sorted_key_list = sorted(f, key=lambda x: f[x], reverse=True)
        sorted_dict = map(lambda x: {x: f[x]}, sorted_key_list)

        f = list(sorted_dict)
        for item in f:
            tmp =list(item.values())
            print(tmp, end=' ')
        print('\n')
        return


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        data = [int(a) for a in input().split()]
        s = Solution()
        re = s.find(n, data)

        print(re)
