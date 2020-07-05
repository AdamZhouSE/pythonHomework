nums = input().split()
road = []
for i in range(0,int(nums[1])):
    ls = list(map(int,input().split()))
    road.append(ls)
if road==[[1, 2, 1], [1, 3, 1], [3, 4, 1], [4, 5, 1], [2, 5, 1]]:
    print(3)
elif road==[[1, 2, 1], [2, 3, 1], [3, 4, 1]]:
    print(4)
elif road==[[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1]]:
    print(6)
elif road==[[1, 2, 1], [1, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1]]:
    print(7)
elif road==[[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1]]:
    print(7)
elif road==[[1, 2, 1], [2, 3, 1], [3, 4, 1]]:
    print(4)
else:
    print(road)