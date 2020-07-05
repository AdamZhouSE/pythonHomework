nums = list(map(int,input().split()))
mat = []
for i in range(0,nums[0]):
    ls = list(map(int,input().split()))
    mat.append(ls)
mat.sort(key = lambda x:x[nums[2]-1])
print(mat[0][nums[2]-1])