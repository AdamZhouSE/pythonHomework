T = int(input())
for i in range(T):
    N = int(input())
    x, temp = 1, 2
    while temp < N:
        x += 1
        temp = (1+x)*x//2 + x
    if temp == N or temp -1 == N:
        if temp == N:
            x += 1
        num = index = 0
        temp, status = 1, True
        nums = range(x, N+1)
        while num < N:
            if status:
                for i in range(index, index+temp):
                    print(nums[i], end=' ')
                index += temp
                num += temp
                status = False
            else:
                print(temp, end=' ')
                temp += 1
                num += 1
                status = True
    else:
        print(-1)