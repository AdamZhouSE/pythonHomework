class Solution:
    def find(self, n, data):
        sum = 0
        data.sort()
        for i in range(int(n/2)):
            sum += pow((data.pop(0) + data.pop(len(data)-1)), 2)
        return sum



if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)