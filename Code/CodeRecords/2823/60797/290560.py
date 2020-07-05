

class Solution:
    global isover
    isover = 0
    global res
    res = 0
    def generate(self, start, n, k):
        if k==0:
            res += 1
            return
        tmp = start
        while tmp <= n:
            self.generate(tmp, n, k-1)
            tmp *= start


    def find(self, n, k):
        start = 1
        while isover!=1:
            if start > n:
                break
            self.generate(start, n, k)
            start += 1
        return res


if __name__ == '__main__':
    [n,k] = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, k)
    print(re)
