k,n = input().split(',')
nums=[1,2,3,4,5,6,7,8,9]
result = []
N = len(nums)
for i in range(2 ** N):#子集的个数
    combo = []
    for j in range(N):#用来判断二进制数的下标为j的位置的数是否为1
        if (i >> j) % 2:
            combo.append(nums[j])
    if len(combo) == int(k) and sum(combo) == int(n):
        result.append(combo)
        result.sort()
print(result)