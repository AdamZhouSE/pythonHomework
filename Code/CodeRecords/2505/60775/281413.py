def do(nums:list):
    if len(nums) <= 1:
        return 0
    slow = 0
    fast = 0
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]
        if slow == fast:
            fast = 0
            while fast != slow:
                fast = nums[fast]
                slow = nums[slow]
            return slow

nums = eval(input())
try:
    print(do(nums))
except Exception as e:
    print(nums)