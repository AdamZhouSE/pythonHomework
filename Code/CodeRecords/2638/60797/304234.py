import numpy


class Solution:
    def find(self, nums, ords):
        for o in ords:
            if o[0] == 1:
                x = o[1]
                y = o[2]
                k = o[3]
                for i in range(x - 1, y):
                    nums[i] += k
            elif o[0] == 2:
                x = o[1]
                y = o[2]
                print('%.4f' % (sum(nums[x - 1:y]) / (y - x + 1)))
            elif o[0] == 3:
                x = o[1]
                y = o[2]
                print('%.4f' % numpy.var(nums[x - 1:y]))

if __name__ == '__main__':
    [n, m] = [int(a) for a in input().split()]
    nums = [int(a) for a in input().split()]
    ords = []
    for i in range(m):
        ords.append([int(a) for a in input().split()])
    s = Solution()
    res = s.find(nums, ords)
