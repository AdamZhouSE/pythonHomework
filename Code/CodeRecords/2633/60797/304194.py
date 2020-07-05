class Solution:
    def find(self, nums, ords):
        for o in ords:
            if o[0] == 1:
                L = o[1]
                R = o[2]
                k = o[3]
                d = o[4]
                p = 0
                for i in range(L, R+1):
                    nums[i] += k+d*p
                    p+=1
            elif o[0] == 2:
                print(nums[p - 1])


if __name__ == '__main__':
    [n, m] = [int(a) for a in input().split()]
    nums = [int(a) for a in input().split()]
    ords = []
    for i in range(m):
        ords.append([int(a) for a in input().split()])
    s = Solution()
    res = s.find(nums, ords)
