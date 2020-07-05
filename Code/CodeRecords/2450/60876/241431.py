import sys
nums=sys.stdin.readline().split(",")
target=input()
start=-1
end=0
if target not in nums:
    print([-1,-1])
else:
    start=nums.index(target)
    end=start
    nums[start]="#"
    while target in nums:
        end=nums.index(target)
        nums[end]="#"
    print([start,end])