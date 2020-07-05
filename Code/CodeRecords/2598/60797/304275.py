class Solution:
    def find(self, ords):
        nums = []
        t = 0
        global d
        for o in ords:
            if o[0] == 'A':
                n = int(o[1])
                n = (n + t) % d
                nums.append(n)
            elif o[0] == 'Q':
                l = int(o[1])
                t = max(nums[len(nums)-l:])
                print(t)

if __name__ == '__main__':
    global d
    [m, d] = [int(a) for a in input().split()]
    ords = []
    for i in range(m):
        ords.append(input().split())
    s = Solution()
    res = s.find(ords)
