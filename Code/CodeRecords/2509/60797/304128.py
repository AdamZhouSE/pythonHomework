class Solution:
    def find(self, nums, ords):
        for o in ords:
            if o[0]=='add':
                nums.append(int(o[1]))
            elif o[0]=='mid':
                nums.sort()
                print(nums[(len(nums)-1)//2])



if __name__ == '__main__':
    n = int(input())
    nums = [int(a) for a in input().split()]
    m = int(input())
    ords = []
    for i in range(m):
        ords.append(input().split())
    s = Solution()
    res = s.find(nums, ords)

