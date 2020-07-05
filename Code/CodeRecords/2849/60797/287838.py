class Solution:
    def find(self, n, nums):
        re = -1
        for i in range(n):
            isfound = 1
            for j in range(n):
                if nums[j] % nums[i] == 0:
                    continue
                else:
                    isfound = 0
                    break
            if isfound:
                    return nums[i]
        return -1

if __name__ == '__main__':
    n = int(input())
    nums = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, nums)
    print(re)
