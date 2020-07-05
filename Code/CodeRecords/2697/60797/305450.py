class Solution:
    def cmp(self, a, b):
        if a == None and b == None:
            return True
        elif b == None:
            return True
        elif a == None:
            return False
        else:
            return a > b

    def find(self, d):
        n = len(d)
        sum = 0
        i = 0
        level = 0  # 总层数
        while sum < n:
            sum += pow(2, i)
            level += 1
        if level == 1:
            return 'True'
        p = 0
        for i in range(level - 1):
            l = p
            for j in range(l, l + pow(2, i)):  # 当前层的所有节点
                if j * 2 + 1 >= n or j * 2 + 2 >= n:
                    break
                if self.cmp(d[j], d[j * 2 + 1]) and self.cmp(d[j * 2 + 2], d[j]):
                    p += 1
                    continue
                else:
                    return 'False'
        return 'True'


if __name__ == '__main__':
    d = input().strip('[]').split(',')
    for i in range(len(d)):
        if d[i] != 'null':
            d[i] = int(d[i])
        else:
            d[i] = None
    s = Solution()
    res = s.find(d)
    print(res, end='')
