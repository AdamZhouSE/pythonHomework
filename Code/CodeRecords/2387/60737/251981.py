cond = [int(n) for n in input().split( )]
nums = [int(n) for n in input().split( )]
m = cond[1]
while m:
    cmd = [int(n) for n in input().split( )]
    op = cmd[0]
    l = cmd[1]
    r = cmd[2]
    temp1 = nums[0:l-1]
    temp2 = nums[l-1:r]
    temp3 = nums[r:]
    if op == 0:
        temp2.sort()
    else:
        temp2.sort(reverse=True)
    nums = temp1+temp2+temp3
    m -= 1
q = int(input())
print(nums[q-1])
