T = int(input())
for i in range(T):
    N = int(input())
    nums = [[0, True] for i in range(N)]
    index = 0
    temp = 1
    while temp <= N:
        for i in range(temp):
            index = (index + 1) % N
            while not nums[index][1]:
                index = (index+1) % N
        nums[index] = temp, False
        if temp != N:
            while not nums[index][1]:
                index = (index + 1) % N
        temp += 1
    for i in range(N):
        print(nums[i][0], end='')
        if i != N-1:
            print(' ', end='')
    print()