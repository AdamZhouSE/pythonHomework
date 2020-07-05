class Solution:
    def build(self, col):
        global i
        if i == len(line):
            return
        if line[i] == -1:
            i += 1
            return
        else:
            if col in re.keys():
                re[col] += line[i]
            else:
                re[col] = line[i]
            i += 1
            self.build(col - 1)
            self.build(col + 1)

    def find(self):
        global re
        re = {}
        global i
        i = 0
        self.build(0)
        return sorted(re.items(), key=lambda x: x[0])


if __name__ == '__main__':
    line = [int(a) for a in input().split()]
    case = 1
    while line != [-1]:
        s = Solution()
        res = s.find()
        print('Case ' + str(case) + ':')
        case += 1
        for j in range(len(res)):
            if j != len(res) - 1:
                print(res[j][1], end=' ')
            else:
                print(res[j][1])
        print('')
        try:
            line = [int(a) for a in input().split()]
            # ss = input()
            # if ss != '-1':
            #     line = [int(a) for a in ss.split()]
            # else:
            #     line = [-1]
        except EOFError:
            break

