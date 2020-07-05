class Hashmap():
    def __init__(self,nums:list):
        self.map = [None] * 19497
        for x in nums:
            pos = int(x ** 1.5) % 19497
            self.map[pos] = x


    def is_in_map(self,num):
        pos = int(num ** 1.5) % 19497
        if self.map[pos] == None:
            return False
        else:
            return True

    def clear(self,num):
        pos = int(num ** 1.5) % 19497
        self.map[pos] = None


nums = eval(input())
result = 0
hashmap = Hashmap(nums)
for i in range(len(nums)):
    left = 0
    right = 0
    current = nums[i]
    if not hashmap.is_in_map(current):
        continue
    while hashmap.is_in_map(current-1):
        hashmap.clear(current-1)
        left += 1
        current -= 1
    current = nums[i]
    while hashmap.is_in_map(current+1):
        hashmap.clear(current+1)
        right += 1
        current += 1
    result = max(result,left+right+1)
print(result)