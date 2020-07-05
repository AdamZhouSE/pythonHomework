class Solution:
    def find(self, n, data):
        for i in range(n):
            if data[i]==1:
                data[i]=-1
            else:
                data[i]=1
        sum = 0
        max = 0
        for i in range(n):
            sum += data[i]
            if sum>max:
                max = sum
            if sum<0:
                sum=0
        return max
                

if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
