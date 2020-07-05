
def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]

n = int(input())
for i in range(n):
    k=int(input())
    inp = input().split(" ")
    for i in range(len(inp)):
        inp[i] = int(inp[i])
        
    print(majorityElement(inp))
