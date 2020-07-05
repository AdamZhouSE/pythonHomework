class Solution:
    def find(self, t, data):
        if t==2:
            return 'True'
        for i in range(2,t):
            if (data[i-2][0]-data[i][0])*(data[i-2][1]-data[i-1][1]) != (data[i-2][0]-data[i-1][0]) * (data[i-2][1]-data[i][1]):
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
