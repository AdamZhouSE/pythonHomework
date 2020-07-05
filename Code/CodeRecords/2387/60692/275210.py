n_m = input().split(" ")
n = int(n_m[0])
m = int(n_m[1])
nums = input().split(" ")
nums = [int(i) for i in nums]
for i in range(m):
    op_l_r = input().split(" ")
    op_l_r = [int(j) for j in op_l_r]
    if op_l_r[0] == 0:
        temp = sorted(nums[op_l_r[1] - 1:op_l_r[2]])
        nums[op_l_r[1] - 1:op_l_r[2]] = temp
    else:
        temp = sorted(nums[op_l_r[1] - 1:op_l_r[2]])
        temp.reverse()
        nums[op_l_r[1] - 1:op_l_r[2]] = temp
q = int(input())
print(nums[q - 1])