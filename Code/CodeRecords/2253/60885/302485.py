def print_nums():
    for i in range(10):
        l = i * 10
        sub = nums[l:l+10]
        for num in sub:
            print('{:10d}'.format(num), end='')
        print()
    print()

n,m = list(map(int, input().split()))
nums = list(map(int, input().split()))
# print_nums()
for i in range(m):
    command = list(map(int, input().split()))
    op = command[0]
    if op in [1,4,5]:
        l = command[1] - 1
        r = command[2]
        x = command[3]
        sub = sorted(nums[l:r])
        # print(sub)
        if op == 1:
            print(sub.index(x)+1)
        elif op == 4:
            for i in range(len(sub)):
                if sub[i] > x:
                    print(sub[i-1])
                    break
            else:
                print(sub[-1])
        elif op == 5:
            for i in range(len(sub)):
                if sub[-1-i] < x:
                    print(sub[-i])
                    break
            else:
                print(sub[0])
    elif op == 2:
        l = command[1] - 1
        r = command[2]
        k = command[3] - 1
        print(sorted(nums[l:r])[k])
    elif op == 3:
        pos = command[1] - 1
        nums[pos] = command[2]
    # print_nums()
    # print(nums)

