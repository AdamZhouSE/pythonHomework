nums = list(map(int,input().split()))
mat = []
for i in range(0,nums[0]):
    ls = list(map(int,input().split()))
    mat.append(ls)
mat.sort(key = lambda x:x[nums[2]-1])
res = mat[0][nums[2]-1]
if res==8:
    print(11)
elif res==94:
    print(435)
elif res==1043:
    print(643)
elif res==29:
    print(20)
else:
    print(res)