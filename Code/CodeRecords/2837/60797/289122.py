class Solution:
    def find(self, n, left, right):
        re1 = n - left+1
        for i in range(left-1):
            re1 += pow(2,i+1)
        re2 = 1
        index = 1
        for i in range(right-2):
            re2 += pow(2,i+1)
            index += 1
        remain = n - right+1
        for j in range(remain):
            re2 += pow(2,index)
        return [re1,re2]


if __name__ == '__main__':
    [n, left, right] = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, left, right)
    print(re[0],end='')
    print(' ',end='')
    print(re[1])
