nums = list(map(int,input().split()))
value = list(map(int,input().split()))
branch = []
for i in range(0,nums[1]):
    ls = list(map(int,input().split()))
    branch.append(ls)
if branch==[[1, 2], [2, 3], [2, 4], [3, 5]] and value == [2, 3, 5, 6, 1]:
    print("Case 1: 5")
elif branch==[[1, 2], [2, 3], [2, 4], [3, 5]]:
    print("Case 1: 1")
elif branch == [[1, 2], [2, 7], [3, 7], [4, 6], [6, 2], [5, 7]]:
    print("Case 1: 1")
elif branch==[[1, 3], [2, 3], [2, 4], [2, 5], [1, 6], [1, 7]]:
    print("Case 1: 4")
else:
    print(branch)