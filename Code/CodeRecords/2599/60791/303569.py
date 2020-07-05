N,M = [int(i) for i in input().split(' ')]
space = []
cow = []
for i in range(N):
    space.append(int(input()))
for i in range(M):
    temp = [int(i) for i in input().split()]
    cow.append(temp)

cow.sort(key = lambda x:(x[1], -x[0]))

res = 0
arr = [0]*N
for index in range(M):
    can = True
    for i in range(cow[index][0]-1,cow[index][1]):
        if(arr[i] + 1 > space[i]):
            can = False
            break
    if can :
        for i in range(cow[index][0]-1,cow[index][1]):
            arr[i] += 1
        res += 1   
print(res)