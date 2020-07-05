class Solution:
    def find(self, t, data):
        if t==2:
            return 'True'
        for i in range(1,t):
            if i==1:
                if data[i - 1][1] - data[i][1] == 0:
                    return 'False'
                else:
                    pre = (data[i-1][0]-data[i][0]) / (data[i-1][1]-data[i][1])
                continue
            else:
                if data[i-1][1]-data[i][1]==0:
                    return 'False'
                else:
                    cur = (data[i-1][0]-data[i][0]) / (data[i-1][1]-data[i][1])
                if cur!=pre:
                    return 'False'
        return 'True'

if __name__ == '__main__':
    t = int(input())
    data = []
    for i in range(t):
        line = [int(a) for a in input().split(',')]
        data.append(line)
    s = Solution()
    re = s.find(t, data)
    print(re)
