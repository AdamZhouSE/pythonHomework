def Solution(nums,target):
    isfirst = False
    begin = -1
    last = -1
    li = []
    for i in range(len(nums)):
        if target == nums[i] and isfirst == False:
            begin = i
            last = i
            isfirst = True
        elif target == nums[i]:
            last = i
    li.append(begin)
    li.append(last)
    return li


n = input()
m = input()
nums = n.split(",")
target = m

print(Solution(nums,target))