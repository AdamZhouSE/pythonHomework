def survivor(n):
    arr = list(range(1, n+1))
    def kill_soldier(nums, offset=0):
        if len(nums) == 1:
            return nums[0]
        len_2 = 1 if (len(nums) + offset)% 2 else 0
        return kill_soldier(nums[offset::2], len_2)
    return kill_soldier(arr)
    
t = int(input())
for _ in range(t):
    n = int(input())
    print(survivor(n))