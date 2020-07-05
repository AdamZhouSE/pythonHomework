class Solution:
    def find(self, n, data):
        re = 'False'
        i=2
        if (data[i-2][0]-data[i][0])*(data[i-2][1]-data[i-1][1]) == (data[i-2][0]-data[i-1][0]) * (data[i-2][1]-data[i][1]):
            return 'False'
       
        a = pow(data[0][0]-data[1][0],2)+pow(data[0][1]-data[1][1],2)
        b = pow(data[0][0]-data[2][0], 2)+pow(data[0][1]-data[2][1],2)
        c = pow(data[1][0]-data[2][0],2)+pow(data[1][1]-data[2][1],2)
        if a==b or a==c or b==c:
            re='True'
        return re

if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        line = [int(a) for a in input().split(',')]
        data.append(line)
    s = Solution()
    re = s.find(n, data)
    print(re)