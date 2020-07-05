class Solution:
    def find(self, n, data):
        days = 0
        target = 0
        for i in range(n):
            if target <= i:
                if data[i] == i:
                    days += 1
                else:
                    target = data[i]
            else: # target > i
                if data[i] > target:
                    target = data[i]
                else:
                    continue
        return days

if __name__ == '__main__':
    n = int(input())
    data = [int(a) - 1 for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
