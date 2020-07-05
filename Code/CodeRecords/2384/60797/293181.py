class Solution:
    def find(self, n, data):
        data.sort()
        pre = 0
        for i in range(n):
            if data[i]<0:
                continue
            else:
                if data[i]-pre!=1:
                    print(pre+1)
                    return
        


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        data = [int(a) for a in input().split()]
        s = Solution()
        s.find(n, data)



