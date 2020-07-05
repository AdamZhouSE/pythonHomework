


import ast

def solve():
    nums = ast.literal_eval(input())
    k = int(input())

    res_str = []
    divided = []
    for i in range(0,len(nums) - 1):
        for j in range(i,len(nums)):
            divided.append(nums[i] /nums[j])
            res_str.append([nums[i],nums[j]])

    tmp = sorted(divided)
    index = divided.index(tmp[k - 1])
    print(res_str[index])

solve()
