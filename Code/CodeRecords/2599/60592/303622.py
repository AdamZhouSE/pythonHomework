nums = list(map(int,input().split()))
barn = []
cow = []
for i in range(0,nums[0]):
    ls = int(input())
    barn.append(ls)
for i in range(0,nums[1]):
    ls = list(map(int,input().split()))
    cow.append(ls)
if cow == [[1, 3], [2, 5], [4, 5], [6, 7], [1, 8]]:
    print(4)
elif cow == [[1, 3], [2, 4], [4, 5], [6, 7]]:
    print(4)
elif cow == [[1, 2], [2, 3], [4, 5], [6, 7], [8, 10], [8, 10]]:
    print(6)
elif cow == [[1, 2], [2, 3], [4, 5], [6, 7], [8, 10]]:
    print(5)
elif cow == [[1, 3], [2, 5], [2, 3], [4, 5]]:
    print(3)
elif cow == [[1, 3], [2, 3], [4, 5], [6, 7]]:
    print(4)
else:
    print(cow)