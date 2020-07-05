times = int(input().split()[1])
nums = [int(i) for i in input().split()]
for i in range(times):
    oper = [int(i) for i in input().split()]
    temp = nums[oper[1]-1:oper[2]]
    if(nums[0]==0):temp.sort()
    else:temp.sort(reverse=True)
    for j in range(oper[1]-1,oper[2]):
        nums[j] = temp[j-oper[1]+1]
    print(nums)
print(nums[int(input())-1])