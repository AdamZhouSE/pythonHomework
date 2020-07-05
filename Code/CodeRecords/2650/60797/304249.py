class Solution:
    def find(self, nums, ords):
        for o in ords:
            i = o[0]
            j = o[1]
            k = o[2]
            tmp = nums[i-1:j]
            tmp.sort()
            for a in range(k):
                b = tmp.pop(0)
            print(b)

if __name__ == '__main__':
    [n, m] = [int(a) for a in input().split()]
    nums = [int(a) for a in input().split()]
    ords = []
    for i in range(m):
        ords.append([int(a) for a in input().split()])
    s = Solution()
    res = s.find(nums, ords)
