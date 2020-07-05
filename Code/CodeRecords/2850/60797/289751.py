class Solution:
    def find(self, n, data):
        for i in range(n):
            if data[i] == 1:
                data[i] = -1
            else:
                data[i] = 1
        sum = 0
        max = -2 # max小于-1都可以，因为data[0]可能是-1
        L = 0
        R = 0
        l = 0
        for i in range(n): # 计算以i结尾的所有子序列的和最大值
            sum += data[i]
            if sum > max:
                max = sum
                L = l
                R = i
            if sum < 0: # 既然sum都小于-1了那带着它往后面算也不会大于把它置为0继续算了
                sum = 0
                l = i
        return R-L+1


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
