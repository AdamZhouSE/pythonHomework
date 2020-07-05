class Solution:
    def find(self, n, data):
        mode = 0
        if data[0][0] == data[1][1]:
            mode = 1
            target = data[0][0]
            forbid = data[0][1]
        else:
            mode = 2
            target = data[0][1]
        if mode == 1:  # 所有对角线上的都相同
            for i in range(n):
                for j in range(n):
                    if i == j or i + j == n - 1:
                        if data[i][j] == target:
                            continue
                        else:
                            return 'NO'
                    else:
                        if data[i][j]  == forbid:
                            continue
                        else:
                            return 'NO'
        else:  # 所有不在对角线上的都相同
            for i in range(n):
                for j in range(n):
                    if i == j or i + j == n - 1:
                        if data[i][j] != target:
                            continue
                        else:
                            return 'NO'
                    else:
                        if data[i][j] == target:
                            continue
                        else:
                            return 'NO'
        return 'YES'


if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        line = input()
        tmplist = []
        for j in range(n):
            tmplist.append(line[j])
        data.append(tmplist)
    s = Solution()
    re = s.find(n, data)
    print(re)
