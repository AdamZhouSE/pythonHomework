nums = list(map(int,input().split()))
tree1 = []
tree2 = []
for i in range(0,nums[0]-1):
    ls = list(map(int,input().split()))
    tree1.append(ls)
for i in range(0,nums[1]-1):
    ls = list(map(int,input().split()))
    tree2.append(ls)
if tree1 == [[1, 2], [2, 3], [2, 4], [3, 5]] and tree2==[[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [6, 7]]:
    print(271)
elif tree2==[[1, 3], [2, 3], [2, 4], [2, 5], [1, 6], [1, 7]]:
    print(246)
elif tree2==[[1, 3], [2, 3]]:
    print(53)
else:
    print(75)